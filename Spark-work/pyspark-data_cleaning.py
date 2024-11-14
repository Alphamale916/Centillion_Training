from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("DataCleaning").getOrCreate()
data = [("Mathesh", None), ("Arun", 23), ("Kumar", None)]
columns = ["Name", "Age"]
df = spark.createDataFrame(data, columns)
df = df.na.fill({"Age": 20})
df = df.withColumn("Age", col("Age").cast("int"))
df.show()
spark.stop()
