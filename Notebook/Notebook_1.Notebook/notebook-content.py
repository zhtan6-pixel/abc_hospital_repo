# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "a2f96c88-feaa-4fc7-badf-585fe5ce3f2c",
# META       "default_lakehouse_name": "LH_Hospital_Project",
# META       "default_lakehouse_workspace_id": "06cffc3a-7a54-445c-b872-aa169731b47f",
# META       "known_lakehouses": [
# META         {
# META           "id": "a2f96c88-feaa-4fc7-badf-585fe5ce3f2c"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!
# Welcome to your new notebook
# Type here in the cell editor to add code!
from notebookutils import mssparkutils

mssparkutils.fs.cp(
    "abfss://WS_ABC_Hospital@onelake.dfs.fabric.microsoft.com/LH_Hospital_Project.Lakehouse/Files/source/lab_results/lab_results_2026_09_14_1329.csv",
    "abfss://WS_ABC_Hospital@onelake.dfs.fabric.microsoft.com/LH_Hospital_Project.Lakehouse/Files/landing/adls_csv/lab_results/lab_results_2026_09_14_1329.csv",
    recurse=False
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
