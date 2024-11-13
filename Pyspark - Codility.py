from pyspark.sql import SparkSession # type: ignore
from pyspark.sql.functions import sum, avg, count, col, row_number # type: ignore
from pyspark.sql import Window # type: ignore
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, DateType # type: ignore
from datetime import date

spark = SparkSession.builder.appName("Movie Booking Analytics").getOrCreate()

schema = StructType([
    StructField("transaction_id", StringType(), True),
    StructField("user_id", StringType(), True),
    StructField("product_id", StringType(), True),
    StructField("category", StringType(), True),
    StructField("amount", DoubleType(), True),
    StructField("transaction_date", DateType(), True)
])

data = [
    ("A13124", "A1", "TICKET", "MOVIE", 12.0, date(2023, 11, 1)),
    ("B24631", "C3", "FOOD", "SNACKS", 8.0, date(2023, 11, 1)),
    ("C35742", "E5", "DRINK", "SNACKS", 5.0, date(2023, 11, 1)),
    ("D46853", "A1", "TICKET", "MOVIE", 12.0, date(2023, 11, 2)),
    ("E57964", "G4", "FOOD", "SNACKS", 10.0, date(2023, 11, 2)),
    ("F68175", "C3", "TICKET", "MOVIE", 15.0, date(2023, 11, 3)),
    ("G79286", "E5", "FOOD", "SNACKS", 7.0, date(2023, 11, 3)),
    ("H81397", "G4", "DRINK", "SNACKS", 5.0, date(2023, 11, 4)),
    ("I92408", "G4", "TICKET", "MOVIE", 12.0, date(2023, 11, 4)),
    ("J13519", "A1", "FOOD", "SNACKS", 9.0, date(2023, 11, 5)),
    ("K24620", "G4", "TICKET", "MOVIE", 12.0, date(2023, 11, 5)),
    ("L35721", "A1", "DRINK", "SNACKS", 6.0, date(2023, 11, 6)),
    ("M46832", "E5", "TICKET", "MOVIE", 10.0, date(2023, 11, 6))
]

df = spark.createDataFrame(data, schema=schema)

user_spend = df.groupBy("user_id").agg(
    sum("amount").alias("total_spent"),
    avg("amount").alias("avg_transaction")
)

count = df.groupBy("user_id", "category").agg(count("category").alias("count"))
window_spec = Window.partitionBy("user_id").orderBy(col("count").desc())

category_ranked = count.withColumn("rank", row_number().over(window_spec)).filter(col("rank") == 1).drop("rank")

result = user_spend.join(category_ranked, on="user_id").select("user_id", "total_spent", "avg_transaction", col("category").alias("favorite_category"))

result.show()