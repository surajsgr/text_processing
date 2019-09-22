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
Samark will work for some engineering tasks and belongs to the data engineering.
George will work on other tasks and it belongs to data science.




we will connect after a short coffee break. Thank you

'''


def get_title(text):
    tokens = nltk.tokenize.sent_tokenize(text)

    story_epic = []
    for str in tokens:
        if 'belongs' in str:
            story_epic.append(str)
    title = story_epic[1:]
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
    # l=[]
    # for sent in title:
    #     word=sent.split(' ')
    #     if 'for' and 'and' in word:
    #         i=word.index['for']
    #         j=word.index['and']
    #         new_word=word[i:j]
    #         str=''
    #         for w in range(1,len(new_word)):
    #             str+=' '+new_word[w]
    #             l.append(str)
    # return l
    l=[]
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

        # for str in word:
        #     if 'for' and 'and' in str:
        #         i=str.index('for')
        #         j=str.index('and')
        #
        #         new_word=word[i:j]
    #     for w in range(1,len(new_word)):
    #         str+=' '+new_word[w]
    #     l.append(str)
    # return l

    #
    #     elif 'on' and 'and' in word:
    #         l=word.index('on')
    #         r=word.index('and')
    #         new_word = word[l:r]
    #
    #         for w in range(1, len(new_word)):
    #
    #             str += ' ' + new_word[w]
    #             l.append(str)
    # print(str)




print(get_title(text))