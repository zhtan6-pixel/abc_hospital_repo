# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

df = spark.read.parquet(
    "abfss://WS_ABC_Hospital@onelake.dfs.fabric.microsoft.com/LH_Hospital_Project.Lakehouse/Files/landing/patients_20260928_224220.parquet"
)

print(df.count())

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
