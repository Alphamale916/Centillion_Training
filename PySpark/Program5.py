import os
os.environ['SPARK_HOME'] = "Users/AlphaMale/Documents/Spark"
os.environ['PYSPARK_DRIVER_PYTHON'] = 'jupyter'
os.environ['PYSPARK_DRIVER_PYTHON_OPTS'] = 'lab'
os.environ['PYSPARK_PYTHON'] = 'python'

from pyspark.sql import SparkSession
from pyspark.sql.functions import desc


spark = SparkSession.builder.appName("DummyFrame").getOrCreate()

rdd = spark.sparkContext.textFile("./data/data.txt")

result_rdd = rdd.flatMap(lambda line: line.split(" ")) \
    .map(lambda word: (word, 1)) \
    .reduceByKey(lambda a, b: a + b) \
    .sortBy(lambda x: x[1], ascending=False)

result_rdd.take(10)

df = spark.read.text("./data/data.txt")


result_df = df.selectExpr("explode(split(value, ' ')) as word") \
    .groupBy("word").count().orderBy(desc("count"))

result_df.take(10)



