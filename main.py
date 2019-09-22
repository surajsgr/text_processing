import nltk
from nameparser.parser import HumanName
from nltk.corpus import wordnet
import re

text = '''

Hey, how are you all? Let's discuss and get started with our stories discussion. 
The epics are data science, analytics,  Research and development, and engineering. 
We have Falcon, Chirag, Raman and Yashica as team members for this project. 
Falcon is working on story 123 for NLP key feature extraction and it belongs to the data science epic. 
how many stories point to the task you are doing Falcon? Story points for story 123 will be 5. 
Another story under data engineering is pending and its story points are 8. 
Well, this was the quick summary and total story points for this sprint is 13. 
Yashica is working on story 569 for Cloudformation and it belongs to the data engineering epic. 
how many stories point to the task you are doing Yashica? Story points for story 569 will be 3. 
Chirag is working on story 4456 for intent extraction and it belongs to the data engineering epic. 
how many stories point to the task you are doing Chirag? Story points for story 4456 will be 3
Raman will be working on story 555 some analysis during free time and it belongs to Research and development.

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

names=list(get_human_names(text[1:]))

def get_title(text):
    tokens = nltk.tokenize.sent_tokenize(text)
    # tokens_word=nltk.word_tokenize(tokens)
    #
    # pos = nltk.pos_tag(tokens_word)
    story=[]
    for str in tokens:
        if 'story' in str:

          story.append(str)

    l = []
    for str in story:
        token_word = nltk.tokenize.word_tokenize(str)
        pos = nltk.pos_tag(token_word)
        for i,j in pos:
            if j=='NNP':
                l.append(i)
    return l

names_new=get_title(text)

for i in names_new:
    if i not in names:
        names_new.remove(i)



def get_stories(text):
    tokens = nltk.tokenize.sent_tokenize(text)
    # tokens_word=nltk.word_tokenize(tokens)
    #
    # pos = nltk.pos_tag(tokens_word)
    story=[]
    for str in tokens:
        if 'story' in str:

          story.append(str)
    final=[]
    for s in story:

        output=re.findall(r"story [0-9]+",s)
        final.extend(output)
    return final
        # for out in output:
        #     final.append(out)
    # return set(final)

# epics_list=list(get_stories(text))
# new_list=sorted(epics_list)
list=get_stories(text)
stories_list=[]
for i in list:
    if i not in stories_list:
        stories_list.append(i)




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


epics_list=get_stories(text)


def get_title(text):
    tokens = nltk.tokenize.sent_tokenize(text)

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


title=get_title(text)
# print(title)

# final=zip(names_new,epics_list)
#
# for i,j in final:
#     print(i,j)




final=zip(names_new,stories_list,title,epics_list)

result = []
for i,j,k,l in final:
    data = {"name":i, "story":j, "title": k, "epic": l}
    result.append(data)
print(result)
