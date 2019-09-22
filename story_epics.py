import nltk
from nameparser.parser import HumanName
from nltk.corpus import wordnet
import re
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
how many stories point to the task you are doing Chirag? Story points for story 4456 will be 3.
Raman will be working on story 555 for some analysis during free time and it belongs to the research and development epic.
Suraj will be working on story 2341 for some other tasks and  belongs to the data analysis epic for.

we will connect after a short coffee break. Thank you

'''


def get_epics(text):
    tokens = nltk.tokenize.sent_tokenize(text)
    # tokens_word=nltk.word_tokenize(tokens)
    #
    # pos = nltk.pos_tag(tokens_word)
    story_epic=[]
    for str in tokens:
        if 'belongs' in str:

          story_epic.append(str)
    l = []
    for str in story_epic:
        token_word = nltk.tokenize.word_tokenize(str)
        pos = nltk.pos_tag(token_word)
        print(pos)


        # d={}

    #     for i,j in pos:
    #     #     idx1 = pos.index('for')
    #     #     idx2 = pos.index('and')
    #     #     final = pos[idx1:idx2]
    #
    #         if (j=='NNS' or j=='NN') :
    #             print(i,j)
    # # return final




        # s=0
        # running=True

    #     for i in range(len(final)):
    #         if i<len(final)-1:
    #             if (final[i][1]=='NNS' and final[i+1][1]=='NN') or (final[i][1]=='NN' and final[i+1][1]=='NNS') or  (final[i][1]=='NN' and final[i+1][1]=='CC') or (final[i][1]=='CC' and final[i+1][1]=='NN'):
    #                 l.append((final[i][0]+' '+final[i+1][0]+ ' '+final[i+2][0]))
    # for word in l:
    #     if 'data' not in word:
    #         l.remove(word)
    # for str in l:
    #     if 'epics' not in str:
    #         idx=l.index(str)
    #         str+=' '+'epic'
    #         l.insert(idx,str)
    # return l


# def get_stories(text):
#         tokens = nltk.tokenize.sent_tokenize(text)
#         # tokens_word=nltk.word_tokenize(tokens)
#         #
#         # pos = nltk.pos_tag(tokens_word)
#         story = []
#         for str in tokens:
#             if 'story' in str:
#                 story.append(str)
#         final = []
#         for s in story:
#
#             output = re.findall(r"story [0-9]+", s)
#             for out in output:
#                 final.append(out)
#         return set(final)
#
#         # while s<len(final)+1:
#         #     new_list=final[s][1]
#         #     s=(s+1)%len(final)
#         #     next=final[s][1]
#         #     print(new_list,next)
#         #     s=s+1
#
#
#
#
#
#
#
#                     # s += 1
#                     # if l[s][1] == 'NN':
#                     #     print(l[s])
#
#
#
#
#
#
#



# epics=list(get_epics(text))
# stories=list(get_stories(text))
# final=zip(epics,stories)
# d={}
# for i,j in final:
#     d[i]=j
# print(d)
print(list(get_epics(text)))
def get_title(text):
    tokens = nltk.tokenize.sent_tokenize(text)
    # tokens_word=nltk.word_tokenize(tokens)
    #
    # pos = nltk.pos_tag(tokens_word)
    story_epic=[]
    for str in tokens:
        if 'epic' in str:

          story_epic.append(str)
    title=story_epic[1:]
    l=[]
    for sent in title:
        word=sent.split(' ')
        str=''
        i=word.index('for')
        j=word.index('and')
        new_word=word[i:j]
        for w in range(1,len(new_word)):
            str+=' '+new_word[w]
        l.append(str)
    return l



print(get_title(text))