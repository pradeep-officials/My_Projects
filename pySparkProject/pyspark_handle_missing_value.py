import logging

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, isnan, count
try:
    logging.basicConfig(level=logging.INFO,filename='app.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')
    logging.warning('This will get logged to a file')
    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')

    spark=SparkSession.builder.appName("Spark_MissingValues").master("local[*]").getOrCreate()
    # spark.sparkContext.setLogLevel("INFO")
    logging.info('This is an info message')
    df=spark.read.csv("inputs/nba2.csv")
    logging.error("Exception occurred", exc_info=True)

    print("getting conf details")
    print(spark.sparkContext.getConf().get("spark.executor.instances"))
    print(df.rdd.getNumPartitions())

    print(df.count())
    df.show(truncate=False)
    df_na=df.filter(df["_c5"].isNull())
    df_na.show()
    print(df_na.count())
    df_na2 = df.filter(df["_c5"].isNull() & df["_c13"].isNotNull())
    df_na2.show()
    print(df_na2.count())
    print(df.columns)
    df_na3 = df.select([count(when(col(c).isNull(),c)).alias(c) for c in df.columns])
    df_na3.show()
    print(df_na3.count())
    df4=df.limit(100)
    print(df4.show(100,truncate=False))
    df4.dropna(how='all')
    df_dropna=df4.dropna(how='any')
    print("Drop NA all cnt...",df_dropna.count())
    print(df_dropna.show())
    # df_dropna2=df4.dropna(how='any')
    # print(df_dropna2.count())
    # print(df_dropna2.show())
except:
    logging.error("Exception occurred", exc_info=True)
