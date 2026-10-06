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

# =====================================================
# Parameters
# =====================================================

# source_folder = (
#     "abfss://WS_ABC_Hospital@onelake.dfs.fabric.microsoft.com/"
#     "LH_Hospital_Project.Lakehouse/Files/source/lab_results"
# )

# landing_root = (
#     "abfss://WS_ABC_Hospital@onelake.dfs.fabric.microsoft.com/"
#     "LH_Hospital_Project.Lakehouse/Files/landing/adls_csv/lab_results"
# )

source_folder = f"{workspace}/{source_path}"
landing_root = f"{workspace}/{landing_path}"


print(source_folder)
print(landing_root)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark",
# META   "frozen": false,
# META   "editable": true
# META }

# CELL ********************

from notebookutils import mssparkutils
from datetime import datetime

# =====================================================
# Convert watermark
# =====================================================

# watermark_dt = datetime.strptime(
#     watermark_value,
#     "%Y-%m-%d %H:%M:%S"
# )

if watermark_value:
    watermark_dt = datetime.strptime(
        watermark_value,
        "%Y-%m-%d %H:%M:%S"
    )
else:
    watermark_dt = datetime.strptime(
        "1900-01-01 00:00:00",
        "%Y-%m-%d %H:%M:%S"
    )

# =====================================================
# Create timestamp folder
# Example:
# landing/adls_csv/lab_results/20261003_180501/
# =====================================================

# batch_folder = datetime.now().strftime("%Y%m%d_%H%M%S")
# batch_folder = start_time.strftime("%Y-%m-%d_%H:%M:%S")

batch_folder = datetime.strptime(
    start_time,
    "%Y-%m-%d %H:%M:%S"
).strftime("%Y-%m-%d_%H:%M:%S")

destination_folder = f"{landing_root}/{batch_folder}"

try:
    mssparkutils.fs.mkdirs(destination_folder)
except:
    pass

# =====================================================
# Filter and Copy
# =====================================================

copied_files = []

for f in mssparkutils.fs.ls(source_folder):

    if not f.name.lower().endswith(".csv"):
        continue

    # Last modified timestamp
    modified_dt = datetime.fromtimestamp(f.modifyTime / 1000)

    if modified_dt > watermark_dt:

        source_file = f.path

        destination_file = (
            f"{destination_folder}/{f.name}"
        )

        print(f"Copying: {f.name}")
        # print(f"testing source_file: {source_file}")
        # print(f"testing destination_file: {destination_file}")


        mssparkutils.fs.cp(
            source_file,
            destination_file,
            recurse=False
        )

        copied_files.append(
            {
                "file_name": f.name,
                "modified_time": modified_dt
            }
        )

# =====================================================
# Summary
# =====================================================

if len(copied_files) == 0:
    print(f"No files copied. Removing folder: {destination_folder}")

    try:
        mssparkutils.fs.rm(
            destination_folder,
            recurse=True
        )
    except Exception as e:
        print(f"Failed to remove folder: {e}")

else:
    print(f"Copied {len(copied_files)} files")

    for x in copied_files:
        print(
            f"{x['file_name']} "
            f"{x['modified_time']}"
        )

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark",
# META   "frozen": false,
# META   "editable": true
# META }

# CELL ********************

# =====================================================
# Summary
# =====================================================

if len(copied_files) == 0:
    print(f"No files copied. Removing folder: {destination_folder}")

    try:
        mssparkutils.fs.rm(
            destination_folder,
            recurse=True
        )
    except Exception as e:
        print(f"Failed to remove folder: {e}")

else:
    print(f"Copied {len(copied_files)} files")

    for x in copied_files:
        print(
            f"{x['file_name']} "
            f"{x['modified_time']}"
        )

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
