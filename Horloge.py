from tkinter import * 
import time



class Timer():
    def __init__(self):
        self.root = Tk()
        self.root.title("Horloge")
        self.label = Label(text="", font=('Arial', 100),foreground='red',background='black')
        self.label.pack()
        self.updateClock()
        self.root.mainloop()
        self.root
        



    def updateClock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text = now)
        self.root.after(1000, self.updateClock)

kais = Timer()