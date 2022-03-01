import random
from tkinter import *
from PIL import ImageTk, Image

# Create App Layout
Lottery = Tk()
Lottery.geometry('800x360')
Lottery.title('Lottery Number Generator')
Lottery.iconbitmap("ticket.ico")

# Define button Command
def Lotto_No():
	q = random.randint(1,9999);
	w = random.randint(1,9999);
	e = random.randint(1,9999);
	r = random.randint(1,9999);
	t = random.randint(1,9999);
	y = random.randint(1,9999);
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

# Difine The  Title
var = StringVar()
var.set("Lottery Numbers Generator")

# Make The First Main Frame (Lottery)
frame = Frame(Lottery)
frame.pack()
frame1 = Frame(Lottery)
frame1.pack(side = TOP)

# Add image file
bg = PhotoImage( file = "bg3.png")
  
# Show image using label
label1 = Label(Lottery, image = bg, width=800, height=360)
label1.place(x = 0,y = 1)

# Make a Label For the Title
label = Label(frame1, textvariable=var, font=("Arial", 48), width= 24, bd=0, highlightthickness=0)
label.pack(side = TOP)
label = Label(frame1, textvariable="", width= 24,)
label.pack(side = TOP)
label = Label(frame1, textvariable="", width= 24)
label.pack(side = TOP)

# Making a 2de Frame for the numbers
frame2 = Frame(Lottery)
frame2.pack(side = TOP)

# Displaying the Numbers inside the Frame
txtDisplay = Entry(frame2, textvariable = num1, bd=20, insertwidth=1, font=("Arial", 20), justify='center', width=4, highlightthickness=0, bg="black", fg="white")
txtDisplay.pack(side = LEFT)
txtDisplay = Entry(frame2, textvariable = num2, bd=20, insertwidth=1, font=("Arial", 20), justify='center', width=4, highlightthickness=0, bg="black", fg="white")
txtDisplay.pack(side = LEFT)
txtDisplay = Entry(frame2, textvariable = num3, bd=20, insertwidth=1, font=("Arial", 20), justify='center', width=4, highlightthickness=0, bg="black", fg="white")
txtDisplay.pack(side = LEFT)
txtDisplay = Entry(frame2, textvariable = num4, bd=20, insertwidth=1, font=("Arial", 20), justify='center', width=4, highlightthickness=0, bg="black", fg="white")
txtDisplay.pack(side = LEFT)
txtDisplay = Entry(frame2, textvariable = num5, bd=20, insertwidth=1, font=("Arial", 20), justify='center', width=4, highlightthickness=0, bg="black", fg="white")
txtDisplay.pack(side = LEFT)
txtDisplay = Entry(frame2, textvariable = num6, bd=20, insertwidth=1, font=("Arial", 20), justify='center', width=4, highlightthickness=0, bg="black", fg="white")
txtDisplay.pack(side = LEFT)

# Making a 3th Frame for the Button
frame3 = Frame(Lottery)
frame3.pack(side = TOP)

# Placing the Buttons Inside The Frame
button1 = Button(frame3, padx=8, width=18, relief="flat", fg="red", bg="black", borderwidth=0, font=("Arial", 26), text = "Generator", command=Lotto_No)
button1.pack(side = TOP, padx=0, pady=0, )

Lottery.mainloop()
