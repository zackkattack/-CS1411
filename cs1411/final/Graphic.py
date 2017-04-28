import tkinter as tk
import tkinter as ttk
from random import randint

board = ['','','','','','','','','']# Array of game board
click = True# Checks is player has clicked a button
AI = False # Signals program to run program with AI
name = "a"
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
                           command=lambda: MainMenu.playerType(controller, player))
        player.pack()

        #Button made for AI game play. When clicked, it will display a AI game play
        playerAI = tk.Button(self,
                           text="AI",
                           command=lambda: MainMenu.playerType(controller, playerAI))
        playerAI.pack()

        #Exit button. When clicked, closes window
        exit = tk.Button(self, text="Exit", command=quit)
        exit.pack()

    #Indicator of what type of game play to load. Saves in variable AI and is loaded in
    #Game class to initiate AI game play or 2 player game play
    def playerType(controller, button):
        controller.show_frame(Game)# Displays Game stage
        if button['text']== "AI":
            AI = True

#Ending page that asks if player wants to play again or quit
class EndPage(tk.Frame):

    #Constructor of EndPage. Darws new frame and displays buttons
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text ="End Page", font=LARGE_FONT)
        label.pack(pady = 10, padx = 10)

        self.winnerDisplay(label)

        #Button that restarts program when pressed
        play_again = tk.Button(self, text="Play Again",
                                command= self.start_over)
        play_again.pack()

        #Button that quits program when clicked
        exit = tk.Button(self, text="Exit", command=quit)
        exit.pack()

    #Checks variable board to see who won the game and displays winner at the top
    #of the window
    def winnerDisplay(self, Label):
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
                Label.labelText = "O wins! Would you like to play again?"

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
                Label.labelText = "x wins! Would you like to play again?"
        else:
            for i in board:
                if i == "":
                    break
                Label.labelText = "Stalmate! Would you like to play again?"

    def start_over(self):
        Game.destroy()



#Holds functions needed for Tic-Tac-Toe. Displays board and buttons that chnage
#depending on what happens
class Game(tk.Frame):
    #constructor for Game
    def __init__(c, p, cont):
        c.draw( p, cont)

    #Creats fram and buttons for the game
    def draw(container, parent, controller):
        tk.Frame.__init__(container,parent)
        label = tk.Label(container, text ="Game", font=LARGE_FONT)

        buttons = tk.StringVar()#

        #Buttons made to represent the positon on the board. when clicked it
        #calls the function checker
        button1 = ttk.Button(container,
                             text=board[0],
                             font= "Arial 30 bold",
                             command=lambda: Game.checker(controller,button1,1),
                             height = 5,
                             width = 10)
        button1.grid(row=0, column=1 )

        button2 = ttk.Button(container,
                             text=board[1],
                             font= "Arial 30 bold",
                             command=lambda: Game.checker(controller, button2,2),
                             height = 5,
                             width = 10)
        button2.grid(row=0, column=2 )

        button3 = ttk.Button(container,
                             text=board[2],
                             font= "Arial 30 bold",
                             command=lambda: Game.checker(controller, button3,3) ,
                             height = 5,
                             width = 10)
        button3.grid(row=0, column=3 )

        button4 = ttk.Button(container,
                             text=board[3],
                             font= "Arial 30 bold",
                             command=lambda: Game.checker(controller, button4,4),
                             height = 5,
                             width = 10)
        button4.grid(row=1, column=1 )

        button5 = ttk.Button(container,
                             text=board[4],
                             font= "Arial 30 bold",
                             command=lambda: Game.checker(controller, button5,5),
                             height = 5,
                             width = 10)
        button5.grid(row=1, column=2 )

        button6 = ttk.Button(container,
                             text=board[5],
                             font= "Arial 30 bold",
                             command=lambda: Game.checker(controller, button6,6),
                             height = 5,
                             width = 10)
        button6.grid(row=1, column=3 )

        button7 = ttk.Button(container,
                             text=board[6],
                             font= "Arial 30 bold",
                             command=lambda: Game.checker(controller, button7,7) ,
                             height = 5,
                             width = 10)
        button7.grid(row=2, column=1 )

        button8 = ttk.Button(container,
                             text=board[7],
                             font= "Arial 30 bold",
                             command=lambda: Game.checker(controller, button8,8),
                             height = 5,
                             width = 10)
        button8.grid(row=2, column=2 )

        button9 = ttk.Button(container,
                             text=board[8],
                             font= "Arial 30 bold",
                             command=lambda: Game.checker(controller, button9,9),
                             height = 5,
                             width = 10)
        button9.grid(row=2, column=3 )

        #Button that take player back to the main menu when clicked
        mainMenu = ttk.Button(container, text="Main Menu", font= "Arial 10 bold",
                                command=lambda: controller.show_frame(MainMenu))
        mainMenu.grid(row=3, column=1, padx = 10, pady= 10 )

        #Button that ends the game
        restart = ttk.Button(container, text="End", font= "Arial 10 bold",
                                command=quit)
        restart.grid(row=3, column=3 , padx = 10, pady = 10)

    #Checks if there is a winner after a game button is pressed
    def checker(controller, button,  num):
            global click
            global board

            #checks weather to load AI gamem play or 2 Player by checking if
            # AI is true or false
            if not(AI): #If false, got to regular game play
                Game.player_vs_player(button, num)
            # elif AI:
            #     Game.AI(button, num)

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
                    print("O wins! Would you like to play again?")
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
                    print("x wins! Would you like to play again?")
                    controller.show_frame(EndPage)

            #Checks if the bord is full and theres no winner
            else:
                for i in board:
                    if i != "":
                        break
                    else:
                        print("Stalmate! Would you like to play again?")
                        controller.show_frame(EndPage)
            print(board)

    #Player vs Player
    def player_vs_player(button, num):
        global click
        global board

        if button["text"] == "" and click == True:
            board[num-1] = "X"
            button["text"]= "x"
            click = False
        elif button["text"] == "" and click == False:
            board[num-1] = "O"
            button["text"] ="O"
            click = True

    # def AI(button, num):
    #     global click
    #     global board
    #
    #     rand = randint(0,9)
    #
    #     if button["text"] == "" and click == True:
    #         board[num-1] = "X"
    #         button["text"]= "x"
    #         click = False
    #     elif button["text"] == "" and click == False:
    #         board[rand] = "O"
    #         button["text"] ="O"
    #         click = True
    #

app = TicTacToe()
app.resizable(width=False, height=False)#Restricts frame size
app.mainloop()
