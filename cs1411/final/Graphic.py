import tkinter as tk
import tkinter as ttk

board = ['','','','','','','','','']

click = True
LARGE_FONT = ("Verdana", 12)

class SeaofBYcapp(tk.Tk):
    def __init__(self, *args, **kargs):

        tk.Tk.__init__(self, *args, **kargs)

        tk.Tk.wm_title(self, "Tic-Tac-Toe")

        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand = False)
        container.grid_rowconfigure(0,weight = 1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, EndPage):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky ="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text ="Main Menu", font=LARGE_FONT)
        label.pack(pady = 10, padx = 10)

        button = tk.Button(self,
                           text="1 v 1",
                           command=lambda: controller.show_frame(PageOne))
        button.pack()

        button = tk.Button(self,
                           text="AI",
                           command=lambda: controller.show_frame(PageOne))
        button.pack()

        button = tk.Button(self, text="Exit", command=quit)
        button.pack()

def move_click():
    print('x')

def close_window():
    app.distroy()

class EndPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text ="EndPage", font=LARGE_FONT)
        label.pack(pady = 10, padx = 10)

        button = tk.Button(self, text="Play Again",
                                command=lambda: controller.show_frame(StartPage))
        button.pack()

        button = tk.Button(self, text="Exit", command=quit)
        button.pack()

#Game winning logic not functioning, fix later
def checker(button,  num):
        global click
        global board

        print("Hey you!")
        if button["text"] == "" and click == True:
            button["text"] = "X"
            board[num-1] = "X"
            click = False
        elif button["text"] == "" and click == False:
            button["text"] = "O"
            board[num-1] = "O"
            click = True
        #
        # if(board[0] == "O" and board[1] == "O"  and board[2] == "O" or
        #    board[3] == "O" and board[4] == "O"  and board[5] == "O" or
        #    board[6] == "O" and board[7] == "O"  and board[8] == "O" or
        #    board[0] == "O" and board[3] == "O"  and board[6] == "O" or
        #    board[1] == "O" and board[4] == "O"  and board[7] == "O" or
        #    board[2] == "O" and board[5] == "O"  and board[8] == "O" or
        #    board[0] == "O" and board[4] == "O"  and board[8] == "O" or
        #    board[2] == "O" and board[4] == "O"  and board[6] == "O" ):
        #         tkinter.messagebox.showinfo("O wins")

        # if(board[0] == "X" and board[1] == "X"  and board[2] == "X" or
        #    board[3] == "X" and board[4] == "X"  and board[5] == "X" or
        #    board[6] == "X" and board[7] == "X"  and board[8] == "X" or
        #    board[0] == "X" and board[3] == "X"  and board[6] == "X" or
        #    board[1] == "X" and board[4] == "X"  and board[7] == "X" or
        #    board[2] == "X" and board[5] == "X"  and board[8] == "X" or
        #    board[0] == "X" and board[4] == "X"  and board[8] == "X" or
        #    board[2] == "X" and board[4] == "X"  and board[6] == "X" ):
        #         winner = ttk.Button(tkinter, text="", font= "Arial 30 bold", command=lambda: EndPage , height = 5, width = 10)
        #         winner.pack()

        print(board)

def start_over():
    for i in range(0,len(board)):
        board[i] = ""

    controller.show_frame(StartPage)


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text ="Game", font=LARGE_FONT)

        buttons = tk.StringVar()

        print("hey")
        button1 = ttk.Button(self,
                             text="",
                             font= "Arial 30 bold",
                             command=lambda: checker(button1,1),
                             height = 5,
                             width = 10)
        button1.grid(row=0, column=1 )

        button2 = ttk.Button(self,
                             text="",
                             font= "Arial 30 bold",
                             command=lambda: checker(button2,2),
                             height = 5,
                             width = 10)
        button2.grid(row=0, column=2 )

        button3 = ttk.Button(self,
                             text="",
                             font= "Arial 30 bold",
                             command=lambda: checker(button3,3) ,
                             height = 5,
                             width = 10)
        button3.grid(row=0, column=3 )

        button4 = ttk.Button(self,
                             text="",
                             font= "Arial 30 bold",
                             command=lambda: checker(button4,4),
                             height = 5,
                             width = 10)
        button4.grid(row=1, column=1 )

        button5 = ttk.Button(self,
                             text="",
                             font= "Arial 30 bold",
                             command=lambda: checker(button5,5),
                             height = 5,
                             width = 10)
        button5.grid(row=1, column=2 )

        button6 = ttk.Button(self,
                             text="",
                             font= "Arial 30 bold",
                             command=lambda: checker(button6,6),
                             height = 5,
                             width = 10)
        button6.grid(row=1, column=3 )

        button7 = ttk.Button(self,
                             text="",
                             font= "Arial 30 bold",
                             command=lambda: checker(button7,7) ,
                             height = 5,
                             width = 10)
        button7.grid(row=2, column=1 )

        button8 = ttk.Button(self,
                             text="",
                             font= "Arial 30 bold",
                             command=lambda: checker(button8,7),
                             height = 5,
                             width = 10)
        button8.grid(row=2, column=2 )

        button9 = ttk.Button(self,
                             text="",
                             font= "Arial 30 bold",
                             command=lambda: checker(button9,9),
                             height = 5,
                             width = 10)
        button9.grid(row=2, column=3 )

        End = ttk.Button(self, text="End", font= "Arial 10 bold",
                                command=lambda: controller.show_frame(EndPage))
        End.grid(row=3, column=2 , padx = 10, pady = 10)

        StartOver = ttk.Button(self, text="Start Over", font= "Arial 10 bold",
                                command=lambda:controller.show_frame(StartPage))
        StartOver.grid(row=3, column=1, padx = 10, pady= 10 )


        print("you there")


app = SeaofBYcapp()
app.resizable(width=False, height=False)
app.mainloop()
