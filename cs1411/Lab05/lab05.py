#Name:Zachary Carson
#Course:CS 1411
#Date:3/4/2017
#Write a python program that
#a) takes a message, encrypts the message as described above and returns the cipher
#text.
#b) that takes a cipher text, decrypts the cipher text as described above and
#returns the message.
#
#Problem:
#Make a program the encrypts and decrypts inputed messages.
#Given:
#encrytpion scheme
#input: “Fight, Matadors, for Tech!“
#output: “ih,Mtdr,frTc!Fgt aaos o eh
#
#Analysis
#Input:A String
#Outputs: A manipulated virsion of the string the decrypts the inputed text or
# a reversal of the decrypted text to readable text.
#
#Method/Algorithm:
#modual encrypt(String s):
#Step 1: even_char = s[0,len(s):2]
#Step 2: odd_char = s[1,len(s):2]
#Step 3: print ("Encrypted message: {}{}".format(even_char,odd_char)
#
#modual dycript(String s):
#Step 1: midpoint = int(len(s)/2)
#Step 2: output = ''
#Step 3: left_Half = s[0, midpoint]
#Step 4: right_Half = s[midpoint:len(s)]
#Step 5: i = 0
#Step 6: output += right_Half[i]+left_Half[i]
#Step 7: if len(s)%2==1 and i == midpoint-1: output += right_Half[-1]
#Step 8: i +=1
#Step 9: if i < midpoint: goto 6
#Step 10: print("\nDecrypted Message: ", output,"\n")
#
#modual Menu:
#Step 1: print "1. Encode Message."
#Step 2: print "2. Decode Message."
#Step 3: print "3. Quit."
#Step 4: if menu == 1: goto modual encrypt
#Step 5: if menu == 1: goto modual decrypt
#Step 6: if menu == 1: break
#Step 7: if True: goto 1
#
#Step 1: menu()
#
#
#TestCases:
#Input:Fight, Matadors, for Tech!
#Expected OutPut:
#encrypt:ih,Mtdr,frTc!Fgt aaos o eh
#decrypt:Fight, Matadors, for Tech!
#
#Input:Fearless champions ever be.
#Expected Output:
#encrypt:erescaposee eFals hmin vrb.
#Decrypt:Fearless champions ever be.
#Write a comment about passing Testing results
#
#Program:

def encrypt(s):

    even_char = s[0:len(s):2]
    odd_char = s[1:len(s):2]
    print ("\nEncrypted message: {}{}\n".format(odd_char,even_char))

def decrypt(s):

    midpoint = 0
    output = ""

    midpoint = int((len(s)/2))

    left_Half = s[0:midpoint]
    right_Half = s[midpoint:len(s)]

    for i in range(0,midpoint):
        output += right_Half[i]+left_Half[i]
        if len(s)%2==1 and i == midpoint-1:
            output += right_Half[-1]
    print("\nDecrypted Message: ", output,"\n")

def menu():

    while True:

        print("1. Encode message.")
        print("2. Decode message.")
        print("3. Quit.")
        menu = input("\nEnter the number of the operatuon you would like to preform: ")

        if menu == '1':
            string = input("Enter the string you want to convert: ")
            encrypt(string)
        if menu == '2':
            string = input("Enter the string you want to convert: ")
            decrypt(string)
        if menu == '3':
            break

menu()
