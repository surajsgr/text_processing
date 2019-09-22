import nltk
from nameparser.parser import HumanName
from nltk.corpus import wordnet
import re
text='''
Hey, how are you all? Let's discuss and get started with our stories discussion. 
The epics are data science, data analytics,  research and development, and data engineering. 
We have Falcon, Chirag, Raman and Yashica as team members for this project. 
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

def get_stories(text):
    tokens = nltk.tokenize.sent_tokenize(text)
    # tokens_word=nltk.word_tokenize(tokens)
    #
    # pos = nltk.pos_tag(tokens_word)
    story=[]
    for str in tokens:
        if 'belongs' in str:

          story.append(str)

    final=[]
    for s in story:
        if 'story' in s:


         output=re.findall(r"story [0-9]+",s)
         final.extend(output)
        else:
            final.append('No story')
    return final
        # for out in output:
        #     final.append(out)
    # return set(final)

# epics_list=list(get_stories(text))
# new_list=sorted(epics_list)
# new_list=get_stories(text)
# new_list=[]
# for i in list:
#     if i not in new_list:
#         new_list.append(i)
# print(get_stories(text))











