import random
import os

def createNameDict(questionList):
    playerNames = open("name.txt", 'r')
    nameDictionary = open('togive.txt', 'w')

    nameDict = {}
    questionNumbers = {}
    for name in playerNames:
        name = name.strip()
        #Sometiemes 4 or 5 numbers generated in dictionary
        nameDict[name] = {random.randint(0,len(questionList)-1) for i in range(5)}

    for key, value in nameDict.items():
        print("{} {}".format(key,sorted(value)), file=nameDictionary)

    playerNames.close()
    nameDictionary.close()

    return nameDict

def questionToList():

    questionsFile = open('QsandOpts.txt', 'r')
    questionList = []
    question = ()

    count = 1
    for line in questionsFile:
        question += (line.strip(),)
        count += 1
        if(count == 4):
            count = 1
            questionList.append(question)
            question = ()

    return questionList

#Errors
#ValueError
def questionDisplay(num, questionList):
    print("\n{}. {}".format(num+1,questionList[num][0]))

    answersChoices = list(questionList[num][1].split("_"))

    for i in range(0,len(answersChoices)):
        print("\t{}. {}".format(i+1,answersChoices[i]))

    answer = int(questionList[num][2])
    while(True):
        user_ans = int(input("What is your answer?:"))
        if not(user_ans in range(0,len(answersChoices)+1)):
            print("Invlad input. Please try again.")
            continue
        if user_ans == answer:
            return 1
            break
        else:
            return 0
            break


def menu(nameList, questionList):

    print("Welcom the quiz spreparation program.")
    while(True):
        name = input("\nPlease input the name of a student who should take a practice quiz (enter EXIT to end the program): ")
        if name in nameList.keys():
            print("Hi " + name + ". Here are your questions")
            questionNumbers = nameList[name]
            right_ans = 0
            for i in questionNumbers:
                right_ans += questionDisplay(i, questionList)
            print("\nYou scored {}/5 - good job".format(right_ans))

            input("\nPress Enter to continue...")

            os.system('cls' if os.name == 'nt' else 'clear')


        elif name == "EXIT":
            print("Bye.")
            break
        else:
            print("This name is not in our databases. Please try again")

questions = questionToList()
NameDict= createNameDict(questions)
#print(NameDict)
menu(NameDict, questions)
