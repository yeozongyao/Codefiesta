from tkinter import *
import os
import tkinter
from tkinter import simpledialog
root = Tk()



def rentorbuy():
    USER_INP = simpledialog.askstring(title="Test",
    prompt="Are you looking to rent or buy")

    agentmatch = Label(root, text = "You have been matched with Alice, a verified agent from Propnex! Thank you!")
    agentmatch.pack()
    
def myClick1():
    USER_INP = simpledialog.askstring(title="Test",
    prompt="What's your Name and Where are you residing currently? Eg. Zong Yao USA California:")
    userinfo = USER_INP.split()

    rentorbuy()

def findjob():
    USER_INP1 = simpledialog.askstring(title="Test",
    prompt="In which sector are you looking for a job?")
    

    companyfound = Label(root, text = "You have been matched wtih Microsoft, a leading company in the " + USER_INP1 + " sector. Good luck!")
    companyfound.pack()

def myClick2():

    USER_INP3 = simpledialog.askstring(title="Test",
    prompt="What's your Name and Where are you residing currently? Eg. Zong Yao USA California:")
    userinfo3 = USER_INP3.split()

    findjob()

def schoolinfo():
    USER_INP5 = simpledialog.askstring(title="Test",
    prompt ="You have been enrolled into Greenwood Primary School! Please update on your date of matriculation: (Eg. 20 February 2021")

    finalupdate = Label(root, text="Thank you your update. We look forward to see you on "+ USER_INP5)
    finalupdate.pack()

def findschool():
    USER_INP5 = simpledialog.askstring(title="Test",
    prompt ="For what age are you looking for an education in?:")

    schoolinfo()

def myClick3():
    USER_INP4 = simpledialog.askstring(title="Test",
    prompt = "What's your Name and Where are you residing currently? Eg. Zong Yao USA California:")

    findschool()

    

accomodationbutton = Button(root, text = "Accomodation", padx=100, pady=80, command=myClick1)
accomodationbutton.pack()

jobbutton = Button(root, text = "Jobs", padx=125, pady=85, command = myClick2)
jobbutton.pack()

educationbutton = Button(root, text = "Education", padx = 110, pady=85, command = myClick3)
educationbutton.pack()














root.mainloop()