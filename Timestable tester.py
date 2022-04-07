
import random
from tkinter import *

class GUI:
    def __init__(self,parent):

        main = Frame(parent)
        T1 = Times_Table()
        

        Label(main,text = T1.timestable_randomizer()).grid(column=0,row=0,sticky=W,pady=5)
        main.grid()
        
        

        


class Times_Table:
    def __init__(self, min = 0, max = 20):
        self.min = min
        self.max = max 

        
    def timestable_randomizer(self): 
        self.number = random.sample(range(self.min,self.max),2)
        return self.number
    

    def check_answer(self):
        answer = self.number[0] * self.number[1]


    #def next(self):
        




if __name__ == "__main__":
    root = Tk()
    buttons = GUI(root)
    root.mainloop()
