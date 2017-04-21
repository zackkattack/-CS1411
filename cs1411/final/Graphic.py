import tkinter as tk

LARGE_FONT = ("Verdana", 12)

class SeaofBYcapp(tk.Tk):
    def __init__(self, *args, **kargs):
        tk.Tk.__init__(self, *args, **kargs)
        container = tk.Frame(self)
        self.geometry("648x648")

        container.pack(side='top', fill='both', expand = True)

        container.grid_rowconfigure(0,weight = 1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne):

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
        label = tk.Label(self, text ="Tic Tac Toe", font=LARGE_FONT)
        label.pack(pady = 10, padx = 10)

        button = tk.Button(self, text="1 v 1",
                                command=lambda: controller.show_frame(PageOne))
        button.pack()

        button = tk.Button(self, text="AI",
                                command=lambda: controller.show_frame(PageOne))
        button.pack()

        button = tk.Button(self, text="Exit", command='')
        button.pack()

def move_click():
        button_text.set('x')

class PageOne(tk.Frame):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text ="Tic Tac Toe", font=LARGE_FONT)
        #label.pack(pady = 10, padx = 10)

        button_text = tk.StringVar()

        button = tk.Button(self, text="E",command=move_click)
        button.grid(row=0, column=1 , padx=(100, 10))
        ##button.pack()

        button_text = tk.StringVar()

        button = tk.Button(self, text="E",
                                    command=lambda: controller.show_frame(move_click))
        button.grid(row=0, column=2, padx=(100, 10))
        ##button.pack()

        button_text = tk.StringVar()

        button = tk.Button(self, text="E",
                                command=lambda: controller.show_frame(move_click))
        button.grid(row=0, column=3, padx=(100, 10))
        ##button.pack()

        button_text = tk.StringVar()

        button = tk.Button(self, text="E",
                        command=lambda: controller.show_frame(move_click))
        button.grid(row=1, column=1, padx=(100, 10))
        ##button.pack()

        button_text = tk.StringVar()

        button = tk.Button(self, text="E",
                                    command=lambda: controller.show_frame(move_click))
        button.grid(row=1, column=2, padx=(100, 10))
        ##button.pack()

        button_text = tk.StringVar()

        button = tk.Button(self, text="E",
                                        command=lambda: controller.show_frame(move_click))
        button.grid(row=1, column=3, padx=(100, 10))
        ##button.pack()

        button_text = tk.StringVar()

        button = tk.Button(self, text="E",
                                        command=lambda: controller.show_frame(move_click))
        button.grid(row=2, column=1, padx=(100, 10))
        ##button.pack()

        button_text = tk.StringVar()

        button = tk.Button(self, text="E",
                                        command=lambda: controller.show_frame(move_click))
        button.grid(row=2, column=2, padx=(100, 10))
        ##button.pack()

        button_text = tk.StringVar()

        button = tk.Button(self, text="E",
                                        command=lambda: controller.show_frame(move_click))
        button.grid(row=2, column=3, padx=(100, 10))
        ##button.pack()



app = SeaofBYcapp()

app.mainloop()
