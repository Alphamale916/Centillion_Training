import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

data = {
    "EmployeeName": ["Alice", "Bob", "Catherine", "David", "Eve", "Frank"],
    "Department": ["Marketing", "Engineering", "Engineering", "Marketing", "Finance", "Finance"],
    "Salary": [3000, 4000, 5000, 3500, 4500, 4200]
}

df = pd.DataFrame(data)

table = pa.Table.from_pandas(df)

parquet_file_path = "sample_employees.parquet"

pq.write_table(table, parquet_file_path)
