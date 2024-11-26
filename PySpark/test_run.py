from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("TestSparkJob") \
    .config("spark.hadoop.fs.defaultFS", "hdfs://localhost:9000") \
    .config("spark.executor.memory", "2g") \
    .getOrCreate()

data = [
    ("Aarav", 28),
    ("Vivaan", 33),
    ("Ishaan", 25),
    ("Aadhya", 30),
    ("Ananya", 27),
    ("Saanvi", 22),
    ("Rohan", 35),
    ("Aditya", 29),
    ("Madhavi", 24),
    ("Krishna", 31)
]

columns = ["Name", "Age"]

df = spark.createDataFrame(data, columns)

df.show()

average_age = df.groupBy().avg("Age").collect()[0][0]
print(f"Average Age: {average_age}")

spark.stop()
