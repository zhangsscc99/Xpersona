
import math
import re
from collections import Counter
import json
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
import random


WORD = re.compile(r"\w+")
#preparing the cosine similarity function and word2vec function.

def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in list(vec1.keys())])
    sum2 = sum([vec2[x] ** 2 for x in list(vec2.keys())])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)



f = open('Xpersona copy/new_dataset.js')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
"""
print(data)
print(data[0])
print(data[0]['persona'])"""
cosine_data=[]
counter=0

k1=["title","body","label"]
res_list=[]

for i in range(len(data)):
    
    
    for j in range(len(data[i]['persona'])):
        p_to_be_docA=data[i]['persona'][j]
        for k in range(len(data[i]['dialogue'])):
            d_to_be_docB=data[i]['dialogue'][k][-1]
            
            
            

            vector1 = text_to_vector(p_to_be_docA)
            vector2 = text_to_vector(d_to_be_docB)

            cosine = get_cosine(vector1, vector2)
            k2=[]
            if cosine>0.25:
                k2.append(p_to_be_docA)
                k2.append(d_to_be_docB)
                k2.append('true')
                d1=zip(k1,k2)
                d1=dict(d1)
                res_list.append(d1)


            


Str = json.dumps(res_list)
with open('train_p_d_two.json', 'w', encoding='utf-8') as f2:
    json.dump(res_list, f2, ensure_ascii=False, indent=4)



# Closing file
f2.close()
                    





