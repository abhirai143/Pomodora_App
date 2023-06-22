from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    label_timer.config(text="Timer")
    canvas.itemconfig(text_timer, text="00:00")
    checkbox_label.config(text="")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def set_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        label_timer.config(text="Break", fg=RED)
        timer_countdown(long_break_sec)

    elif reps % 2 == 0:
        label_timer.config(text="Break", fg=PINK)
        timer_countdown(short_break_sec)
    else:
        label_timer.config(text="Work", fg=GREEN)
        timer_countdown(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

def timer_countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = "0"+f"{count_sec}"
    canvas.itemconfig(text_timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, timer_countdown, count - 1)
    else:
        set_timer()
        marks = ""
        work_session  = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✔"
            checkbox_label.config(text=marks)


label_timer = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=("Arial", 40, "bold"))
label_timer.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0 )
image_link = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image_link)
text_timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

button_start = Button(text="Start", highlightthickness=0, command=set_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
button_reset.grid(column=2, row=2)

checkbox_label = Label(text="", fg=GREEN, bg=YELLOW)
checkbox_label.grid(column=1, row=3)






window.mainloop()
