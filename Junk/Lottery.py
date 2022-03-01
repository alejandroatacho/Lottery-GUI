import random
from tkinter import *
from PIL import ImageTk, Image

Lottery = Tk()
Lottery.geometry('800x700')
Lottery.title('Lottery Number Generator')
Lottery.iconbitmap("ticket.ico")

# Define button Command


def Lotto_No():
    q = random.randint(1, 9999)
    w = random.randint(1, 9999)
    e = random.randint(1, 9999)
    r = random.randint(1, 9999)
    t = random.randint(1, 9999)
    y = random.randint(1, 9999)
    num1.set(q)
    num2.set(w)
    num3.set(e)
    num4.set(r)
    num5.set(t)
    num6.set(y)
    return


num1 = StringVar()
num2 = StringVar()
num3 = StringVar()
num4 = StringVar()
num5 = StringVar()
num6 = StringVar()


Lottery.mainloop()
