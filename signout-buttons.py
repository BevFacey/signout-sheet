#!/usr/bin/env python3

from datetime import datetime
import csv

import tkinter as tk
from tkinter import ttk
from turtle import color

# log program start time
with open('signout-log.csv', 'a') as logfile:
    logfile.write('Program Started' +','+ str(datetime.now()) + '\n')

# read CSV file in the format  Name,Period
period3_students = []
period4_students = []
with open('students.csv') as csvfile:
    r = csv.reader(csvfile, delimiter=',')
    for row in r:
        if row[0].lower() != 'name':
            student = row[0]
            period = int(row[1])
            if period == 3:
                period3_students.append(student)
            else:
                period4_students.append(student)

def log_this(i):
    student = period3_students[i]
    now = datetime.now()
    label = labels[i]
    label_text = label.cget('text')
    if label_text == 'out':
        label.config(text='in', fg='black')
    else:
        label.config(text='out', fg='red')
    print(student, label.cget('text'), now)
    with open('signout-log.csv', 'a') as logfile:
        logfile.write(student + ',' + str(now)  + '\n')

window = tk.Tk()
window.title('Classroom Signout')

# add buttons and labels
padding = 5
labels = []
for n, student in enumerate(period3_students):
    button = tk.Button(window, text=student, command=lambda i=n: log_this(i))
    button.grid(row=n, column=1, padx=padding, pady=padding)
    label = tk.Label(window, text='out', fg='red')
    labels.append(label)
    label.grid(row=n, column=2, padx=padding, pady=padding)
     
window.mainloop()