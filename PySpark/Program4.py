#setting env
import os
os.environ['SPARK_HOME'] = "/Users/AlphaMale/Documents/Spark"
os.environ['PYSPARK_DRIVER_PYTHON'] = 'jupyter'
os.environ['PYSPARK_DRIVER_PYTHON_OPTS'] = 'lab'
os.environ['PYSPARK_PYTHON'] = 'python'


from pyspark.sql import SparkSession

numbers = [1, 2, 3, 4, 5]
rdd = spark.sparkContext.parallelize(numbers)

a =rdd.collect()
print(a)
data = [("Tim", 20), ("Kim", 35), ("Jim", 30), ("Pym", 40)]
rdd = spark.sparkContext.parallelize(data)

print("All elements of the rdd: ", rdd.collect())

count = rdd.count()
print("The total number of elements in rdd: ", count)


first_element = rdd.first()
print( first_element)

rdd.foreach(lambda x: print(x))