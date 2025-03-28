from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("MallCustomersLoader") \
    .getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
def load_customer_data(path):
    spark = SparkSession.builder \
        .appName("MallCustomersLoader") \
        .getOrCreate()

    df = spark.read.csv(path, header=True, inferSchema=True)
    df.printSchema()
    df.show(5)
    return df

if __name__ == "__main__":
    load_customer_data("data/Mall_Customers.csv")



