#Zach & Bryan Arias
#CS 1411
#5/5/17
#
#Project Description: In our Tic Tac Toe game we created a simple program to run
# Tic Tac Toe.In a board with 9 slots, the player is given the choice to choose
# character “X” or  ”O”. Once player chooses the character of their choice, you
# get to choose what slot you want. If you get 3 characters in a row you win the
# game, if not the computer wins. After the game is over, it will display who the
# winner is on text box then. After you click okay on the box, the program will
# close.
#
# Major steps in the code:
#
## Main Menu:
##
## 1V1 button: Takes you to player vs play game play of tic tac toe where you play against #another player.
## AI button: Takes you to AI game play of tic tac toe where you can play against the computer
## Exit button: Exits the program
##
## Game play:
##
## Game buttons: Allows to click the buttons to select a spot. if there is a winner or a stalemate #there will be a pop up window saying that that there is a winner or stalemate. Then it till take #you the end frame.
##
## End Screen:
##
## End Button: Closes the window and ends the program.
#
#Development:
##Zachary Carson:
##
##Class TicTac Toe:
##    constructor, def show_frame
##Class Game:
##    def checker, def AI, def draw
##
##Bryan Arias:
##
##Class EndPage:
##    constructor
##Class MainMenu:
##    def draw, def check_if_AI
##Class Game:
##    def player_vs_player, def draw
#
#
#Instructions:
#
#In order to start Tic-Tac-Toe run the command: `python Tic-Tac-Toe.py`.
#
#TestCases:
#Player vs. Player game play : One winner
#
#Input:
# 1v1 button -> game play -> one winner
#Expected OutPut:
#Display the one winner and transition to end screen where they close the program by pressing #end or exciting out of the window
#
#TestCases:
#Player vs. Player game play : Stalemate
#Input:
#1v1 button -> game play -> stalemate
#
#Expected OutPut:
#Tells player there is a stalemate and transition to end screen where they close the program by #pressing #end or exciting out of the window
#
#TestCases:
#Player vs. computer: One winner
#
#Input:
#1v1 button -> game play -> one winner
#
#Expected OutPut:
#Display the one winner and transition to end screen where they close the program by pressing #end or exciting out of the window
#
#TestCases:
#Player vs. computer: Stalemate
#Input:
#1v1 button -> game play -> stalemate
#
#Expected OutPut:
#Tells player there is a stalemate and transition to end screen where they close the program by #pressing #end or exciting out of the window
#
#TestCases:
#End Program: Window X or End button
#Input:
#Pressing the end button at any point of the program, or clicking the window x
#
#Expected OutPut:
#End program
#
#Results: All of the Test Cases passed. The expected out put was returned.
#Program:

import tkinter as tk
import tkinter as ttk
from tkinter import messagebox
import random

board = ['','','','','','','','','']# Array of game board
click = True# Checks is player has clicked a button
AI = False # Signals program to run program with AI
LARGE_FONT = ("Verdana", 12)

#This class darws the menu for each part of the program and renders all stages
#in the same window
class TicTacToe(tk.Tk):
    #Sets up constructor of window
    def __init__(self, *args, **kargs):

        #Creates a instance of tkinter
        tk.Tk.__init__(self, *args, **kargs)
        #Assign name to window
        tk.Tk.wm_title(self, "Tic-Tac-Toe")

        #Sets up pramaters in the of window
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand = False)
        container.grid_rowconfigure(0,weight = 1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}# list of stages in the program

        #Iterates through the list of stages and renders them into the window
        # created above
        for F in (MainMenu, Game, EndPage):

            # new instance of a frame with the name of itterated value
            frame = F(container, self)
            self.frames[F] = frame
            #frame dimensions
            frame.grid(row=0, column=0, sticky ="nsew")

        self.show_frame(MainMenu)# displays the first stage in the program

    # Made to display different frames in the window created
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise() #Raise this widget in the stacking order

