from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("BasicSetupExample").setMaster("local")
sc = SparkContext(conf=conf)
print("SparkContext initialized with app name:", sc.appName)
sc.stop()
