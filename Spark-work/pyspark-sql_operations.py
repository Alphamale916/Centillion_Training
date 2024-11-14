from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SQLOperations").getOrCreate()
data = [("Mathesh", "IT"), ("Arun", "HR"), ("Kumar", "Finance")]
columns = ["Name", "Department"]
df = spark.createDataFrame(data, columns)
df.createOrReplaceTempView("employees")
result = spark.sql("SELECT * FROM employees WHERE Department = 'IT'")
result.show()
spark.stop()
