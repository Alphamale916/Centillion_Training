from pyspark.sql import SparkSession
import os

spark = SparkSession.builder.appName("ParquetToCSV").getOrCreate()

parquet_file_path = "path/to/input/file.parquet"
output_directory = "dataframe_operations_output "

df = spark.read.parquet(parquet_file_path)

row_count = df.count()

df.write.mode("overwrite").option("header", "true").csv(output_directory)

metadata_path = os.path.join(output_directory, "metadata.txt")
with open(metadata_path, "w") as meta_file:
    meta_file.write(f"RowCount: {row_count}")
