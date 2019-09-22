# Hey, how are you all? Let's discuss and get started with our stories discussion. The epics are data science, analytics, and engineering. We have Falcon, Chirag, and Yashica as team members for this project. Falcon is working on story 123 for NLP key feature extraction and it belongs to the data science epic. how many stories point to the task you are doing Falcon? Story points for story 123 will be 5. Another story under data engineering is pending and its story points are 8. Well, this was the quick summary and total story points for this sprint is 13. Yashica is working on story 569 for Cloudformation and it belongs to the data engineering epic. how many stories point to the task you are doing Yashica? Story points for story 569 will be 3. Chirag is working on story 4456 for intent extraction and it belongs to the data engineering epic. how many stories point to the task you are doing Chirag? Story points for story 4456 will be 3

# The questions which need to be answered?
# Who are the team members?
# What stories they are working on
# What are the epics?
# What stories are related to Epics?
import nltk
from nameparser.parser import HumanName
from nltk.corpus import wordnet
text='''
Hey, how are you all? Let's discuss and get started with our stories discussion. 
The epics are data science, analytics,  research and development, and engineering. 
We have Falcon, Chirag, Raman and Yashica as team members for this project. 
Falcon is working on story 123 for NLP key feature extraction and it belongs to the data science epic. 
how many stories point to the task you are doing Falcon? Story points for story 123 will be 5. 
Another story under data engineering is pending and its story points are 8. 
Well, this was the quick summary and total story points for this sprint is 13. 
Yashica is working on story 569 for Cloudformation and it belongs to the data engineering epic. 
how many stories point to the task you are doing Yashica? Story points for story 569 will be 3. 
Chirag is working on story 4456 for intent extraction and it belongs to the data engineering epic. 
how many stories point to the task you are doing Chirag? Story points for story 4456 will be 3
Raman will be working on story 555 some analysis during free time and it belongs to research and development.

we will connect after a short coffee break. Thank you

'''

import nltk
from nameparser.parser import HumanName

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

# print(get_human_names(text[1:]))