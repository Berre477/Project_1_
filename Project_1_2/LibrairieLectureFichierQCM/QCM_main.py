import qcm
filename = "QCM.txt"
filename_2="QCM2.txt"
questions_1 = qcm.build_questionnaire(filename)
questions_2=qcm.build_questionnaire(filename_2)

#Put the questions together
full_question=[]
for x in questions_1:
    full_question.append(x)
for y in questions_2:
    full_question.append(y)

def get_question(lst:list,index):
    return lst[index]
#Pseudo random number generator
import random as rd
def PRNG(intervall):
    intervall_list=[x for x in range(0,intervall)]
    number=rd.choice(intervall_list)
    return number

translate_number_to_letter={"0":"A","1":"B","2":"C","3":"D","4":"E"}
translate_number_to_letter=str.maketrans(translate_number_to_letter)

translate_letter_to_number={"A":"0","B":"1","C":"2","D":"3","E":"4"}
translate_letter_to_number=str.maketrans(translate_letter_to_number)

def QCM(questions: list):
    Grade=0
    over=len(questions)


    for i in range(len(questions)):
        question_num = PRNG(len(questions))
        question = questions[question_num]
        answers=question[1]
        random_answers=[]
        while answers:
            answer_num=PRNG(len(answers))
            ans=answers[answer_num]
            answers.remove(ans)
            random_answers.append(ans)

        answer_list={}

        print(f"Q:{question[0]}")
        letter_list=[]
        tried=True
        while tried:
            try:
                for y in range(len(random_answers)):
                    answer_list[y]=random_answers[y][1]
                    i=str(y).translate(translate_number_to_letter)
                    print(f"{i} : {random_answers[y][0]}")


                answer = input(f"answer : ").upper()
                answer=int(answer.translate(translate_letter_to_number))


                if answer_list[answer]:
                        print("right answer\n")
                        tried=False
                        Grade+=1
                else:
                        print("wrong answer\n")
                        tried=False

                questions.remove(questions[question_num])
            except ValueError:
                pass
    print(f"{Grade}/{over}")

QCM(full_question)





