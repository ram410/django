
from tkinter import *
def main ():
    root=Tk()
    app=Window1(root)
    
class Window1:
    def __init__(self,master):
        self.master=master
        self.master.title("Testing Part")
        self.master.geometry("500x300+0+0")
        self.username=Label(text="USERNAME")
        self.username.grid(row=0,column=0)
        self.username=Entry()
        self.username.grid(row=0,column=1)
        self.password=Label(text="PASSWORD")
        self.password.grid(row=1,column=0)
        self.password=Entry()
        self.password.grid(row=1,column=1)


main()

