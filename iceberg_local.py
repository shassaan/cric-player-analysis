from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Cricket Iceberg Ingestion") \
    .config("spark.sql.catalog.local", "org.apache.iceberg.spark.SparkCatalog") \
    .config("spark.sql.catalog.local.type", "hadoop") \
    .config("spark.sql.catalog.local.warehouse", "warehouse/") \
    .getOrCreate()

# Read sample data
df = spark.read.option("multiLine", True).json("data/sample.json")
df.show(truncate=False)

# Write to Iceberg table
df.writeTo("local.cricket.players").using("iceberg").createOrReplace()

# Query the table
spark.sql("SELECT player, year, icc_ranking FROM local.cricket.players").show()

spark.stop()