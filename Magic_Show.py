from tkinter import *
import random

root = Tk()
root.geometry("400x400")

word = Label(root)

def generate():
    alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    r1 = random.randint(0, 25)
    r2 = random.randint(0, 25)
    r3 = random.randint(0, 25)
    r4 = random.randint(0, 25)
    r5 = random.randint(0, 25)
    ra1 = alpha[r1]
    ra2 = alpha[r2]
    ra3 = alpha[r3]
    ra4 = alpha[r4]
    ra5 = alpha[r5]
    
    word["text"] = ra1 + ra2 + ra3 + ra4 + ra5

btn = Button(root, text="Magic Show", command=generate, bg="coral", fg="white", font=("comic sans MS", 15, "bold", "italic"))
btn.place(relx=0.5, rely=0.4, anchor=CENTER)

word.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()