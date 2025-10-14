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
    right_answers=0
    wrong_answers=0
    over=len(questions)


    while True:
        print("Choisissez votre mode de cotation : \nA: Légère : +1 pour les bonnes réponses ,0 pour les mauvaises \nB: sévère : +1 pour les bonnes réponses ,-1 pour les mauvaises")
        quoting=input("Choisisez A ou B : ").lower()
        if quoting in ["a","b"]:
            quoting_value=True if quoting == "a" else False
            break
        else:
            print("S'il vous plait choisissez A ou B")
    print("Choisissez votre mode de présentation :\nA: Evaluation : un seul résultat pour un mode de résultat choisis\nB: Comparatif: résultats pour les 2 modes de cotation  " )
    presentation=input("Choisissez A ou B : ").lower()
    if presentation in ["a","b"]:
        presentation_value=True if presentation == "a"else False

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
        tried=True
        while tried:
            try:
                for y in range(len(random_answers)):
                    answer_list[y]=random_answers[y][1]
                    i=str(y).translate(translate_number_to_letter)
                    print(f"{i} : {random_answers[y][0]}")


                answer = input(f"answer : ").upper()
                answer =list(answer)
                for t in answer:
                    if t == ' ':
                        answer.remove(t)

                answer_to_number=[]
                for u in answer:
                    z=u.translate(translate_letter_to_number)
                    answer_to_number.append(int(z))


                Good_answers={}
                Bad_answers={}
                for i in range(len(answer_list)):
                    if answer_list[i] :
                        Good_answers[i] = answer_list[i]
                    else:
                        Bad_answers[i] = answer_list[i]

                if answer_to_number == list(Good_answers.keys()):
                        print("right answer\n")
                        tried=False
                        right_answers+=1
                else:
                        print("wrong answer\n")
                        tried=False
                        wrong_answers+=1

                questions.remove(questions[question_num])
            except ValueError:
                pass
    light_quoting=f"{right_answers}/{over}"
    severe_quoting=f"{right_answers-wrong_answers}/{over}"

    if presentation_value:#Evaluation
        if quoting_value:
            print("Résultat leger: "+light_quoting)
        else:
            print("Résultat severe: "+severe_quoting)
    else:#comparatif
        print(f"Résultat leger: {light_quoting}  \t Résultat severe: {severe_quoting}")





QCM(full_question)





