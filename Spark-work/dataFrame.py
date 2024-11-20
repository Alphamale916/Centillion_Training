from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("PySpark Example") \
    .config("spark.some.config.option", "config-value") \
    .config("spark.executorEnv.PYSPARK_PYTHON", "path\\to\\python.exe")\
    .getOrCreate()

data = [("John", "Doe", 30), ("Jane", "Smith", 25), ("Sam", "Brown", 35)]
columns = ["First Name", "Last Name", "Age"]

df = spark.createDataFrame(data, columns)

df.show()

spark.stop()
