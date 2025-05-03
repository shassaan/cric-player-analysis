

from pyspark import SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.types import DoubleType, FloatType, LongType, StructType, StructField, StringType, IntegerType



warehouse_path = "./warehouse"
iceberg_spark_jar = 'org.apache.iceberg:iceberg-spark-runtime-3.4_2.12:1.4.3'
iceberg_spark_ext = 'org.apache.iceberg:iceberg-spark-extensions-3.4_2.12:1.4.3'
catalog_name = "demo"

# Setup iceberg config
conf = SparkConf().setAppName("YourAppName") \
    .set("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions") \
    .set(f"spark.sql.catalog.{catalog_name}", "org.apache.iceberg.spark.SparkCatalog") \
    .set('spark.jars.packages', iceberg_spark_jar) \
    .set('spark.jars.packages', iceberg_spark_ext) \
    .set(f"spark.sql.catalog.{catalog_name}.warehouse", warehouse_path) \
    .set(f"spark.sql.catalog.{catalog_name}.type", "hadoop")\
    .set("spark.sql.defaultCatalog", catalog_name)

# Create spark session
spark = SparkSession.builder.config(conf=conf).getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

schema = StructType([
    StructField("vendor_id", LongType(), True),
    StructField("trip_id", LongType(), True),
    StructField("trip_distance", FloatType(), True),
    StructField("fare_amount", DoubleType(), True),
    StructField("store_and_fwd_flag", StringType(), True)
])
spark.sql("CREATE DATABASE IF NOT EXISTS db")




# Create an empty table in the Iceberg catalog
spark.sql("""
    CREATE TABLE IF NOT EXISTS db.taxis (
        vendor_id BIGINT,
        trip_id BIGINT,
        trip_distance FLOAT,
        fare_amount DOUBLE,
        store_and_fwd_flag STRING
    )
    USING iceberg
""")

# Insert data into the Iceberg table
data = [
    (1, 1000371, 1.8, 15.32, "N"),
    (2, 1000372, 2.5, 22.15, "N"),
    (2, 1000373, 0.9, 9.01, "N"),
    (1, 1000374, 8.4, 42.13, "Y")
]
df = spark.createDataFrame(data, schema)
df.writeTo("db.taxis").append()

# Read the table
df = spark.read.table("db.taxis")
df.show()