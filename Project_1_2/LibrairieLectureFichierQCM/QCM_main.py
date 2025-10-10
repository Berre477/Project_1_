import qcm
filename = "QCM.txt"
filename_2="QCM2.txt"
questions_1 = qcm.build_questionnaire(filename)
questions_2=qcm.build_questionnaire(filename_2)
import pandas as pd
#Put the questions together
full_question=[]
for x in questions_1:
    full_question.append(x)
for y in questions_2:
    full_question.append(y)
a=pd.DataFrame(full_question,[x for x in range(1,9)])
print(a)
