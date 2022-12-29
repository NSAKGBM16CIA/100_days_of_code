from tkinter import *
"""
buttons= ['q','w','e','r','t','y','u','i','o','p',
          'a','s','d','f','g','h','j','k','l',
          'z','x','c','v','b','n','m']
rows = 3
cols = 0

sentence = ""

def write(value):
    global sentence
    value = value
    if value == 'Space':
        value = ' '
        entry.insert(END, value)
    else:
        entry.insert(END, value)
    sentence += sentence+value


for button in buttons:
    command = lambda x=button: write(x)

    if button =='Space':
        Button(window, text=button, command=command).grid(row=5, column=cols)
    else:
        Button(text=button, command=command, width=5, font=("Arial", 14, 'bold'), bg="blue",
               padx=3.5, pady=3.5, bd=5).grid(row=rows, column=cols)
    cols += 1
    if cols > 9  and rows == 3:
        cols = 0
        rows += 1
    if cols > 8 and rows == 4:
        cols = 0
        rows += 1


"""