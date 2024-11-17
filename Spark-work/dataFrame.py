from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("PySpark Example") \
    .config("spark.some.config.option", "config-value") \
    .getOrCreate()

data = [("John", "Doe", 30), ("Jane", "Smith", 25), ("Sam", "Brown", 35)]
columns = ["First Name", "Last Name", "Age"]

df = spark.createDataFrame(data, columns)

df.show()

spark.stop()
