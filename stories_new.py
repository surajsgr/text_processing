import nltk
from nameparser.parser import HumanName
from nltk.corpus import stopwords
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
Samark belongs to the data engineering.
George is working on analysis and belongs to data science.



we will connect after a short coffee break. Thank you

'''
def epics(text):

    sent=nltk.sent_tokenize(text)
    # word=nltk.word_tokenize(sent)
    epic=[]
    for str in sent:

       if 'epics' in str:
          word=nltk.word_tokenize(str)
          pos=nltk.pos_tag(word)
          pos=str.split(',')
          i=word.index('The')
          j=word.index('are')
          del word[i:j+1]
          stop=set(stopwords.words('english'))
          new_str=''
          for s in word:
              new_str+=' '+s
          l=new_str.split(',')
          str=''
          l1=[]
          for i in l:
              s = ''
              k=i.split(' ')

              del k[0]
              del k[-1]

              if k[0] in stop:
                  del k[0]
                  l=k
                  for r in l:
                      s+=' '+r
                  l1.append(s)



              else:
                  s+=i
                  l1.append(s)
          return l1









                      # if (pos[i][1] == 'DT' and pos[i + 1][1] == 'NN') :


def get_stories(text):
    tokens = nltk.tokenize.sent_tokenize(text)
    # tokens_word=nltk.word_tokenize(tokens)
    #
    # pos = nltk.pos_tag(tokens_word)
    story_epic=[]
    for str in tokens:
        if 'belongs' in str:

          story_epic.append(str)
    # return story_epic
    l = []
    for str in story_epic:
        token_word = nltk.tokenize.word_tokenize(str)
        # stop=set(stopwords.words('english'))
        # pos=[i for i in str.lower().split() if i not in stop]
        pos=nltk.pos_tag(token_word)
        # print(pos)

        # pos = nltk.pos_tag(token_word)


        for i in range(len(pos)):
            if i<len(pos)-1:
                if (pos[i][1] == 'NNS' and pos[i + 1][1] == 'NN') or (
                        pos[i][1] == 'NN' and pos[i + 1][1] == 'NNS') or (
                        pos[i][1] == 'NN' and pos[i + 1][1] == 'CC') or (
                        pos[i][1] == 'CC' and pos[i + 1][1] == 'NN'):

               # if (pos[i][1]=='NNS' and pos[i+1][1]=='NN') or (pos[i][1]=='NN' and pos[i+1][1]=='NNS') :

               # if (pos[i][1] == 'DT' and pos[i + 1][1] == 'NN') :

                  l.append((pos[i][0]+' '+pos[i+1][0]+' '+pos[i+2][0]))
    return l

#         #     next=pos[s][1]
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
#
#
#
#
# epics_list=get_stories(text)
# print(epics_list)
# new_epics=[]
# for i in epics_list:
#     if i not in new_epics:
#         new_epics.append(i)
# print(new_epics)

# print(old_epics)
# new_epics=[x.rstrip('epic') for x in get_stories(text)]
# new_epics=[x.rstrip() for x in new_epics]
# print(new_epics)

# l=[]

# for ptr in new_epics:
#     for str in old_epics:
#         if ptr==str:
#             l.append(ptr)
#         # else:
#         #     new_epics.remove(ptr)
# for i in l:
#     if i not in new_epics:
#         l.remove(i)

# print(l)
def main(text):

  old_epics=epics(text)
  old_epics=[x.strip() for x in old_epics]


  new_epic=get_stories(text)
  new_epic=[x.strip('.') for x in new_epic]

  new_epic=[x.strip('epic') for x in new_epic]
  new_epic=[x.strip() for x in new_epic]


  l1=[]
  for ptr in new_epic:
      for str in old_epics:
          if ptr==str:
              l1.append(ptr)
  return l1




print(main(text))

