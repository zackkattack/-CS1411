#Name:Zachary Carson
#Course:CS 1411
#Date:04/13/17
#
#
#Problem:
#Create a Python program to read in a file (Qsand0pts.txt) of quiz questions and
#answers into a list.  Each question set is stored inside the file using 3 lines.
#The first line contains the questions itself.
#The second line contains the choices for the question. The choices are separated
#by two characters, a dot and underscore; each question may have a different
#number of choices. The choices should be displayed with the number associated
#with them, starting with number one.
#The third line contains the number of the correct choice.
#Each question set should be stored as a tuple in the list.
#Display all of the question sets to the screen in the following format:
#1.  Question
#1) First option
#2) Second option
#3) Third option

#2.  Question
#1) First option
#2) Second option
#3) Third option
#Read in a file of names (names.txt).  As you read each name, choose 5 unique
#and random questions from the questions file.  Store the questions in a set.
#Enter the name into a dictionary where the name is the key and the set of
#questions is the value.  Print the names and questions neatly to the
#screen where the questions are in ascending order.
#
#		Judy		Questions 3, 8, 15, 17, 22
#		Marta		Questions 1, 2, 3, 4, 5
#		Martin		Questions 17, 20, 21, 23, 28
#		…
#
#Save the dictionary to a file called ‘togive.txt’.
#Each name and question set should be stored on one line in the file.
#Create a Python program to read in the ‘Qsand0pts.txt’ file into a list and to
# read in the ‘togive.txt’ file into a dictionary as given in the
# “Lab Preparation” Section.  Allow the user to select a name and then give the
# associated quiz using the questions in the question set stored in the
# dictionary.  Show the user his/her score at the end of the quiz.  Allow the user
# to select as many names as desired and give the quiz for each name.
# In the sample run below, Judy is given questions 3, 8, 15, 17, and 22 in order
# from the questions file, but the questions are numbered from 1 to 5.
#
# Welcome to the quiz preparation program.
#
# Please input the name of a student who should take a practice quiz (enter EXIT
# to end the program):  Judy
# Hi Judy.  Here are your questions.
#
# 1.  Question
# 1. First option
# 2. Second option
# 3. Third option
# What is your answer? 1
#
# 2.  Question
# 1. First option
# 2. Second option
# 3. Third option
# What is your answer? 2
# …
# You scored 3/5 – good job
#
# Please input the name of a student who should take a practice quiz (enter EXIT
# to end the program):  EXIT
# Bye.
# For your program, do not use global variables except for DEBUG, validate
# all input, perform exception handling, and use at least 4 functions
# (each function should have its purpose immediately above the function).
#
#Given:
#
#
#
#Analysis
#Input: togive.txt, name.txt, QsandOpts.txt
#Outputs: 5 quiz questions
#
#
#Method/Algorithm:
#createNameDict(questionList):
#
#Step 1:playerNames = open("name.txt", 'r')
#Step 2:nameDictionary = open('togive.txt', 'w')
#Step 3:nameDict = {}
#Step 4:for name in playerNames:
#Step 5:    questionNumbers = {}
#Step 6:    name = name.strip()
#Step 7:    questionNumbers = {random.randint(0,len(questionList)-1) for i in range(5)}
#Step 8:    if(lne(questionList) != 5): goto 7
#Step 9:    nameDict[name]=questionList
#Step 10:for key,value in nameDict.items():
#Step 11:print keys questions values, file = nameDictionary
#Step 12:playerNames.close()
#Step 13:nameDictionary.close()
#
#questionToList()
#Step 1:questionToList = []
#Step 2:question = ()
#Step 3:count = 1
#Step 4:questionsFile = open('questionsFile.txt', 'r')
#Step 5:for lines in questionsFile
#Step 6:    question +=(line.strip(),)
#Step 7:    count += 1
#Step 8:    if count == 4: count=1, questionList.append(question)
#Step 9:    question=()
#Step 10:return questionList
#
#questionDisplay(num, questionList)
#Step 1:print("\n{}. {}".format(num+1,questionList[num][0]))
#Step 2:answersChoices = list(questionList[num][1].split("_"))
#Step 3:i = 0
#Step 4:print("\t{}. {}".format(i+1,answersChoices[i]))
#Step 5:if i < lne(answersChoices): goto 4
#Step 6:try:
#Step 7:    user_ans = int(input("What is your answer?:"))
#Step 8:    if not(user_ans in range(0,len(answersChoices)+1)): print("Invlad input. Please try again."), continue
#Step 9:    if user_ans == answer: return 1, break
#Step 10:    else: retrun 0, break
#Step 11:except ValueError:
#Step 12:    print("Invlad input. Please try again.")
#Step 13:if True: goto 6
#
#menu(questionList):
#Step 1:togive = open('togive.txt', 'r')
#Step 2:nameList = {}
#Step 3:for line in togive:
#Step 4:    line = line.split()
#Step 5:    nameList[line[0]]= [int(line[i]) for i in range(2, 7)]
#Step 6:print("Welcom the quiz spreparation program.")
#Step 7:name = input("\nPlease input the name of a student who should take a practice quiz (enter EXIT to end the program): ")
#Step 8:if name in nameList.keys():
#Step 9:    print("Hi " + name + ". Here are your questions")
#Step 10:   questionNumbers = nameList[name]
#Step 11:   right_ans = 0
#Step 12:   for i in questionNumbers:
#Step 13:       right_ans += questionDisplay(i, questionList)
#Step 14:   if right_ans >=3: response = "good job"
#Step 15:   elif right_ans <3: response = "study harder"
#Step 16:   print("\nYou scored {}/5 - {}".format(right_ans, response))
#Step 17:   input("\nPress Enter to continue...")
#Step 18:   os.system('cls' if os.name == 'nt' else 'clear')
#Step 19:elif name == "EXIT": print('Bye.'), break
#Step 20:else: print("This name is not in our databases. Please try again")
#Step 21:if true: goto 6
#
#Step 1:questions = questionToList()
#Step 2:createNameDict(questions)
#Step 3:menu(questions)
#
#
#
#TestCases:
#Input:EXIT
#Expected OutPut: Bye.
#
#Input:Zachary,1,2,3,2,1
#Expected Output:1/5 - Better luck next time.
#Write a comment about passing Testing results
#Sucessful
#Program:

