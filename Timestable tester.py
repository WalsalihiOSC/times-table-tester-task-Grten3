import random
from tkinter import *

class GUI:
    def __init__(self,parent):

        main = Frame(parent)
        self.T1 = Times_Table()
        numbers_list = self.T1.timestable_randomizer()
        main.grid()
        Label(main,text = "{} * {}".format(numbers_list[0],numbers_list[1])).grid(column=0,row=0,sticky=E,pady=10)

        self.entry() 
        self.verify()
        self.next()

    def entry(self):
        self.user_entry = Entry(width= 20).grid(column=1,row=0,sticky=W,pady=10,padx=5)
        return self.user_entry


    def verify(self):
        Button(text="Check Answer", command = self.T1.check_answer).grid(column=0,row=1,sticky=E,padx=10,pady=5)
        Label(text="    ").grid(column=1,row=2)

    def next(self):
        Button(text="Next").grid(column=1,row=1,sticky=E,pady=5,padx=10)
        




class Times_Table:
    def __init__(self, min = 0, max = 20):
        self.min = min
        self.max = max 
        self.user_answer = GUI.entry()

        
    def timestable_randomizer(self): 
        self.number = random.sample(range(self.min,self.max),2)
        return self.number
    

    def check_answer(self):
        answer = self.number[0] * self.number[1]

        if answer == self.user_answer:
            


    #def next(self):
        




if __name__ == "__main__":
    root = Tk()
    buttons = GUI(root)
    root.mainloop()
