
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
import pandas as pd

documentA = 'the man went out for a walk'
documentB = 'the children sat around the fire'



vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform([documentA, documentB])
feature_names = vectorizer.get_feature_names()
dense = vectors.todense()
denselist = dense.tolist()
df = pd.DataFrame(denselist, columns=feature_names)
print(df)

corpus = ['this is the first document',
        'this is the second second document',
        'and the third one',
        'is this the first document']
words_list = list()
for i in range(len(corpus)):
    words_list.append(corpus[i].split(' '))

import gensim
from gensim import corpora
from gensim import models
# 赋给语料库中每个词(不重复的词)一个整数id
dic = corpora.Dictionary(words_list)
new_corpus = [dic.doc2bow(words) for words in words_list]
tfidf = models.TfidfModel(new_corpus)
tfidf.save("tfidf.model")
# 载入模型
tfidf = models.TfidfModel.load("tfidf.model")
# 使用这个训练好的模型得到单词的tfidf值
tfidf_vec = []
for i in range(len(corpus)):
    string = corpus[i]
    string_bow = dic.doc2bow(string.lower().split())
    string_tfidf = tfidf[string_bow]
    tfidf_vec.append(string_tfidf)
# 输出 词语id与词语tfidf值
print(tfidf_vec)