#Logic and rendering for the main menu giving the user the option to play 2 player
# play against AI or exit the program
class MainMenu(tk.Frame):

    #constructor of MainMenu
    def __init__(self, parent, controller):
        self.draw(parent, controller)

    #creation of frame, buttons, and the logic that goes to them
    def draw(self,  parent, controller):
        #Creation of new frame
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text ="Main Menu", font=LARGE_FONT)
        label.pack(pady = 10, padx = 10)

        #Button made for 1 on 1 game play. When clicked, it will display a 2
        #player game play
        player = tk.Button(self,
                           text="1 v 1",
                           command=lambda: controller.show_frame(Game))
        player.pack()

        #Button made for AI game play. When clicked, it will display a AI game play
        playerAI = tk.Button(self,
                           text="AI",
                           command=lambda: MainMenu.check_if_AI(controller))
        playerAI.pack()

        #Exit button. When clicked, closes window
        exit = tk.Button(self, text="Exit", command=quit)
        exit.pack()

    #Indicator of what type of game play to load. Saves in variable AI and is loaded in
    #Game class to initiate AI game play or 2 player game play
    def check_if_AI(controller):
        global AI
        AI = True
        controller.show_frame(Game)# Displays Game stage

#Ending page that asks if player wants to play again or quit
class EndPage(tk.Frame):
    message = ""

    #Constructor of EndPage. Darws new frame and displays buttons
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        label = tk.Label(self, textvariable ="Game Over!", font=LARGE_FONT)
        label.pack(pady = 10, padx = 10)

        #Button that quits program when clicked
        exit = tk.Button(self, text="Exit", command=quit)
        exit.pack()


