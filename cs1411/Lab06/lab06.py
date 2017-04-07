#Name:Zachary Carson
#Course:CS 1411
#Date:3-12-16
#
#
#Problem:
#Write a program to read the encrypted file, to decrypt one line at a time, and
#write each decrypted line into another file.  Allow the user to specify the input
#filename and output filename.  Use exception handling to check for file
#existence on the input file and to determine if the output file exists so you
#can ask the user if the output file should be overwritten or not.  Prompt for
#another output filename if the user does not want the file overwritten or if the
#output filename is the same as the input filename.
#
#Given:
#Encrypted key
#
#
#Analysis
#Input:in file, out file
#Outputs:Decrypted message
#
#
#Method/Algorithm:
#Step 1:Start
#modual substitutionDecrypt(encryptLine, encryptionKey)
#Step 2:bad_chars = string.whitespace+string.punctuation
#Step 3:decryptLine = ""
#Step 4:location = 0
#Step 5:char = ''
#Step 6:i = ''
#Step 7:if char == i: if ord(i) == 9: break
#Step 8:decryptLine +=i
#Step 9:if i <= bad_chars: goto 7
#Step 10:j = ''
#Step 11:if cahr == j: location = EncryptionKey.find(j)
#Step 12:if location !=26: decryptLine +=chr(ord('a')+location), break
#Step 13:if j <=char: goto 11
#Dtep 14: k = ''
#Step 15:if cahr == k: location = EncryptionKey.upper().find(j)
#Step 16:if location !=26: decryptLine +=chr(ord('A')+location), break
#Step 17:if k <=char: goto 15
#Step 18: return decryptLine
#modual menu
#Step 19:Get in_file
#Step 20:imput_message = open(in_file, r)
#Step 21:except IOError: print this file doesnt exist
#Step 22:if True: goto 19
#Step 23:get out_file
#Step 24output = (out_file, w);
#Step 25:if out_file == in_file: print this is your inout file, contunue
#Step 26:if (os.path.exists("./"+out_file)):
#Step 27:get overwrite
#Step 28:if overwrite == yes: output = open(out_file, w)
#Step 29:if overwrite == no:continue
#Step 30:else: continue
#Step 31:output =open(out_file, w)
#Step 32:break
#Step 33:if out_file == in_fileor state: goto 23
#Step 34:except IOError: output = open(out_file, w)
#Step 35:Encryptedkey = open('EncryptionKey.txt', 'r')
#Step 36:key_list = Encryptedkey.readlines()
#Step 37:key = ""
#Step 38:i = 0
#Step 39:key += i
#Step 40:if i < key_list: goto 43
#Step 41:print(substitutionDecrypt(line_str,key), end ="", file = output)
#Step 42:if line_str < input_message: goto 45
#Step 43:menu()
#
#
#
#TestCases:
#Input:Encrypted.txt, out.txt
#Expected OutPut:
#N/A
#
#Input:ENcrypted.txt,Encrypted.txt, out.txt, no, Encrypted.txt, Decrypted.txt
#Expected Output:N/A
#Write a comment about passing Testing results
#Both files worked fine. the error hadling catches all of misinputted informaion.
#Program:

import string
import os

def substitutionDecrypt(encryptLine, encryptionKey):
    bad_chars = string.whitespace+string.punctuation# List of characters to ignore
    decryptLine = ""# The String that has been put through the decryption
    location = 0
    for char in encryptLine:#Searchers through each charater in the line
        for i in bad_chars:#Checks if char is one of these bad characters
            if char == i:
                if ord(i) == 9:# if it is a tab it will break out of the loop
                    break
                decryptLine += i#If its anything else it will contunue
        for j in encryptionKey:# compairs char to the key
            if char == j:#looks to see if char is in the key and replcaes the letter with the right charater
                location = encryptionKey.find(j)# Find location of the letter in the key string
                if location != 26:# If the string of the key is not greater than 26 char
                    decryptLine += chr(ord('a') + (location))#Replace char with decrypted character
                    break
        for k in encryptionKey.upper(): #Looks if char is in the key but all in uppercase
            if char == k:
                location = encryptionKey.upper().find(k)# Find location of the letter in the key string
                if location != 26: #If the string of the key is not greater than 26 char
                    decryptLine += chr(ord('A')+location)#Looks if char is in the key but all in uppercase
                    break

    return(decryptLine)

def menu():
    while(True):
        try:
            #Gets the input file's name
            in_file = input("Enter the name of the file that you want to decrypt: ")
            input_message = open(in_file, 'r')#Checks if file exists
            break
        except IOError:
            #if flsile does not exist, it clears the screen and prompts for a
            #new file name
            print("The file does not exist. Please try again.")


    try:
        while(True):
                #Gets the input file's name
            out_file = input("Enter the name of the file that you want to print the output to: ")
            if ( out_file == in_file):#checks id new input is the same is the input file
                print("This is you input file, please Try again.")
                continue

            if (os.path.exists("./"+out_file)):#Checks if file exists
                overwrite = input("\nThis file already exists, do you want to overwrite it?(yes or no): ")
                if (overwrite == 'yes'):# If yes, it will open the file and overwrite it
                    output = open(out_file, 'w')
                elif(overwrite == 'no' ):# If no user will be prompted a different options
                    continue
                else:
                    print("Invalid input")
                    continue
            output = open(out_file, 'w')
            break
    except IOError:
        #If the file does not exist, it creates a new file with the same name
        print("Output will be save in file", out_file)
        output = open(out_file, 'w')

    Encryptedkey = open('EncryptionKey.txt', 'r')
    key_list = Encryptedkey.readlines()
    key = ""#String version of ENcryption key
    for i in key_list:#Convers key from a list to a string
        key += i

    for line_str in input_message:#Gets a line from the file and converts it into plain text
        print(substitutionDecrypt(line_str,key), end="", file = output)#Converts each line and prints them on the new file.

menu()#Starts program
print("Done.")
