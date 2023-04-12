# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 09:00:39 2023

@author: Kshitij Soni
"""

from tkinter import*
import random

root=Tk()
root.geometry("400x400")
root.title("Doodle's realm of Magic")

canvas=Canvas(root, width=400, height=400)
canvas.configure(bg="#f3d151")

canvas.create_rectangle(0,0, 400, 50, fill="#ed1107")

Label_Heading=canvas.create_text(200,25, font=('times','27','bold'), fill="white", text="Magic Volunteer")
Label_text=Label(root)

Alpha=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
def Seat_no():
    Random1= random.randint(0, 25)
    print(Random1)
    Random2= random.randint(0, 25)
    Random3= random.randint(0, 25)
    Random4= random.randint(0, 25)
    Random5= random.randint(0, 25)
    Alpa1=Alpha[Random1]
    Alpa2=Alpha[Random2]
    Alpa3=Alpha[Random3]
    Alpa4=Alpha[Random4]
    Alpa5=Alpha[Random5]
    Seat=Alpa1 + Alpa2 + Alpa3 + Alpa4 + Alpa5
    print(Seat)
    Label_text["text"]=Seat 

Label=canvas.create_window(200, 150, anchor=CENTER, window=Label_text)


Button1=Button(root, text="Who is Lucky?", command= Seat_no)
Button1.configure(activebackground="#40cb3f", bg="#3ea4c9", font=('times','15','bold'), width=10)
button=canvas.create_window(200, 250, anchor=CENTER, window=Button1)

canvas.pack()
root.mainloop()
canvas_ex.py