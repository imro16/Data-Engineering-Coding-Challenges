from pyspark.sql import SparkSession
from pyspark.sql.functions import sha2, concat_ws

# Initialize Spark session
spark = SparkSession.builder \
    .appName("CSV Anonymization") \
    .getOrCreate()

# Load CSV into DataFrame
df = spark.read.csv('data.csv', header=True)

# Anonymize columns
anonymized_df = df.withColumn('first_name', sha2('first_name', 256)) \
                  .withColumn('last_name', sha2('last_name', 256)) \
                  .withColumn('address', sha2('address', 256))

# Save the anonymized data
anonymized_df.write.csv('anonymized_data_spark.csv', header=True)

spark.stop()
print("Anonymized CSV file 'anonymized_data_spark.csv' generated successfully using PySpark.")
