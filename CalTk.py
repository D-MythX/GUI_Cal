#!/usr/bin/env python3
#Title: Calculator
#Author: MYTH

import tkinter as tk
import time
from tkinter import * 

def delete():
    mistake = input.get()[:-1]
    input.set(mistake)
      
def clear():
    error = input.get()
    input.set("")

def text_insert(text):
    current = input.get()
    input.set(current + str(text))
    
def evaluate():
    eqn = input.get()
    try:
        result = str(eval(eqn))
        time.sleep(0.3)
        input.set(result)
    except SyntaxError:
        time.sleep(1.0)
        input.set("SyntaxERROR")

cal = tk.Tk()
cal.title("Calculator")
cal.geometry("400x400")
cal.resizable(False, False)

input = StringVar()

title = tk.Label(cal, text="Calculator",  font=("Times New Roman", 10, "bold"), background="black", fg="white")
title.place(x=150)

display = tk.Entry(cal, bd=5, textvariable= input, justify=RIGHT, width=20, font=("Times New Roman", 10)).place(x=30, y=50)

seven = tk.Button(cal, text="7", command = lambda:text_insert(7), bd=2, bg="gray").place(y=120)

eight = tk.Button(cal, text="8", command = lambda:text_insert(8), bd=2, bg="gray").place(x=100, y=120)

nine = tk.Button(cal, text="9", command = lambda:text_insert(9), bd=2, bg="gray").place(x=200, y=120)

delete = tk.Button(cal, text="Del", command=delete, width=1, height=1, bd=2, bg="yellow", fg="red", activebackground="red", activeforeground="yellow").place(x=300, y=120)

ac = tk.Button(cal, text="AC", command=clear, width=1, height=1, bd=2, bg="yellow", fg="red", activebackground="red", activeforeground="yellow").place(x=400, y=120)

four = tk.Button(cal, text="4", command = lambda:text_insert(4), bg="gray", bd=2).place(y=200)

five = tk.Button(cal, text="5", command = lambda:text_insert(5), bg="gray", bd=2).place(x=100, y=200)

six = tk.Button(cal, text="6", command = lambda:text_insert(6), bg="gray", bd=2).place(x=200, y=200)

mul = tk.Button(cal, text="×", command = lambda:text_insert("*"), bg="lightgreen", bd=2).place(x=300, y=200)

div = tk.Button(cal, text="÷", command = lambda:text_insert("/"), bg="lightgreen", bd=2).place(x=400, y=200)

one = tk.Button(cal, text="1", command = lambda:text_insert(1), bg="gray", bd=2).place(y=280)

two = tk.Button(cal, text="2", command = lambda:text_insert(2), bg="gray", bd=2).place(x=100, y=280)

three = tk.Button(cal, text="3", command = lambda:text_insert(3), bg="gray", bd=2).place(x=200, y=280)

plus = tk.Button(cal, text="+", command= lambda:text_insert("+"), bg="lightgreen", bd=2).place(x=300, y=280)

minus = tk.Button(cal, text="-", command = lambda:text_insert("-"), width=1, height=1, bg="lightgreen", bd=2).place(x=400, y=280)

zero = tk.Button(cal, text="0", command = lambda:text_insert(0), bg="gray", bd=2).place(y=360)

dot = tk.Button(cal, text=".", command = lambda:text_insert("."), bg="gray", bd=2).place(x=100, y=360)

equalTo = tk.Button(cal, text="=", command = evaluate, bg="yellow", fg="red", activebackground="blue", activeforeground="white", bd=2).place(x=200, y=360)

openBrac = tk.Button(cal, text="(", command = lambda:text_insert("("), bg="lightgreen", bd=2).place(x=300, y=360)

closeBrac = tk.Button(cal, text=")", command = lambda:text_insert(")"), bg="lightgreen", bd=2).place(x=400, y=360)

exit = tk.Button(cal, text="EXIT", fg="white",  command=quit, bg="red", bd=2).place(x=350, y=440) 

cal.configure(background = "black")
cal.maxsize(400,400)
cal.minsize(400,400)
cal.mainloop()