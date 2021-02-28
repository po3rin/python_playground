# from sklearn.feature_extraction.text import CountVectorizer

# v = CountVectorizer(binary=True)
# docs = ["i am boy", "i am cat"]
# bow = v.fit_transform(docs)
# print(bow)
# print(v.vocabulary_)

import logging
from gensim.models import word2vec, Word2Vec

logging.basicConfig(
    format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# sentences = word2vec.Text8Corpus("ja.text8")
# model = word2vec.Word2Vec(sentences, size=100)
# model.save("models/model.bin")

model = Word2Vec.load('models/model.bin')
results = model.most_similar('猫', topn=5)
print(results)
