from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, col

spark = SparkSession.builder \
    .appName("Document Intelligence") \
    .master("local[*]") \
    .getOrCreate()

input_path = "data/clean_text/*.txt"

df = spark.read.text(input_path)

words_df = df.select(
    explode(
        split(col("value"), " ")
    ).alias("word")
)

word_counts = words_df.groupBy("word").count().orderBy(col("count").desc())

word_counts.show(20, truncate=False)

word_counts.write.mode("overwrite").csv("data/spark_output/word_counts")

spark.stop()
