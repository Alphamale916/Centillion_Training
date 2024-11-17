from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, avg, col
from pyspark.sql.window import Window
from pyspark.sql.types import StructType, StructField, IntegerType, DateType, DoubleType
from datetime import date

spark = SparkSession.builder.appName("Customer Transactions Analysis").getOrCreate()

schema = StructType([
    StructField("customer_id", IntegerType(), True),
    StructField("transaction_date", DateType(), True),
    StructField("amount", DoubleType(), True)
])

data = [
    (1, date(2023, 10, 1), 100.0),
    (1, date(2023, 7, 3), 500.0),
    (1, date(2023, 11, 5), 200.0),
    (1, date(2023, 9, 8), 150.0),
    (2, date(2023, 4, 1), 820.0),
    (2, date(2023, 12, 2), 120.0),
    (2, date(2023, 10, 4), 160.0),
    (2, date(2023, 10, 7), 930.0),
]

transactions = spark.createDataFrame(data, schema=schema)

cumulative_window = Window.partitionBy("customer_id").orderBy("transaction_date").rowsBetween(Window.unboundedPreceding, Window.currentRow)

rolling_window = Window.partitionBy("customer_id").orderBy("transaction_date").rowsBetween(-6, Window.currentRow)

result = transactions.withColumn(
    "cumulative_amount", sum("amount").over(cumulative_window)
).withColumn(
    "rolling_avg_amount", avg("amount").over(rolling_window)
)

result.select("customer_id", "transaction_date", "amount", "cumulative_amount", "rolling_avg_amount").show()
