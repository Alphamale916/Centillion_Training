from pyspark import SparkContext

sc = SparkContext("local", "RDD Transformations")
data = [1, 2, 3, 4, 5]
rdd = sc.parallelize(data)
rdd_squared = rdd.map(lambda x: x ** 2)
print("Squared RDD:", rdd_squared.collect())
sc.stop()
