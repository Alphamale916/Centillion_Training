from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

spark = SparkSession.builder.appName("Aggregations").getOrCreate()
data = [("Mathesh", "IT", 5000), ("Arun", "IT", 6000), ("Kumar", "HR", 4000)]
columns = ["Name", "Department", "Salary"]
df = spark.createDataFrame(data, columns)
agg_df = df.groupBy("Department").agg(avg("Salary").alias("AverageSalary"))
agg_df.show()
spark.stop()
