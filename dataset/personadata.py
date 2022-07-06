import json
  
# Opening JSON file
f = open('dataset/en_persona.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list
#for each in data:
 #   print(each)

"""
data2=data[0]
list2=data2["dialogue"]
print(data2["dialogue"])
print(type(data2["dialogue"]))
print(list2)
for each in list2:
    print(each)
testo=list2[0]
testo.append("")
k1=["title","body","label"]
d1=zip(k1,testo)
res_list=[]
print(testo)
print(dict(d1))"""


k1=["persona","b_sentence","label"]
res_list=[]
for each in data:
    to_get=each['dialogue']
    for i in range(len(to_get)):
        print(to_get[i])
        to_get[i].append("")
        d1=zip(k1,to_get[i])
        d1=dict(d1)
        res_list.append(d1)
print(res_list)

Str = json.dumps(res_list)
with open('res_data.json', 'w', encoding='utf-8') as f2:
    json.dump(res_list, f2, ensure_ascii=False, indent=4)





  
# Closing file
f.close()