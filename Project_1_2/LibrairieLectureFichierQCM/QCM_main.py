from qcm import build_questionnaire
import string
import random as rd

#Put the questions together

#
def add_questions_together(q1,q2):
    return q1+q2

#Pseudo random number generator
def PRNG(intervall:int):
    intervall_list=[x for x in range(0,intervall)]# liste des interval
    number=rd.choice(intervall_list)
    return number

def translater():

    uppercase_alpha=string.ascii_uppercase
    letter_to_number={}
    number_to_letter={}
    for i,j in zip(uppercase_alpha,[x for x in range(10)]):
        letter_to_number[i]=str(j)
        number_to_letter[str(j)]=i
    translate_number_to_letter = str.maketrans(number_to_letter)  # Traduit un nombre de entre 0 et 9 en sa lettre équivalent
    translate_letter_to_number = str.maketrans(letter_to_number)  # Traduit une lettre en son nombre équivalent

    return translate_number_to_letter,translate_letter_to_number



def QCM(questions: list):
    translate_number_to_letter=translater()[0]
    translate_letter_to_number=translater()[1]
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

    #boucle sur toute les questions
    for i in range(len(questions)):
        question_num = PRNG(len(questions))# donne un nombre aléatoire dans un intervall question
        question = questions[question_num]#Prend une question de la liste
        answers=question[1]#Prend tout les réponses a la question
        random_answers=[]
        while answers:#Tounre jusqu'a answers est vide
            answer_num=PRNG(len(answers))
            ans=answers[answer_num]
            answers.remove(ans)#enleve une réponse dans la liste
            random_answers.append(ans)#Met les question de maniere aleatoire dans la liste grace au PRNG

        answer_list={}
        tried=True
        while tried:
            try:
                letters=[]
                print(f"Q:{question[0]}")  # imprime la question
                #Affiche les options de réponse
                for y in range(len(random_answers)):
                    answer_list[y]=random_answers[y][1]#Ajoute le nombre + bool
                    i=str(y).translate(translate_number_to_letter)#Transforme un nombre en sa lettre adjacent
                    print(f"{i} : {random_answers[y][0]}")
                    letters.append(i)

                answer = input(f"answer : ").upper()
                answer =list(answer)
                #Enlever les choses inutiles dans answer
                for t in answer:
                    if t in[' ',"," ]:
                        answer.remove(t)

                answer_to_number=[]
                #Transforme toute les lettres en leur nombre adjacent
                for letter in answer:
                    z=letter.translate(translate_letter_to_number)
                    answer_to_number.append(int(z))#Tout les réponse en nombre


                Good_answers={}
                Bad_answers={}
                #Trie les bonne et mauvaise réponse
                for i in range(len(answer_list)):
                    if answer_list[i] :#Verifie si la reponse est bonne
                        Good_answers[i] = answer_list[i]#Ajoute l'index plus la valeur boolean Vrai

                    else:
                        Bad_answers[i] = answer_list[i]#Ajoute l'index plus la valeur boolean Fausse


                for answer in answer_to_number:
                    #Verifie que la réponse est bien dans les bonne réponse et mauvaise réponse
                    if answer not in list(Good_answers.keys()) + list(Bad_answers.keys()):
                        print("S'il vous plaît, choisissez une des lettres affichées")
                        break
                    else:
                        #Verifie que toute les bonne réponse sont la
                        if all(ans in list(Good_answers.keys()) for ans in answer_to_number):
                            print("\nBonne réponse :)\n")
                            tried=False
                            right_answers += 1
                            questions.remove(questions[question_num])
                            break

                        #Verifie si il y aune mauvaise réponse
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



filename = "QCM.txt"
filename_2="QCM2.txt"

question_1=build_questionnaire(filename)
question_2=build_questionnaire(filename_2)

full_question=add_questions_together(question_1,question_2)
QCM(full_question)