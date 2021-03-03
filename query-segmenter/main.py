from query_segmenter.unsupervised import Segmenter
import pandas as pd
import joblib


df = pd.read_csv("yahoo_keywords.min.csv")
queries = df["keyword"].to_list()

segmenter = Segmenter()
segmenter.compute_scores(queries)

segments = segmenter.segment('鼻血 よく 出る 大人')
print(segments)
