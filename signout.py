#!/usr/bin/env python3

import datetime
import csv

#from tkinter import ttk
#from tkinter import *
#from tkinter.ttk import *

import tkinter as tk
from tkinter import ttk

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


def log_this(student):
    print(student)

#style = ttk.Style()
#style.configure('BW.TLabel', foreground='black', background='white')
#l1 = ttk.Label(text="Test", style="BW.TLabel")

root = tk.Tk()
root.title('Classroom Signout')

ttk.Label(root, text='Students').pack()

#ttk.Button(root, text=student, command=lambda: log_this(student)).pack()

root.mainloop()