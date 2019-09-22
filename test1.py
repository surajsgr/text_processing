# from nltk.corpus import wordnet
#
#
# for syn in wordnet.synsets('belongs'):
#     for s in syn.lemmas():
#         if s.antonyms():
#
#           k=s.antonyms()[0].name()
#           for i in k:
#               print(i)

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
final=text.collocations()
print(final)