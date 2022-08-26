#!/usr/bin/env python3

from datetime import datetime
import csv

import tkinter as tk
import tkinter.font as font

# log program start time
with open('signout-log.csv', 'a') as logfile:
    logfile.write('Program Started' +','+ str(datetime.now()) + '\n')

def log_this(_):
    infoLabel.config(text='')
    now = datetime.now()
    student = inputbox.get(1.0, "end-1c").strip()
    if student == '':
        infoLabel.config(text='Please type your name')
    else:
        if button1.cget('text') == '':
            button1.config(text=student)
        elif button2.cget('text') == '':
            button2.config(text=student)
        elif button3.cget('text') == '':
            button3.config(text=student)
        else:
            infoLabel.config(text='Please wait')
        if infoLabel.cget('text') != 'Please wait':
            with open('signout-log.csv', 'a') as logfile:
                logfile.write(student + ',' + 'out' + ',' + str(now)  + '\n')
        inputbox.delete('1.0', "end-1c")
    inputbox.focus_set()

def button1_command():
    now = datetime.now()
    student = button1.cget('text')
    if student != '':
        with open('signout-log.csv', 'a') as logfile:
            logfile.write(student + ',' + 'in' + ',' + str(now)  + '\n')
    button1.config(text='')
    inputbox.focus_set()

def button2_command():
    now = datetime.now()
    student = button2.cget('text')
    if student != '':
        with open('signout-log.csv', 'a') as logfile:
            logfile.write(student + ',' + 'in' + ',' + str(now)  + '\n')
    button2.config(text='')
    inputbox.focus_set()

def button3_command():
    now = datetime.now()
    student = button3.cget('text')
    if student != '':
        with open('signout-log.csv', 'a') as logfile:
            logfile.write(student + ',' + 'in' + ',' + str(now)  + '\n')
    button3.config(text='')
    inputbox.focus_set()

window = tk.Tk()
window.title('Classroom Signout')
window.geometry('800x600')
window.configure(bg='white')
buttonfont = font.Font(size=50)

padding = 5
inputbox = tk.Text(window, height=1, width=25)
inputbox.bind('<Return>', log_this)
inputbox.focus_set()
inputbox.pack(pady=padding)
inputbutton = tk.Button(window, text='signout', command=lambda: log_this(''), bg='white')
inputbutton.pack(pady=padding)

button1 = tk.Button(window, text='', command=button1_command, font=buttonfont, bg='white')
button2 = tk.Button(window, text='', command=button2_command, font=buttonfont, bg='white')
button3 = tk.Button(window, text='', command=button3_command, font=buttonfont, bg='white')
button1.pack(pady=padding)
button2.pack(pady=padding)
button3.pack(pady=padding)
infoLabel = tk.Label(window, text='', bg='white')
infoLabel.pack(pady=padding)

window.mainloop()