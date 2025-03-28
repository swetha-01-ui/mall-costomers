from pyspark.sql.functions import col, avg, count
from load_data import load_customer_data

def analyze_spending_score(df):
    print("\n📊 Spending Score Distribution:")
    df.groupBy("Spending Score (1-100)") \
      .count() \
      .orderBy("Spending Score (1-100)") \
      .show()

    print("\n📈 Average Income by Spending Score Range:")
    df.groupBy("Spending Score (1-100)") \
      .agg(avg("Annual Income (k$)").alias("Avg Income"), count("*").alias("Count")) \
      .orderBy("Spending Score (1-100)") \
      .show()

if __name__ == "__main__":
    df = load_customer_data("data/Mall_Customers.csv")
    analyze_spending_score(df)
