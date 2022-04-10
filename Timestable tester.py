
import random
from tkinter import *

class GUI:
    def __init__(self, parent):

        
        main = Frame(parent)
        main.grid()


        self.T1 = Times_Table()
        numbers_list = self.T1.timestable_randomizer()
        
        Label(main,text = "{} * {}".format(numbers_list[0],numbers_list[1])).grid(column=0,row=0,sticky=E,pady=10)

        
        self.user_entry = Entry(main)
        self.user_entry.grid(column=1,row=0,sticky=W,pady=10,padx=5)
       
        
        Button(main,text="Check Answer", command = self.display).grid(column=0,row=1,sticky=E,padx=10,pady=5)
        
        Button(main,text="Next").grid(column=1,row=1,sticky=E,pady=5,padx=10)
       

    def display(self):
        Label(text=self.T1.check_answer(self.user_entry.get())).grid(column=0,row=3,sticky=E,padx=10,pady=5)

    
        
        
         
        




class Times_Table:
    def __init__(self, min = 0, max = 20):
        self.min = min
        self.max = max 
        

        
    def timestable_randomizer(self): 
        self.number = random.sample(range(self.min,self.max),2)
        return self.number
    

    def check_answer(self,user_answer):
        self.user_answer = user_answer
        self.answer = self.number[0] * self.number[1]
        print(self.answer)

        try:
            user_answer = int(user_answer)
            if self.answer == user_answer:
                self.display = " CORRECT "
                return self.display

            else:
                self.display = "INCORRECT"
                return self.display

        except:
            return "INCORRECT"
            




    #def next(self):
        




root = Tk()
root.title("Times Table tester")
GUI(root)
root.mainloop()
