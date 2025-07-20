# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "52e8d1b2-a10c-4579-bbc0-557f24c10f64",
# META       "default_lakehouse_name": "lh_silver",
# META       "default_lakehouse_workspace_id": "ac8278dd-5e74-4219-a61f-c6d1989495dc",
# META       "known_lakehouses": [
# META         {
# META           "id": "52e8d1b2-a10c-4579-bbc0-557f24c10f64"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

%run /DeltaLakeFunctions

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### Iterate through all tables in lakehouse and run OPTIMIZE and VACCUM commands

# CELL ********************

df = spark.sql("show tables")
tableList = df.select("tableName").rdd.flatMap(lambda x:x).collect()
# print (tables)
for table in tableList:
    print ("optimizing",table)
    optimizeDelta(table)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
