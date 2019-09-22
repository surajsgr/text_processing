text='''
Zebras are several species of African equids (horse family) united by their distinctive black and white stripes. 
Their stripes come in different patterns, unique to each individual. 
They are generally social animals that live in small harems to large herds. 
Unlike their closest relatives, horses and donkeys animals, zebras have never been truly domesticated.
There are three species of zebras: the plains zebra, the Grévy's zebra and the mountain zebra. 
The plains zebra and the mountain zebra belong to the subgenus Hippotigris, but Grévy's zebra is the sole species of subgenus Dolichohippus. 
The latter resembles an ass, to which it is closely related, while the former two are more horse-like. 
All three belong to the genus Equus, along with other living equids. 
The unique stripes of zebra make them one of the animals most familiar to people. 
They occur in a variety of habitats, such as grasslands, savannas, woodlands, thorny scrublands, mountains, and coastal hills.
However, various anthropogenic factors have had a severe impact on zebra populations, in particular hunting for skins and habitat destruction. 
Grévy's zebra and the mountain Zebras are endangered. 
While plains zebras are much more plentiful, one subspecies, the quagga, became extinct in the late 19th century – though there is currently a plan, called the Quagga Project, that aim to breed zebras that are phenotypically similar to the quagga in a process called breeding back.
'''



#steps to follow

  #word_tokenize the questions given
  #remove all the stop words from questions
  #chunk the words related to j=='NNS' or j=='VBN' or j=='NNP' or j=='JJS' or j=='CD' or j=='NN'
  #word_tokenize the text given
  # check whether the question_word tokenize is a subset of word tokenize or not in text
  # if that is a subset then we need to extract the lines where the answer is there according to question order
  # then compare with the answers given and check whether those answer substring are the part of answers (that has been extracted) or not
  #create a dictionary to maintain the order

questions=["Which Zebras are endangered?","What is the aim of the Quagga Project?","Which animals are some of their closest relatives?","Which are the three species of zebras?","Which subgenus do the plains zebra and the mountain zebra belong to?"]

answers='''subgenus Hippotigris;the plains zebra, the Grévy's zebra and the mountain zebra;horses and donkeys;aim to breed zebras that are phenotypically similar to the quagga;Grévy's zebra and the mountain Zebras'''
result=answers.split(';')
# print(result)

import nltk
from nltk.corpus import stopwords


stop=set(stopwords.words('english'))
# print(stop)
sent=nltk.tokenize.sent_tokenize(text)
# print(sent)

l=[]
s = ''
for w in questions:
    words=nltk.tokenize.word_tokenize(w)
    for r in words:
        wo=r.lower()
        if wo in stop :
            if wo.capitalize() in words:

               words.remove(wo.capitalize())

    for w in words:
        s+=' '+w
s.strip(' ')
s.lstrip(' ')

question_new=s.split('?')
# print(question_new)
result_new=[]
for s in question_new:
    new=nltk.tokenize.word_tokenize(s.lstrip(' '))
    pos=nltk.pos_tag(new)
    # print(pos)
    sentt=nltk.ne_chunk(pos,binary=False)
    person = set()
    for i,j in pos:
        if j=='NNS' or j=='VBN' or j=='NNP' or j=='JJS' or j=='CD' or j=='NN':
            person.add(i)
            result_new.append(person)

new_result=[]
for i in result_new:
    if i not in new_result:
        new_result.append(i)
print(new_result)
L=[]
for i in new_result:
    for s in sent:

       sent_new=nltk.tokenize.word_tokenize(s)
       new_set=set(sent_new)
       if i.issubset(new_set):
           print(L.append(s))
print(L)
final_list=[]

d={}
print(result)
for i in range(len(result)):
    for j in range(len(L)):
        if result[i] in L[j]:
            d[j]=result[i]




ordered_dict=dict(sorted(d.items()))

for k,v in ordered_dict.items():
    print(v)











