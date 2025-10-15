import qcm
import string
import random as rd
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

#Pseudo random number generator
def PRNG(intervall):
    intervall_list=[x for x in range(0,intervall)]
    number=rd.choice(intervall_list)
    return number

uppercase_alpha=string.ascii_uppercase
letter_to_number={}
number_to_letter={}
for i,j in zip(uppercase_alpha,[x for x in range(10)]):
    letter_to_number[i]=str(j)
    number_to_letter[str(j)]=i
translate_number_to_letter=str.maketrans(number_to_letter)
translate_letter_to_number=str.maketrans(letter_to_number)

def QCM(questions: list):
    right_answers=0
    wrong_answers=0
    over=len(questions)

    #Choisir le mode de cotation
    while True:
        print("Choisissez votre mode de cotation : \nA: Légère : +1 pour les bonnes réponses ,0 pour les mauvaises \nB: sévère : +1 pour les bonnes réponses ,-1 pour les mauvaises")
        quoting = input("Choisisez A ou B : ").lower()
        if quoting in ["a","b"]:
            quoting_value=True if quoting == "a" else False
            break
        else:
            print("S'il vous plait choisissez A ou B")

    #Choisir le mode de presentation
    while True:
            print("Choisissez votre mode de présentation :\nA: Evaluation : un seul résultat pour un mode de résultat choisis\nB: Comparatif: résultats pour les 2 modes de cotation  " )
            presentation=input("Choisissez A ou B : ").lower()
            if presentation in ["a","b"]:
                presentation_value=True if presentation == "a"else False
                break
            else:
                print("S'il vous plait choisissez A ou B")

    for i in range(len(questions)):
        question_num = PRNG(len(questions))# donne un nombre aléatoire dans un intervall question
        question = questions[question_num]
        answers=question[1]
        random_answers=[]
        while answers:
            answer_num=PRNG(len(answers))
            ans=answers[answer_num]
            answers.remove(ans)
            random_answers.append(ans)

        answer_list={}
        tried=True

        while tried:
            try:
                letters=[]
                print(f"Q:{question[0]}")  # imprime la question
                #Affiche les options de réponse
                for y in range(len(random_answers)):
                    answer_list[y]=random_answers[y][1]
                    i=str(y).translate(translate_number_to_letter)#Transforme un nombre en sa lettre adjacent
                    print(f"{i} : {random_answers[y][0]}")
                    letters.append(i)



                answer = input(f"answer : ").upper()
                answer =list(answer)

                for t in answer:
                    if t in[' ',"," ]:
                        answer.remove(t)

                answer_to_number=[]
                #Transforme toute les lettres en leur nombre adjacent
                for letter in answer:#
                    z=letter.translate(translate_letter_to_number)
                    answer_to_number.append(int(z))


                Good_answers={}
                Bad_answers={}

                for i in range(len(answer_list)):
                    if answer_list[i] :
                        Good_answers[i] = answer_list[i]
                    else:
                        Bad_answers[i] = answer_list[i]

                for answer in answer_to_number:
                    if answer not in list(Good_answers.keys()) + list(Bad_answers.keys()):
                        print("S'il vous plaît, choisissez une des lettres affichées")
                        break
                    else:

                        if all(ans in list(Good_answers.keys()) for ans in answer_to_number):
                            print("\nBonne réponse :)\n")
                            tried=False
                            right_answers += 1
                            questions.remove(questions[question_num])
                            break
                        elif any(ans in list(Bad_answers.keys()) for ans in answer_to_number):
                            print("\nMauvaise réponse :(\n")
                            tried = False
                            wrong_answers += 1
                            questions.remove(questions[question_num])
                            break

            except ValueError:
                print("S'il vous plait choisiser une des lettre afficher")

    light_quoting=f"{right_answers}/{over}"
    severe_quoting=f"{right_answers-wrong_answers}/{over}"

    if presentation_value:#Evaluation
        if quoting_value:
            print("Résultat leger: "+light_quoting)
        else:
            print("Résultat severe: "+severe_quoting)
    else:#comparatif
        print(f"Résultat leger: {light_quoting}  \t Résultat severe: {severe_quoting}")

print(questions_1)