import nltk
from nameparser.parser import HumanName
from nltk.corpus import wordnet
import re

text='''
Hey, how are you all? Let's discuss and get started with our stories discussion. 
The epics are data science, data analytics,  research and development, and data engineering. 
We have Falcon, Chirag, Raman and Yashica,Samark,George,John as team members for this project. 
Falcon is working on story 123 for NLP key feature extraction and it belongs to the data science epic. 
how many stories point to the task you are doing Falcon? Story points for story 123 will be 5. 
Another story under data engineering is pending and its story points are 8. 
Well, this was the quick summary and total story points for this sprint is 13. 
Yashica is working on story 569 for Cloudformation and it belongs to the data engineering epic. 
how many stories point to the task you are doing Yashica? Story points for story 569 will be 3. 
Chirag is working on story 4456 for intent extraction and it belongs to the data engineering epic. 
how many stories point to the task you are doing Chirag? Story points for story 4456 will be 3.
Raman will be working on story 555 for some analysis during free time and it belongs to research and development epic.
Suraj will be working on story 1456 for some analysis during free time and it belongs to the data analytics.
Samark belongs to the data engineering.
George is working on analysis and belongs to data science.
John is working for other tasks and it belongs to data engineering.




we will connect after a short coffee break. Thank you

'''

text1='''
Hey, how are you all? Let's discuss and get started with our stories discussion. 
The epics are data science, data analytics,  research and development, and data engineering. 
We have Falcon, Chirag, Raman and Yashica,Samark,George as team members for this project. 
Falcon is working on story 123 for NLP key feature extraction and it belongs to the data science epic. 
how many stories point to the task you are doing Falcon? Story points for story 123 will be 5. 
Another story under data engineering is pending and its story points are 8. 
Well, this was the quick summary and total story points for this sprint is 13. 
Yashica is working on story 569 for Cloudformation and it belongs to the data engineering epic. 
how many stories point to the task you are doing Yashica? Story points for story 569 will be 3. 
Chirag is working on story 4456 for intent extraction and it belongs to the data engineering epic. 
how many stories point to the task you are doing Chirag? Story points for story 4456 will be 3.
Raman will be working on story 555 for some analysis during free time and it belongs to research and development epic.
Suraj will be working on story 1456 for some analysis during free time and it belongs to the data analytics.
Samark is working for other tasks and belongs to the data engineering.
George is working for analysis and belongs to data science.



we will connect after a short coffee break. Thank you



'''
def get_human_names(text):
    tokens = nltk.tokenize.word_tokenize(text[2:])
    pos = nltk.pos_tag(tokens)
    sentt = nltk.ne_chunk(pos, binary = False)
    person_list = []
    person = []
    name = ""
    for subtree in sentt.subtrees(filter=lambda t: t.label() == 'PERSON' or t.label() == 'GPE'):
        for leaf in subtree.leaves():
            person.append(leaf[0])

        # if len(person) > 1: #avoid grabbing lone surnames
        #     for part in person:
        #         name += part + ' '
        #     if name[:-1] not in person_list:
        #         person_list.append(name[:-1])
        #     name = ''


    return set(person)

# names=list(get_human_names(text[1:]))
# print(names)


def get_title(text):
    tokens = nltk.tokenize.sent_tokenize(text)
    # tokens_word=nltk.word_tokenize(tokens)
    #
    # pos = nltk.pos_tag(tokens_word)
    story=[]
    for str in tokens:
        if 'belongs' in str:

          story.append(str)

    l = []
    for str in story:
        token_word = nltk.tokenize.word_tokenize(str)
        pos = nltk.pos_tag(token_word)
        for i,j in pos:
            if j=='NNP':
                l.append(i)
    return l
    # d ={}
    # for i,j in pos:
    #     print(i,j)




def main(text):
    names=list(get_human_names(text[1:]))
    names_new=get_title(text)
    for i in names_new:
        if i not in names:
            names_new.remove(i)
    return names_new



# print(main(text1))