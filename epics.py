import nltk
from nameparser.parser import HumanName
from nltk.corpus import wordnet


text='''

Hey, how are you all? Let's discuss and get started with our stories discussion. The epics are data science, analytics, and engineering. We have Falcon, Chirag, and Yashica as team members for this project. Falcon is working on story 123 for NLP key feature extraction and it belongs to the data science epic. how many stories point to the task you are doing Falcon? Story points for story 123 will be 5. Another story under data engineering is pending and its story points are 8. Well, this was the quick summary and total story points for this sprint is 13. Yashica is working on story 569 for Cloudformation and it belongs to the data engineering epic. how many stories point to the task you are doing Yashica? Story points for story 569 will be 3. Chirag is working on story 4456 for intent extraction and it belongs to the data engineering epic. how many stories point to the task you are doing Chirag? Story points for story 4456 will be 3





'''

def get_stories(text):
    tokens = nltk.tokenize.sent_tokenize(text)
    # tokens_word=nltk.word_tokenize(tokens)
    #
    # pos = nltk.pos_tag(tokens_word)
    for str in tokens:
        if 'epics' in str:
            sent=str

    token_word=nltk.tokenize.word_tokenize(word)
    pos=nltk.pos_tag(token_word)
    sentt = nltk.ne_chunk(pos, binary=False)
    # return pos
    epic=[]
    str=''
    for i,j in pos:
        if j=='NNS' or j=='NN':

          epic.append(i)
    for i in epic:
        if i=='epics':

          epic.remove(i)
    return epic

    # for subtree in sentt.subtrees(filter=lambda t: t.label() == 'NNS' or t.label() == 'NN'):
    #     return subtree
    #     # for leaf in subtree.leaves():
    #     #     epic.append(leaf[0])
    #     #
    #     #     return epic




print(get_stories(text))