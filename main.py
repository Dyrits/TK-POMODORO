from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#E2979C"
RED = "#E7305B"
GREEN = "#9BDEAC"
YELLOW = "#F7F5DD"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 60

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global repetitions
    global counter
    repetitions = 0
    window.after_cancel(counter)
    title.config(text="Ready?", fg=GREEN)
    checkmark.grid_forget()
    canvas.itemconfig(timer, text="...")
    checkmark.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global repetitions
    global checkmarks
    if repetitions % 2 == 0:
        title.config(text="Work!", fg=GREEN)
        count_down(WORK_MIN * 60)
    elif repetitions % 8 == 0:
        title.config(text="Break!", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
        checkmark.grid_forget()
    else:
        title.config(text="Break!", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
        checkmarks.append("✔")
        checkmark.config(text="".join(checkmarks))
        checkmark.grid(column=1, row=2)
    repetitions += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global counter
    time = "{:02d}:{:02d}".format(*divmod(count, 60))
    canvas.itemconfig(timer, text=f"{time}")
    if count > 0:
        counter = window.after(1000, count_down, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

repetitions = 0
counter = ""

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title = Label(text="Ready?", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
title.grid(column=1, row=0)

tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=205, height=230, bg=YELLOW, highlightthickness=0)
canvas.create_image(105, 115, image=tomato_img)
timer = canvas.create_text(105, 140, text=f"...", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start = Button(text="Start", highlightthickness=0, fg=GREEN, font=(FONT_NAME, 12, "bold"), padx=10, pady=5,borderwidth=2)
start.grid(column=0, row=2)
start.config(command=start_timer)

reset = Button(text="Reset", highlightthickness=0, fg=RED, font=(FONT_NAME, 12, "bold"), padx=10, pady=5,borderwidth=2)
reset.grid(column=2, row=2)
reset.config(command=reset_timer)

checkmarks = []
checkmark = Label(text="", fg=GREEN, bg=YELLOW)

window.mainloop()