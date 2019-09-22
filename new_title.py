import nltk
from nameparser.parser import HumanName
from nltk.corpus import wordnet
import re

text='''
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


def get_title(text):
    tokens = nltk.sent_tokenize(text)
    story_epic = []
    epic = []
    for str in tokens:
        if 'belongs' in str:
            story_epic.append(str)
    for s in story_epic:
        if 'for' not in s:
            epic.append(s)
            a = story_epic.index(s)

    title = []
    for i in story_epic:
        if i not in epic:
            title.append(i)

    l = []
    for sent in title:
        word = sent.split(' ')
        str = ''
        i = word.index('for')
        j = word.index('and')
        new_word = word[i:j]
        for w in range(1, len(new_word)):
            str += ' ' + new_word[w]
        l.append(str)

    return l
    l1 = []
    for sent in epic:
        word = sent.split(' ')
        str = ''
        i = word.index('on')
        j = word.index('and')
        new_word = word[i:j]
        for w in range(1, len(new_word)):
            str += ' ' + new_word[w]
        l1.append(str)
    return l1
    for i in l1:
        l.insert(a, i)
    L=[x.lstrip() for x in l]
    return L



