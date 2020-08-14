#! /usr/env/python

from tkinter import *
import parser
from math import factorial
from math import *

root = Tk()
root.title('Calculator')

# Current input position
i = 0


# Takes in variable and displays on input field
def get_variables(num):
    global i
    display.insert(i, num)
    i += 1


# Function that processes operators
def get_operation(op):
    global i
    length = len(op)
    display.insert(i, op)
    i += length


# Function that clears input field
def clear_all():
    display.delete(0, END)


# Function to undo previous action, like backspace
def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0, 'Error')


# Function to parse input and evaluate, returns calculation
def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, 'Error')


# Function to calculate factorial
def fact():
    entire_string = display.get()
    try:
        result = factorial(int(entire_string))
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, 'Error')


# -----------------------------------------------UI-----------------------------------------------

# Creates input field
display = Entry(root)
display.grid(row=1, columnspan=7, sticky=N+E+W+S)

# Creates number buttons
Button(root, text='1', command = lambda : get_variables(1)).grid(row=2, column=0, sticky=N+S+E+W)
Button(root, text='2', command = lambda : get_variables(2)).grid(row=2, column=1, sticky=N+S+E+W)
Button(root, text='3', command = lambda : get_variables(3)).grid(row=2, column=2, sticky=N+S+E+W)

Button(root, text='4', command = lambda : get_variables(4)).grid(row=3, column=0, sticky=N+S+E+W)
Button(root, text='5', command = lambda : get_variables(5)).grid(row=3, column=1, sticky=N+S+E+W)
Button(root, text='6', command = lambda : get_variables(6)).grid(row=3, column=2, sticky=N+S+E+W)

Button(root, text='7', command = lambda : get_variables(7)).grid(row=4, column=0, sticky=N+S+E+W)
Button(root, text='8', command = lambda : get_variables(8)).grid(row=4, column=1, sticky=N+S+E+W)
Button(root, text='9', command = lambda : get_variables(9)).grid(row=4, column=2, sticky=N+S+E+W)

# Clear and operator buttons
Button(root, text='AC', command = lambda : clear_all()).grid(row=5, column=0, sticky=N+S+E+W)
Button(root, text=' 0', command = lambda : get_variables(0)).grid(row=5, column=1, sticky=N+S+E+W)
Button(root, text=' .', command = lambda : get_variables('.')).grid(row=5, column=2, sticky=N+S+E+W)

Button(root, text='+', command = lambda : get_operation('+')).grid(row=2, column=3, sticky=N+S+E+W)
Button(root, text='-', command = lambda : get_operation('-')).grid(row=3, column=3, sticky=N+S+E+W)
Button(root, text='*', command = lambda : get_operation('*')).grid(row=4, column=3, sticky=N+S+E+W)
Button(root, text='/', command = lambda : get_operation('/')).grid(row=5, column=3, sticky=N+S+E+W)

# Add more operators
Button(root, text='pi', command = lambda : get_operation(str(pi))).grid(row=2, column=4, sticky=N+S+E+W)
Button(root, text='%', command = lambda : get_operation('%')).grid(row=3, column=4, sticky=N+S+E+W)
Button(root, text='(', command = lambda : get_operation('(')).grid(row=4, column=4, sticky=N+S+E+W)
Button(root, text='exp', command = lambda : get_operation('**')).grid(row=5, column=4, sticky=N+S+E+W)

Button(root, text='<-', command = lambda : undo()).grid(row=2, column=5, sticky=N+S+E+W)
Button(root, text='x!', command = lambda : fact()).grid(row=3, column=5, sticky=N+S+E+W)
Button(root, text=')', command = lambda : get_operation(')')).grid(row=4, column=5, sticky=N+S+E+W)
Button(root, text='^2', command = lambda : get_operation('**2')).grid(row=5, column=5, sticky=N+S+E+W)

Button(root, text='sqrt', command = lambda : get_operation('sqrt(')).grid(row=2, column=6, sticky=N+S+E+W)
Button(root, text='e', command = lambda : get_operation(str(e))).grid(row=3, column=6, sticky=N+S+E+W)
Button(root, text='|x|', command = lambda : get_operation('abs(')).grid(row=4, column=6, sticky=N+S+E+W)
Button(root, text='log', command = lambda : get_operation('log(')).grid(row=5, column=6, sticky=N+S+E+W)
Button(root, text='log10', command = lambda : get_operation('log10(')).grid(row=6, column=6, sticky=N+S+E+W)

Button(root, text='=', command = lambda : calculate()).grid(row=6, columnspan=6, sticky=N+S+E+W)


root.mainloop()