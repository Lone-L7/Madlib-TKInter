from tkinter import *
import menu

class Madlib2Input():
    def __init__(self, main, ffamily, fweight, white, width, relx, anchor):
        self.main = main

        self.verb1Msg = Label(self.main, font=(ffamily, 15, fweight), bg=white, text='Verb: ')
        self.verb1Msg.place(relx=relx, rely=0.1, anchor=anchor)

        self.verb1 = Entry(self.main, font=(ffamily, 15, fweight), bg=white, width=width)
        self.verb1.place(relx=relx, rely=0.15, anchor=anchor)

        self.verb2Msg = Label(self.main, font=(ffamily, 15, fweight), bg=white, text='Second Verb: ')
        self.verb2Msg.place(relx=relx, rely=0.25, anchor=anchor)

        self.verb2 = Entry(self.main, font=(ffamily, 15, fweight), bg=white, width=width)
        self.verb2.place(relx=relx, rely=0.3, anchor=anchor)

        self.verb3Msg = Label(self.main, font=(ffamily, 15, fweight), bg=white, text='Third Verb: ')
        self.verb3Msg.place(relx=relx, rely=0.4, anchor=anchor)

        self.verb3 = Entry(self.main, font=(ffamily, 15, fweight), bg=white, width=width)
        self.verb3.place(relx=relx, rely=0.45, anchor=anchor)

        self.noun1Msg = Label(self.main, font=(ffamily, 15, fweight), bg=white, text='Place: ')
        self.noun1Msg.place(relx=relx, rely=0.55, anchor=anchor)

        self.noun1 = Entry(self.main, font=(ffamily, 15, fweight), bg=white, width=width)
        self.noun1.place(relx=relx, rely=0.6, anchor=anchor)

        self.verb4Msg = Label(self.main, font=(ffamily, 15, fweight), bg=white, text='Verb: ')
        self.verb4Msg.place(relx=relx, rely=0.7, anchor=anchor)

        self.verb4 = Entry(self.main, font=(ffamily, 15, fweight), bg=white, width=width)
        self.verb4.place(relx=relx, rely=0.75, anchor=anchor)

        self.missing = Label(self.main, font=(ffamily, 15, fweight), bg=white, fg='Dark Red', text='Please Insert Words!')

        self.next = Button(self.main, font=(ffamily, 15, fweight), bg='yellow', activebackground='yellow', text='Next', command=lambda: self.nextPage('sans-serif', 'bold', 'white', 17, 0.5, 'center'))
        self.next.place(relx=relx, rely=0.9, anchor=anchor)

    def nextPage(self, ffamily, fweight, white, width, relx, anchor):
        if (not self.verb1.get().isalpha() and not self.verb2.get().isalpha() and not self.verb3.get().isalpha() and not self.noun1.get().isalpha() and not self.verb4.get().isalpha()):
            self.missing.place(relx=0.5, rely=0.825, anchor='center')
        else: 
            self.missing.place_forget()
            self.next.destroy()
            self.verb1Msg.place_forget()
            self.verb1.place_forget()
            self.verb2Msg.place_forget()
            self.verb2.place_forget()
            self.noun1Msg.place_forget()
            self.noun1.place_forget()
            self.verb3Msg.place_forget()
            self.verb3.place_forget()
            self.verb4Msg.place_forget()
            self.verb4.place_forget()

            self.noun2Msg = Label(self.main, font=(ffamily, 15, fweight), bg=white, text='Noun: ')
            self.noun2Msg.place(relx=relx, rely=0.1, anchor=anchor)

            self.noun2 = Entry(self.main, font=(ffamily, 15, fweight), bg=white, width=width)
            self.noun2.place(relx=relx, rely=0.15, anchor=anchor)

            self.noun3Msg = Label(self.main, font=(ffamily, 15, fweight), bg=white, text='Another Noun: ')
            self.noun3Msg.place(relx=relx, rely=0.25, anchor=anchor)

            self.noun3 = Entry(self.main, font=(ffamily, 15, fweight), bg=white, width=width)
            self.noun3.place(relx=relx, rely=0.3, anchor=anchor)

            self.verb5Msg = Label(self.main, font=(ffamily, 15, fweight), bg=white, text='Verb: ')
            self.verb5Msg.place(relx=relx, rely=0.4, anchor=anchor)

            self.verb5 = Entry(self.main, font=(ffamily, 15, fweight), bg=white, width=width)
            self.verb5.place(relx=relx, rely=0.45, anchor=anchor)

            self.verb6Msg = Label(self.main, font=(ffamily, 15, fweight), bg=white, text='How Many Hours: ')
            self.verb6Msg.place(relx=relx, rely=0.55, anchor=anchor)

            self.verb6 = Entry(self.main, font=(ffamily, 15, fweight), bg=white, width=width)
            self.verb6.place(relx=relx, rely=0.6, anchor=anchor)

            self.verb7Msg = Label(self.main, font=(ffamily, 15, fweight), bg=white, text='Another Verb: ')
            self.verb7Msg.place(relx=relx, rely=0.7, anchor=anchor)

            self.verb7 = Entry(self.main, font=(ffamily, 15, fweight), bg=white, width=width)
            self.verb7.place(relx=relx, rely=0.75, anchor=anchor)

            self.next2 = Button(self.main, font=('Sans-Serif 15 bold'), bg='Yellow', activebackground='Yellow', text='Next', command=lambda: self.nextPage2('sans-serif', 'bold', 'white', 17, 0.5, 'center'))
            self.next2.place(relx=0.5, rely=0.9, anchor='center')

    def nextPage2(self, ffamily, fweight, white, width, relx, anchor):
        if (not self.noun2.get().isalpha() and not self.noun3.get().isalpha() and not self.verb5.get().isalpha() and not self.verb6.get().isalpha() and not self.verb7.get().isalpha()):
            self.missing.place(relx=0.5, rely=0.825, anchor='center')
        else: 
            self.missing.place_forget()
            self.next2.destroy()
            self.noun2Msg.place_forget()
            self.noun2.place_forget()
            self.noun3Msg.place_forget()
            self.noun3.place_forget()
            self.verb5Msg.place_forget()
            self.verb5.place_forget()
            self.verb6Msg.place_forget()
            self.verb6.place_forget()
            self.verb7Msg.place_forget()
            self.verb7.place_forget()

            self.verb8Msg = Label(self.main, font=(ffamily, 15, fweight), bg=white, text='Verb: ')
            self.verb8Msg.place(relx=relx, rely=0.4, anchor=anchor)

            self.verb8 = Entry(self.main, font=(ffamily, 15, fweight), bg=white, width=width)
            self.verb8.place(relx=relx, rely=0.45, anchor=anchor)

            self.submitBtn = Button(self.main, font=(ffamily, 15, fweight), bg='yellow', activebackground='yellow', text='Submit', command=self.submit)
            self.submitBtn.place(relx=relx, rely=0.6, anchor=anchor)

    def submit(self):
        if (not self.verb8.get().isalpha()):
            self.missing.place(relx=0.5, rely=0.525, anchor='center')
        else:
            self.result = 'In the morning, I will ' + self.verb1.get() + ', ' + self.verb2.get() + ', and ' + self.verb3.get() + '. Later on I will go down to ' + self.noun1.get() + ' to ' + self.verb4.get() + '. After finishing my ' + self.noun2.get() + ', I will go to ' + self.noun3.get() + ' to ' + self.verb5.get() + '. It will took me ' + self.verb6.get() + ' to finish the ' + self.verb7.get() + '. After I finished, I will ' + self.verb8.get() + '.'
            self.answer = Label(self.main, font=('Sans-Serif 15 bold'), bg='white', text=self.result, wraplength=425, justify=LEFT)
            self.answer.place(relx=0.5, rely=0.5, anchor='center')
            self.missing.destroy()
            self.verb8Msg.destroy()
            self.verb8.destroy()
            self.submitBtn.destroy()
            self.repeatBtn = Button(self.main, font=('Sans-Serif 15 bold'), bg='Yellow', activebackground='Yellow', text='Play Again?', command=self.repeat)
            self.repeatBtn.place(relx=0.5, rely=0.9, anchor='center')

    def repeat(self):
        self.answer.destroy()
        self.repeatBtn.destroy()
        menu.MainMenu(self.main)
        