
import random
from tkinter import *

#GUI class that the user interacts with 
class GUI:
    def __init__(self, parent):

        
        self.main = Frame(parent)
        self.main.grid()


        self.T1 = Processing()
        
        self.numbers_list = self.T1.timestable_randomizer()

    
        self.question = Label(self.main,text = "{} * {}".format(self.numbers_list[0],self.numbers_list[1]))
        self.question.grid(column=0,row=0,sticky=E,pady=10)
        
        
        self.user_entry = Entry(self.main)
        self.user_entry.grid(column=1,row=0,sticky=W,pady=10,padx=5)
       
        
        Button(self.main,text="Check Answer", command = self.display).grid(column=0,row=1,sticky=E,padx=10,pady=5)
        
        self.next = Button(self.main,text="Next", command= self.new_main)
        self.next.grid(column=1,row=1,sticky=E,pady=5,padx=10)

#display if the user's answer is correct or incorrect
    def display(self):
        try:
            self.display_label.configure(text="")
            
        except:
            pass
        self.display_label=Label(text=self.T1.check_answer(self.user_entry.get()))
        self.display_label.grid(column=0,row=3,sticky=E,padx=10,pady=5)

#resets everything and display a new question
    def new_main(self):
        
        self.numbers_list = self.T1.timestable_randomizer()
        self.question.configure(text = "{} * {}".format(self.numbers_list[0],self.numbers_list[1]))

        self.user_entry.delete(0, END)

        try:
            self.display_label.configure(text="")
            
        except:
            pass
       
        
        
        
        
         
        



#this class is to process and return the data sent over by the GUI class
class Processing:
    def __init__(self, min = 0, max = 12):
        self.min = min
        self.max = max 
        

    #get 2 random numbers for the question
    def timestable_randomizer(self): 
        self.number = random.sample(range(self.min,self.max),2)
        return self.number
    
    #check if user's answer is correct then return the result
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
            





    
#main routine
root = Tk()
root.title("Times Table tester")
GUI(root)
root.mainloop()
