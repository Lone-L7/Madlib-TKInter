from tkinter import *
import random
import madlibEntry.madlib1
import madlibEntry.madlib2
import madlibEntry.madlib3

class Window():
    def __init__(self, main, title, geo, size, size2, bgColor, boxColor):
        self.main = main
        self.main.title(title)
        self.main.geometry(geo)
        self.main.resizable(size, size2)
        self.main.configure(bg=bgColor)
        self.box = Frame(self.main, bg=boxColor)
        self.box.place(relwidth=0.905, relheight=0.935, relx=0.05, rely=0.03)

class Roulette():
    def __init__(self, main):
        self.main = main

    def pick1(self):
        self.madlib1 = madlibEntry.madlib1.Madlib1Input(self.main, 'sans-serif', 'bold', 'white', 17, 0.5, 'center')

    def pick2(self):
        self.madlib2 = madlibEntry.madlib2.Madlib2Input(self.main, 'sans-serif', 'bold', 'white', 17, 0.5, 'center')

    def pick3(self):
        self.madlib3 = madlibEntry.madlib3.Madlib3Input(self.main, 'sans-serif', 'bold', 'white', 17, 0.5, 'center')

class MainMenu():
    def __init__(self, main):
        self.main = main

        self.title = Label(self.main, font=('sans-serif 50 bold'), bg='white', text='MADLIB\nROULETTE')
        self.title.place(relx=0.5, rely=0.35, anchor='center')
        self.made = Label(self.main, font=('sans-serif 20 bold'), bg='white', text='made with python')
        self.made.place(relx=0.5, rely=0.5, anchor='center')
        self.start = Button(self.main, font=('sans-serif 25 bold'), bg='Yellow', activebackground='Yellow', text='START', command=self.startMadlib)
        self.start.place(relx=0.5, rely=0.6, anchor='center')
        self.quit = Button(self.main, font=('sans-serif 25 bold'), bg='Yellow', activebackground='Yellow', text='QUIT', command=main.destroy)
        self.quit.place(relx=0.5, rely=0.71, anchor='center')
        
    def startMadlib(self):
        self.title.destroy()
        self.made.destroy()
        self.start.destroy()
        self.quit.destroy()

        madlibs = [Roulette.pick1, Roulette.pick2, Roulette.pick3]
        random.choice(madlibs)(self)

if __name__=='__main__':
    root = Tk()
    Window(root, 'Madlib', '500x700', False, False, 'yellow', 'white')
    MainMenu(root)
    root.mainloop()