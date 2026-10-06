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
    "abfss://WS_ABC_Hospital@onelake.dfs.fabric.microsoft.com/LH_Hospital_Project.Lakehouse/Files/landing_old/hospitals_20260928_224142.parquet"  

    
)

print(df.count())
# import notebookutils

# notebookutils.notebook.exit("2")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.read.csv(
    "abfss://WS_ABC_Hospital@onelake.dfs.fabric.microsoft.com/LH_Hospital_Project.Lakehouse/Files/landing/adls_csv/lab_results/lab_results_2026_09_14_1329.csv"
)

print(df.count())
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
