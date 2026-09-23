import dlt

@dlt.table
def transform_date():
    return spark.range(10)