from pyspark.sql import SparkSession
import matplotlib.pyplot as plt

spark = SparkSession.builder.appName("DataVisualization").getOrCreate()
data = [("Mathesh", 21), ("Arun", 23), ("Kumar", 25)]
columns = ["Name", "Age"]
df = spark.createDataFrame(data, columns)
ages = [row['Age'] for row in df.collect()]
plt.bar(["Mathesh", "Arun", "Kumar"], ages)
plt.xlabel("Names")
plt.ylabel("Ages")
plt.title("Age Bar Chart")
plt.show()
spark.stop()
