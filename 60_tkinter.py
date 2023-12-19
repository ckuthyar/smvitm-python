from tkinter import *
from tkinter.ttk import *
from random import *
window1=Tk()
rand1=randint(0,5)
ifPressed=False
num1=0
def one():
    global ifPressed
    ifPressed=True
    global num1
    num1=1
    print("Congratulations")

def two():
    global ifPressed
    ifPressed=True
    global num1
    num1=2
    print("Sorry, this is wrong")

button3=Button(window1, text="click the button with the correct spelling")
button3.pack(ipadx=25, ipady=5)

button1=Button(window1, text="India", command=one)
button1.pack(ipadx=25, ipady=25)

button2=Button(window1, text="Indya", command=two)
button2.pack(ipadx=25, ipady=25)

mainloop()
