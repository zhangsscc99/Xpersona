#data labeling file version 1.0
#high-precision algorithm
import json
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
import random

  
# Opening JSON file
f = open('dataset/new_dataset.js')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
print(data)


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


#print(data[0])
k1=["title","body","label"]
res_list=[]

#positive samples:
#each pairs
for each in data:
    to_get=each['dialogue']
    to_getper=each['persona']
    #each dialogue
    for i in range(len(to_get)):
        #print(to_get[i])
        
        prepare_a=to_get[i][1].split(" ")
        #each persona
        for j in range(len(to_getper)):
            #the following line is used to see whether the sentence matches the persona
            
            
            prepare_p=to_getper[j].split(" ")
            counter=0
            #each word in persona
            for k in range(len(prepare_p)):


                #we use a simple high-precision function to label the dialogue. and here is the logic.
                #we need "stopwords" to reduce the noise caused by "the" "a" etc
                if prepare_p[k] in prepare_a and counter<1 and prepare_p[k] not in stopwords.words('english'):
                    counter+=1

            #if to_getper[j]==to_get[i][1]:
                    to_get[i][0]=to_getper[j]
                    to_get[i].append("true")
                    #we are just getting the right data form here.
                    d1=zip(k1,to_get[i])
                    d1=dict(d1)
                    res_list.append(d1)
                    
                else:
                    pass

        """
        d1=zip(k1,to_get[i])
        d1=dict(d1)
        res_list.append(d1)
        """



"""
for each in data:
    to_get=each['dialogue']
    to_getper=each['persona']
    for i in range(len(to_getper)):
        rand1=random.randint(0,range_d-1)
        while rand1==i:
            rand1=random.randint(0,range_d-1)
        #rand2=random.randint(0,range_d-1)
        #while rand2==rand1 or rand2==i:
        #    rand2=random.randint(0,range_d-1)
        while to_getper[i] in data[rand1]['persona']: #or to_getper[i] in data[rand2]['persona']:
            rand1=random.randint(0,range_d-1)
            while rand1==i:
                rand1=random.randint(0,range_d-1)
        #    rand2=random.randint(0,range_d-1)
        #    while rand2==rand1 or rand2==i:
        #        rand2=random.randint(0,range_d-1)
        #here,we have picked two sentences
        #we have persona and 2 sentences .
        for j in range(len(data[rand1]['dialogue'])):

            prepare_a1=data[rand1]['dialogue'][j][1].split(" ")
            #prepare_a2=data[rand2]['dialogue'][j][1].split(" ")
            

            prepare_p=to_getper[i].split(" ")
            counter=0
            for k in range(len(prepare_p)):


                if (prepare_p[k] in prepare_a1 or prepare_p[k] in prepare_a2) and prepare_p[k] not in stopwords.words('english'):
                    pass
                else:
                    print(res_list2)
                    container1=data[rand1]['dialogue']
                    container1[0]=to_getper[i]
                    container1.append("false")
                    container2=data[rand2]['dialogue']
                    container2[0]=to_getper[i]
                    container2.append("false")


                    f1=zip(k1,container1)
                    f1=dict(f1)
                    f2=zip(k1,container2)
                    f2=dict(f2)
                    res_list2.append(f1)
                    res_list2.append(f2)

            
"""

#add negative samples:
#negative sampling
#for negative sampling, our data labeling algorithm is the same as above(for positive sampling)
#However, since we need to choose different dialogues for the same persona, we modified the codes. 
#The reason is that, for positive sampling, each time when we meet a persona, we just need to check whether within the same pair, the dialogues
#can be matched right. But here, for negative sampling, we need to do this on purpose, so we choose dialogues out of the same pair. 
#so the lines of codes are a bit different from above. But this is still the same "high-precision" function for the "if" code.

range_d=len(data)
ans_list2=[]
for i in range(len(data)):
    #to_get=data[i]['dialogue']
    to_getper2=data[i]['persona']
    rand1=random.randint(0,range_d-1)
    
    while rand1==i:
        rand1=random.randint(0,range_d-1)
    #not choosing those dialogues with same persona
    for n in range(len(to_getper2)):
        while to_getper2[n] in data[rand1]['persona']:
            rand1=random.randint(0,range_d-1)

    to_get2=data[rand1]['dialogue']

    for m in range(len(to_get2)):
        prepare_a1=to_get2[m][1].split(" ")

        for j in range(len(to_getper2)):
            prepare_p2=to_getper2[j].split(" ")
            counter=0
            for k in range(len(prepare_p2)):
                #stopwords list is used to deal with "the" "a " etc.
                if prepare_p2[k] in prepare_a1  and prepare_p2[k] not in stopwords.words('english'):
                    pass
                

                else:
                    #counter is used to end the loop. (once we get that it is a negative sample)
                    #the algorithm here is still the high-precision one.
                    if counter<1:

                        counter+=1
                        to_get2[m][0]=to_getper2[j]
                        to_get2[m].append("false")
                        g1=zip(k1,to_get2[m])
                        
                        g1=dict(g1)
                        if g1['label']!="true":
                            res_list.append(g1)

                


   
# we add the positive samples and negative samples into the same container. The positive samples go first, and then the negative samples 
#follow behind. 
Str = json.dumps(res_list)
with open('train_persona_dialogue.json', 'w', encoding='utf-8') as f2:
    json.dump(res_list, f2, ensure_ascii=False, indent=4)



# Closing file
f2.close()
"""
Str2 = json.dumps(ans_list2)
with open('f_persona_res.json', 'w', encoding='utf-8') as f5:
    json.dump(ans_list2, f5, ensure_ascii=False, indent=4)

# Closing file
f5.close()
"""
#print(stopwords.words('english'))
print(len(data))