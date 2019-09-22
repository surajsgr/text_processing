import nltk
from  nltk.text import ConcordanceIndex

text='''

Hey, how are you all? Let's discuss and get started with our stories discussion. The epics are data science, analytics, and engineering. We have Falcon, Chirag, and Yashica as team members for this project. Falcon is working on story 123 for NLP key feature extraction and it belongs to the data science epic. how many stories point to the task you are doing Falcon? Story points for story 123 will be 5. Another story under data engineering is pending and its story points are 8. Well, this was the quick summary and total story points for this sprint is 13. Yashica is working on story 569 for Cloudformation and it belongs to the data engineering epic. how many stories point to the task you are doing Yashica? Story points for story 569 will be 3. Chirag is working on story 4456 for intent extraction and it belongs to the data engineering epic. how many stories point to the task you are doing Chirag? Story points for story 4456 will be 3

'''




tokens=nltk.tokenize.word_tokenize(text)
raw_text=nltk.Text(tokens)

result=raw_text.concordance('data',width=90,lines=3)
l=[]

print(result)
# try:
#
#     for i in final:
#
#         l.append(i)
#     print(l)
#
#
#
# except:
#     print('')
