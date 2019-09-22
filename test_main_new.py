import rename
import stories_num
import stories_new
import new_title
from main_new import results
import pytest

text1='''
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
text2='''
Hey, how are you all? Let's discuss and get started with our stories discussion. 
The epics are data science, data analytics,  research and development, and data engineering. 
We have Falcon, Chirag, Raman and Yashica,Samark,George,John as team members for this project. 
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
John will be working on other tasks and it belongs to data engineering.



we will connect after a short coffee break. Thank you



'''

@pytest.mark.parametrize("test_input,test_output",

                          [
                              (text1,['Falcon', 'Yashica', 'Chirag', 'Raman', 'Suraj', 'Samark', 'George']),
                              (text2,['Falcon', 'Yashica', 'Chirag', 'Raman', 'Suraj', 'Samark', 'George'])

                          ]
                          )
def test_rename(test_input,test_output):
    name=rename.main(test_input)
    assert name == test_output




