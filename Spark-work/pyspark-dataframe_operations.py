from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("DataFrameOperations").getOrCreate()
data = [("Mathesh", 21), ("Arun", 23), ("Kumar", 25)]
columns = ["Name", "Age"]
df = spark.createDataFrame(data, columns)
df.show()
spark.stop()
