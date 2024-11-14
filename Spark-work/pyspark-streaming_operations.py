from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("StreamingOperations").getOrCreate()
lines = spark.readStream.format("socket").option("host", "localhost").option("port", 9999).load()
words = lines.selectExpr("explode(split(value, ' ')) as word")
word_counts = words.groupBy("word").count()
query = word_counts.writeStream.outputMode("complete").format("console").start()
query.awaitTermination()
spark.stop()
