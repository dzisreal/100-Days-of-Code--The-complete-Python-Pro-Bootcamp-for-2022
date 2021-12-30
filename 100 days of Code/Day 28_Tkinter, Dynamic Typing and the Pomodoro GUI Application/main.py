from tkinter import *
import os
import time
os.chdir("C:/Users/Admin/Desktop/100 days of Code/Day 28_Tkinter, Dynamic Typing and the Pomodoro GUI Application")
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25*60
SHORT_BREAK_MIN = 5*60
LONG_BREAK_MIN = 20*60
reps = 1
marks = ""
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_mark_label.config(text="")
    global reps
    reps = 1

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN)
        title_label.config(text="Break", fg=RED)
    elif reps%2:
        count_down(WORK_MIN)
        title_label.config(text="Work", fg=GREEN)
    else:
        count_down(SHORT_BREAK_MIN) 
        title_label.config(text="Break", fg=PINK)
    reps+=1
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global timer
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0: 
        timer = window.after(1000, count_down, count - 1)
    else:
        global marks
        start_timer()
        if reps%2:
            marks+="✔"
        check_mark_label.config(text=marks)
 
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg=YELLOW)


title_label = Label(text = "Timer", fg=GREEN, font = (FONT_NAME,45), bg=YELLOW)
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=1)

start_button = Button(text="Start", highlightthickness=0,command=start_timer)
start_button.grid(column=0, row=2)

check_mark_label = Label(fg=GREEN, font=(FONT_NAME,25), bg=YELLOW)
check_mark_label.grid(column=1, row=3)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)


window.mainloop()