import random
import os

#Creates a file with the names of students and there assigned questions
def createNameDict(questionList):
    playerNames = open("name.txt", 'r')
    nameDictionary = open('togive.txt', 'w')

    nameDict = {}# stores the names and questioins values

    #reads through the list of names and assigns names with 5 random questions
    for name in playerNames:
        questionNumbers = {}
        name = name.strip()

        #makes a random list of 5 numbers
        while(len(questionNumbers) != 5):
            questionNumbers = {random.randint(0,len(questionList)-1) for i in range(5)}

        nameDict[name] = questionNumbers

    #prints name dictionary and questions to a file
    for key, value in nameDict.items():
        print("{} Question ".format(key),end='', file=nameDictionary)
        for num in value:
            print(num, " ", end='', file=nameDictionary)
        print('', file=nameDictionary)

    playerNames.close()
    nameDictionary.close()

#Concerts lines QsandOpts.txt into a managable list
def questionToList():

    questionsFile = open('QsandOpts.txt', 'r')
    questionList = []#List of the tuples
    question = ()#questions tuple that holds a queston's questions,
                #answer choices, and answers

    #strips questions and their atributes from file and puts them in a tuple
    count = 1
    for line in questionsFile:
        question += (line.strip(),)
        count += 1
        if(count == 4):
            count = 1
            questionList.append(question)
            question = ()

    return questionList

#Question Object: manages logic for one question, returns 1 if right and 0 if wrong
def questionDisplay(num, questionList):
    #prints out the question and answer choices
    print("\n{}. {}".format(num+1,questionList[num][0]))

    answersChoices = list(questionList[num][1].split("_"))

    for i in range(0,len(answersChoices)):
        print("\t{}. {}".format(i+1,answersChoices[i]))

    answer = int(questionList[num][2])

    #checks if answer is right, wrong, or invalid
    while(True):#keeps checking untill it gets a valid input
        try:
            user_ans = int(input("What is your answer?:"))
            if not(user_ans in range(0,len(answersChoices)+1)):
                print("Invlad input. Please try again.")
                continue
            if user_ans == answer:
                return 1# if right, it will return a 1
                break
            else:
                return 0 # if wrong, it will return a 0
                break
        except ValueError:#If plyers does not enter a integer
            print("Invlad input. Please try again.")

#Main menu that manages the game logic
def menu(questionList):
    togive = open('togive.txt', 'r')
    nameList = {} # dictionary of names and theri question numbers

    #converts togive.txt into a Dictionary
    for line in togive:

    	line = line.split()

    	nameList[line[0]]= [int(line[i]) for i in range(2, 7)]


    while(True):
        print("Welcom the quiz spreparation program.")
        name = input("\nPlease input the name of a student who should take a practice quiz (enter EXIT to end the program): ")
        if name in nameList.keys():#checks if the name is in the dictionary list
            print("Hi " + name + ". Here are your questions")
            questionNumbers = nameList[name]
            right_ans = 0
            for i in questionNumbers:#Adds up how many asers the player got right and prints it when they are done
                right_ans += questionDisplay(i, questionList)

            if right_ans >=3:#If they get more then 3 right
                response = "good job"
            elif right_ans <3:#if they get more than 3 wrong
                response = "study harder"

            print("\nYou scored {}/5 - {}".format(right_ans, response))

            input("\nPress Enter to continue...")# pause fro unser input

            os.system('cls' if os.name == 'nt' else 'clear')#clear screen


        elif name == "EXIT":
            print("Bye.")
            break
        else:
            print("This name is not in our databases. Please try again")

questions = questionToList()# make questions list
createNameDict(questions)#  make togive.txt file
menu(questions)# Start menu
