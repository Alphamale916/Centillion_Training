from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression

spark = SparkSession.builder.appName("MLlibBasics").getOrCreate()
data = [(1, 2), (2, 3), (3, 4)]
columns = ["Feature", "Label"]
df = spark.createDataFrame(data, columns)
vec_assembler = VectorAssembler(inputCols=["Feature"], outputCol="Features")
vec_df = vec_assembler.transform(df)
lr = LinearRegression(featuresCol="Features", labelCol="Label")
model = lr.fit(vec_df)
print("Coefficients:", model.coefficients)
spark.stop()