#Holds functions needed for Tic-Tac-Toe. Displays board and buttons that chnage
#depending on what happens
class Game(tk.Frame):


    #constructor for Game
    def __init__(c, p, cont):
        button_array = []
        numbers_of_spaces = []
        c.draw( p, cont, button_array, numbers_of_spaces)

    #Creats frame and buttons for the game
    def draw(container, parent, controller, button_array, numbers_of_spaces):
        numbers_of_spaces = [0,1,2,3,4,5,6,7,8]
        lastMove =0

        tk.Frame.__init__(container,parent)
        label = tk.Label(container, text ="Game", font=LARGE_FONT)

        buttons = tk.StringVar()#

        #Buttons made to represent the positon on the board. when clicked it
        #calls the function checker
        button0 = ttk.Button(container,
                             text=board[0],
                             font= "Arial 30 bold",
                             command=lambda: Game.checker(controller, 0, button_array, numbers_of_spaces, lastMove),
                             height = 5,
                             width = 10)
        button0.grid(row=0, column=1 )
        button_array.append(button0)

        button1 = ttk.Button(container,
                             text=board[1],
                             font= "Arial 30 bold",
                             command=lambda: Game.checker(controller, 1, button_array,numbers_of_spaces, lastMove),
                             height = 5,
                             width = 10)
        button1.grid(row=0, column=2 )
        button_array.append(button1)

        button2 = ttk.Button(container,
                             text=board[2],
                             font= "Arial 30 bold",
                             command=lambda: Game.checker(controller, 2, button_array, numbers_of_spaces, lastMove) ,
                             height = 5,
                             width = 10)
        button2.grid(row=0, column=3 )
        button_array.append(button2)

        button3 = ttk.Button(container,
                             text=board[3],
                             font= "Arial 30 bold",
                             command=lambda: Game.checker(controller, 3, button_array, numbers_of_spaces, lastMove),
                             height = 5,
                             width = 10)
        button3.grid(row=1, column=1 )
        button_array.append(button3)

        button4 = ttk.Button(container,
                             text=board[4],
                             font= "Arial 30 bold",
                             command=lambda: Game.checker(controller, 4, button_array,numbers_of_spaces, lastMove),
                             height = 5,
                             width = 10)
        button4.grid(row=1, column=2 )
        button_array.append(button4)

        button5 = ttk.Button(container,
                             text=board[5],
                             font= "Arial 30 bold",
                             command=lambda: Game.checker(controller, 5,button_array, numbers_of_spaces, lastMove),
                             height = 5,
                             width = 10)
        button5.grid(row=1, column=3 )
        button_array.append(button5)

        button6 = ttk.Button(container,
                             text=board[6],
                             font= "Arial 30 bold",
                             command=lambda: Game.checker(controller, 6,button_array, numbers_of_spaces, lastMove) ,
                             height = 5,
                             width = 10)
        button6.grid(row=2, column=1 )
        button_array.append(button6)

        button7 = ttk.Button(container,
                             text=board[7],
                             font= "Arial 30 bold",
                             command=lambda: Game.checker(controller, 7,button_array, numbers_of_spaces,lastMove),
                             height = 5,
                             width = 10)
        button7.grid(row=2, column=2 )
        button_array.append(button7)

        button8 = ttk.Button(container,
                             text=board[8],
                             font= "Arial 30 bold",
                             command=lambda: Game.checker(controller, 8,button_array, numbers_of_spaces, lastMove),
                             height = 5,
                             width = 10)
        button8.grid(row=2, column=3 )
        button_array.append(button8)

        #Button that take player back to the main menu when clicked
        mainMenu = ttk.Button(container, text="Main Menu", font= "Arial 10 bold",
                                command=lambda: controller.show_frame(MainMenu))
        mainMenu.grid(row=3, column=1, padx = 10, pady= 10 )

        #Button that ends the game
        restart = ttk.Button(container, text="End", font= "Arial 10 bold",
                                command=quit)
        restart.grid(row=3, column=3 , padx = 10, pady = 10)

    #Checks if there is a winner after a game button is pressed
    def checker(controller, num, button_array, numbers_of_spaces,lastMove):
            global click
            global board

            #checks weather to load AI gamem play or 2 Player by checking if
            # AI is true or false
            if not(AI): #If false, got to regular game play
                Game.player_vs_player(button_array, num)
            elif AI:
                 Game.AI(num, button_array, numbers_of_spaces, lastMove)

            print(board)

            #Checks if O wins, if so displays "O wins!, would you like to play again?"
            #displays at the top of the window
            if(board[0] == "O" and board[1] == "O"  and board[2] == "O" or
               board[3] == "O" and board[4] == "O"  and board[5] == "O" or
               board[6] == "O" and board[7] == "O"  and board[8] == "O" or
               board[0] == "O" and board[3] == "O"  and board[6] == "O" or
               board[1] == "O" and board[4] == "O"  and board[7] == "O" or
               board[2] == "O" and board[5] == "O"  and board[8] == "O" or
               board[0] == "O" and board[4] == "O"  and board[8] == "O" or
               board[2] == "O" and board[4] == "O"  and board[6] == "O" ):
                    #Displays winner on pop up box
                    messagebox.showinfo("Player O","You have won the game")
                    controller.show_frame(EndPage)

            #Checks if X wins, if so displays "X wins!, would you like to play again?"
            #displays at the top of the window
            elif(board[0] == "X" and board[1] == "X"  and board[2] == "X" or
               board[3] == "X" and board[4] == "X"  and board[5] == "X" or
               board[6] == "X" and board[7] == "X"  and board[8] == "X" or
               board[0] == "X" and board[3] == "X"  and board[6] == "X" or
               board[1] == "X" and board[4] == "X"  and board[7] == "X" or
               board[2] == "X" and board[5] == "X"  and board[8] == "X" or
               board[0] == "X" and board[4] == "X"  and board[8] == "X" or
               board[2] == "X" and board[4] == "X"  and board[6] == "X" ):
                    #Displays winner on pop up box
                    messagebox.showinfo("Player X!", "You have won the game!")
                    controller.show_frame(EndPage)

            #Checks if the bord is full and theres no winner
            else:
                j = 0
                #Loops through the array and chaeks if the board is full with peices
                for i in board:
                    if i == "X" or i == "O":
                        j +=1
                if j == 9:
                    #Displays winner on pop up box
                    messagebox.showinfo("There is no winner","Stalemate!")
                    controller.show_frame(EndPage)



    #Player vs Player Game logic. Lets one player make a move then restricts them
    #till after the other player makes their move.
    def player_vs_player(button_array, num):
        global click
        global board

        #Allows for 1v1 input
        if button_array[num]["text"] == "" and click == True:
            board[num] = "X"
            button_array[num]["text"]= "X"
            click = False
        elif button_array[num]["text"] == "" and click == False:
            board[num] = "O"
            button_array[num]["text"] ="O"
            click = True

    #Allows player to Play against the computer
    def AI(num, button_array, numbers_of_spaces, lastMove):
        global click
        global board

        #Allows for the player to click a box
        if button_array[num]["text"] == "" and click == True  and num in numbers_of_spaces:
            board[num] = "X"
            button_array[num]["text"]= "x"
            click = False
            #removes number from list of open spaces
            numbers_of_spaces.remove(num)

        if not numbers_of_spaces:
            return

        #Checks if rand is a valid move, and if the space is open. If so it
        # makes its move to that spot
        try:
            #represent the box that the computer chooses
            rand = random.choice(numbers_of_spaces)
            #Checks if the spot is empty and rand is not the same the user"s input
            #if Given a bad number, the try will reassign the number to a different one
            if button_array[rand]["text"] == "" and rand != num :
                while(True):
                    #checks if spot is a valid move
                    try:
                        if rand < 9 and (rand in numbers_of_spaces):
                            if button_array[lastMove-1]["text"] == "" and (lastMove-1)in numbers_of_spaces:
                                button_array[lastMove-1]["text"] = 'O'
                                board[lastMove-1] = "O"
                                click = True
                                numbers_of_spaces.remove(lastMove-1)
                                break
                            elif button_array[lastMove+1]["text"] == ""and (lastMove+1)in numbers_of_spaces:
                                button_array[lastMove+1]["text"] = 'O'
                                board[lastMove+1] = "O"
                                click = True
                                numbers_of_spaces.remove(lastMove+1)
                                break
                            elif button_array[lastMove+2]["text"] == ""and (lastMove+2)in numbers_of_spaces:
                                button_array[lastMove+2]["text"] = 'O'
                                board[lastMove+2] = "O"
                                click = True
                                numbers_of_spaces.remove(lastMove+2)
                                break
                            elif button_array[lastMove-2]["text"] == ""and (lastMove-2)in numbers_of_spaces:
                                button_array[lastMove-2]["text"] = 'O'
                                board[lastMove-2] = "O"
                                click = True
                                numbers_of_spaces.remove(lastMove-2)
                                break
                            elif button_array[lastMove+3]["text"] == ""and (lastMove+3)in numbers_of_spaces:
                                button_array[lastMove+3]["text"] = 'O'
                                board[lastMove+3] = "O"
                                click = True
                                numbers_of_spaces.remove(lastMove+3)
                                break
                            elif button_array[lastMove-3]["text"] == ""and (lastMove-3)in numbers_of_spaces:
                                button_array[lastMove-3]["text"] = 'O'
                                board[lastMove-3] = "O"
                                click = True
                                numbers_of_spaces.remove(lastMove-3)
                                break
                            elif button_array[lastMove+4]["text"] == ""and (lastMove+4)in numbers_of_spaces:
                                button_array[lastMove+4]["text"] = 'O'
                                board[lastMove+4] = "O"
                                click = True
                                numbers_of_spaces.remove(lastMove+4)
                                break
                            elif button_array[lastMove-4]["text"] == ""and (lastMove-4)in numbers_of_spaces:
                                button_array[lastMove-4]["text"] = 'O'
                                board[lastMove-4] = "O"
                                click = True
                                numbers_of_spaces.remove(lastMove-4)
                                break
                            elif rand in numbers_of_spaces:
                                button_array[rand]["text"] = 'O'
                                board[rand] = "O"
                                click = True
                                #removes spot from list of spots. If spot is not
                                #in the list, the function will return continue
                                #through the loop
                                try:
                                    numbers_of_spaces.remove(rand)
                                except IndexError:
                                    continue
                                break
                        # If the random number generated doesnt met the condidtions
                        # assign it a new number
                        else:
                            rand = random.choice(numbers_of_spaces)
                    # If the random number generated doesnt met the condidtions
                    # assign it a new number
                    except IndexError:
                        rand = random.choice(numbers_of_spaces)

            lastMove = rand# ressign the last move to current move
        #if there is a stalemate, the program will jump out of the Loops
        except IndexError:
            return

app = TicTacToe()
app.resizable(width=False, height=False)#Restricts frame size
app.mainloop()
