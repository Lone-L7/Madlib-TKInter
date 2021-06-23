from tkinter import *
import menu

class Madlib3Input():
    def __init__(self, main, ffamily, fweight, white, width, relx, anchor):
        self.main = main

        self.noun1Msg = Label(self.main, font=(ffamily, 15, fweight), bg=white, text='Your Name: ')
        self.noun1Msg.place(relx=relx, rely=0.4, anchor=anchor)

        self.noun1 = Entry(self.main, font=(ffamily, 15, fweight), bg=white, width=width)
        self.noun1.place(relx=relx, rely=0.45, anchor=anchor)

        self.missing = Label(self.main, font=(ffamily, 15, fweight), bg=white, fg='Dark Red', text='Please Insert Words!')

        self.submitBtn = Button(self.main, font=(ffamily, 15, fweight), bg='yellow', activebackground='yellow', text='Submit', command=self.submit)
        self.submitBtn.place(relx=relx, rely=0.55, anchor=anchor)

    def submit(self):
        if (not self.noun1.get().isalpha()):
            self.missing.place(relx=0.5, rely=0.5, anchor='center')
        else:
            self.result = 'Hello ' + self.noun1.get() + '!'
            self.answer = Label(self.main, font=('Sans-Serif 15 bold'), bg='white', text=self.result, wraplength=425, justify=LEFT)
            self.answer.place(relx=0.5, rely=0.5, anchor='center')
            self.missing.destroy()
            self.noun1Msg.destroy()
            self.noun1.destroy()
            self.submitBtn.destroy()
            self.repeatBtn = Button(self.main, font=('Sans-Serif 15 bold'), bg='Yellow', activebackground='Yellow', text='Play Again?', command=self.repeat)
            self.repeatBtn.place(relx=0.5, rely=0.9, anchor='center')

    def repeat(self):
        self.answer.destroy()
        self.repeatBtn.destroy()
        menu.MainMenu(self.main)