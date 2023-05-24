#!/usr/bin/env python3

students = ["Alice", "Bob", "Charlie", "David", "Eve"]
number_of_columns = 4

from datetime import datetime
import tkinter as tk

def format_time(time):
    if time < 10:
        return f"0{time}"
    else:
        return str(time)

def update_time():
    global seconds, minutes, hours, running
    if running:
        seconds += 1
        if seconds == 60:
            seconds = 0
            minutes += 1
        time_string = f"{format_time(minutes)}:{format_time(seconds)}"
        display.config(text=time_string)
        root.after(1000, update_time)

def click_button(button):
    global running, active_button, seconds, minutes
    if seconds or minutes:  # if seconds or minutes is not 0, then log the name and time
        logThis = f"{button['text']},{minutes*60 + seconds},{datetime.now()}"
        with open('signout-log.csv', 'a') as logfile:
            logfile.write(logThis + '\n')
    seconds = 0
    minutes = 0
    display.config(text="00:00")
    if not running:
        running = True
        active_button = button
        for other_button in buttons:
            if other_button != button:
                other_button.config(state="disabled")
        update_time()
    else:
        running = False
        active_button = None
        for other_button in buttons:
            other_button.config(state="normal")

root = tk.Tk()
root.title("Student Break Timer")
root.geometry('1280x1024')
root.configure(background='white')

seconds = 0
minutes = 0
running = False
active_button = None

display = tk.Label(root, text="00:00", font=("Arial", 24), bg='white')
#display.pack()
display.grid(row=0, column=0, columnspan=number_of_columns)

'''
buttons = []
for i in range(len(students)):
    button = tk.Button(root, text=students[i], bg='white', command=lambda i=i: click_button(buttons[i]))
    button.pack()
    buttons.append(button)
'''
buttons = []
for i in range(len(students)):
    row = i // number_of_columns + 1
    col = i % number_of_columns
    button = tk.Button(root, text=students[i], bg='white', command=lambda i=i: click_button(buttons[i]))
    button.grid(row=row, column=col)
    buttons.append(button)

root.mainloop()