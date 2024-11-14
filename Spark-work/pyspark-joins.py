from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Joins").getOrCreate()
data1 = [("Mathesh", 21), ("Arun", 23)]
data2 = [("Mathesh", "IT"), ("Arun", "HR")]
columns1 = ["Name", "Age"]
columns2 = ["Name", "Department"]
df1 = spark.createDataFrame(data1, columns1)
df2 = spark.createDataFrame(data2, columns2)
joined_df = df1.join(df2, on="Name", how="inner")
joined_df.show()
spark.stop()
