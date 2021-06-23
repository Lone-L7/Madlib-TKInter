from tkinter import *
import menu

class Madlib1Input():
    def __init__(self, main, ffamily, fweight, white, width, relx, anchor):
        self.main = main

        self.noun1Msg = Label(self.main, font=(ffamily, 15, fweight), bg=white, text='Person: ')
        self.noun1Msg.place(relx=relx, rely=0.25, anchor=anchor)

        self.noun1 = Entry(self.main, font=(ffamily, 15, fweight), bg=white, width=width)
        self.noun1.place(relx=relx, rely=0.3, anchor=anchor)

        self.verb1Msg = Label(self.main, font=(ffamily, 15, fweight), bg=white, text='Verb: ')
        self.verb1Msg.place(relx=relx, rely=0.4, anchor=anchor)

        self.verb1 = Entry(self.main, font=(ffamily, 15, fweight), bg=white, width=width)
        self.verb1.place(relx=relx, rely=0.45, anchor=anchor)

        self.verb2Msg = Label(self.main, font=(ffamily, 15, fweight), bg=white, text='Another Verb: ')
        self.verb2Msg.place(relx=relx, rely=0.55, anchor=anchor)

        self.verb2 = Entry(self.main, font=(ffamily, 15, fweight), bg=white, width=width)
        self.verb2.place(relx=relx, rely=0.6, anchor=anchor)

        self.missing = Label(self.main, font=(ffamily, 15, fweight), bg=white, fg='Dark Red', text='Please Insert Words!')

        self.submitBtn = Button(self.main, font=(ffamily, 15, fweight), bg='yellow', activebackground='yellow', text='Submit', command=self.submit)
        self.submitBtn.place(relx=relx, rely=0.75, anchor=anchor)

    def submit(self):
        if (not self.noun1.get().isalpha() and not self.verb1.get().isalpha() and not self.verb2.get().isalpha()):
            self.missing.place(relx=0.5, rely=0.675, anchor='center')
        else:   
            self.result = 'My favorite person is ' + self.noun1.get() + '. It is because I ' + self.verb1.get() + ' them and I want to ' + self.verb2.get() +  '.'
            self.answer = Label(self.main, font=('Sans-Serif 15 bold'), bg='white', text=self.result, wraplength=425, justify=LEFT)
            self.answer.place(relx=0.5, rely=0.5, anchor='center')
            self.missing.destroy()
            self.noun1Msg.destroy()
            self.noun1.destroy()
            self.verb1Msg.destroy()
            self.verb1.destroy()
            self.verb2Msg.destroy()
            self.verb2.destroy()
            self.submitBtn.destroy()
            self.repeatBtn = Button(self.main, font=('Sans-Serif 15 bold'), bg='Yellow', activebackground='Yellow', text='Play Again?', command=self.repeat)
            self.repeatBtn.place(relx=0.5, rely=0.9, anchor='center')

    def repeat(self):
        self.answer.destroy()
        self.repeatBtn.destroy()
        menu.MainMenu(self.main)
        
