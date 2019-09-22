import nltk
from  nltk.text import ConcordanceIndex

text='''

Hey, how are you all? Let's discuss and get started with our stories discussion. The epics are data science, analytics, and engineering. We have Falcon, Chirag, and Yashica as team members for this project. Falcon is working on story 123 for NLP key feature extraction and it belongs to the data science epic. how many stories point to the task you are doing Falcon? Story points for story 123 will be 5. Another story under data engineering is pending and its story points are 8. Well, this was the quick summary and total story points for this sprint is 13. Yashica is working on story 569 for Cloudformation and it belongs to the data engineering epic. how many stories point to the task you are doing Yashica? Story points for story 569 will be 3. Chirag is working on story 4456 for intent extraction and it belongs to the data engineering epic. how many stories point to the task you are doing Chirag? Story points for story 4456 will be 3

'''

def get_stories(text):
    tokens = nltk.tokenize.sent_tokenize(text)
    # tokens_word=nltk.word_tokenize(tokens)
    #
    # pos = nltk.pos_tag(tokens_word)
    story_epic=[]
    for str in tokens:
        if 'epic' and 'belongs' in str:

          story_epic.append(str)

    l = []
    for str in story_epic:
        token_word = nltk.tokenize.word_tokenize(str)
        pos = nltk.pos_tag(token_word)
        d={}

        for i,j in pos:

            if j=='NNS' or j=='NN':
               final=pos


        s=0
        running=True

        for i in range(len(final)):
            if i<len(final)-1:
                if (final[i][1]=='NNS' and final[i+1][1]=='NN') or (final[i][1]=='NN' and final[i+1][1]=='NNS'):
                    l.append((final[i][0]+' '+final[i+1][0]))
    for word in l:
        if 'data' not in word:
            l.remove(word)
    return l

                    #



        # while s<len(final)+1:
        #     new_list=final[s][1]
        #     s=(s+1)%len(final)
        #     next=final[s][1]
        #     print(new_list,next)
        #     s=s+1







                    # s += 1
                    # if l[s][1] == 'NN':
                    #     print(l[s])











epics_list=print(get_stories(text))
# new_epics=[]
# for i in epics_list:
#     if i not in new_epics:
#         new_epics.append(i)
# print(new_epics)