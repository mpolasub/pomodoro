from tkinter import *

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
    reps = 0
    canvas.itemconfig(timer_num, text="00:00")
    timer_text.config(text="Timer", fg=GREEN)
    check_text.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        time = work_sec
        timer_text.config(text="Work", fg=GREEN)
    elif reps == 2 or reps == 4 or reps == 6:
        time = short_break_sec
        timer_text.config(text="Break", fg=PINK)
    else:
        time = long_break_sec
        timer_text.config(text="Break", fg=RED)

    count_down(time)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    mins = count // 60
    secs = count % 60
    if secs < 10:
        secs = f"0{secs}"

    canvas.itemconfig(timer_num, text=f"{mins}:{secs}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        check = ""
        for n in range(0, reps // 2):
            check += "✔"
        check_text.config(text=check)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_num = canvas.create_text(100, 139, text="00:00", fill="white", font=(FONT_NAME, 36, "bold"))
canvas.grid(column=1, row=1)

timer_text = Label(text="Timer", font=(FONT_NAME, 36, "bold"), fg=GREEN, bg=YELLOW)
timer_text.grid(column=1, row=0)

check_text = Label(fg=GREEN, bg=YELLOW)
check_text.grid(column=1, row=3)

start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(column=2, row=2)

window.mainloop()
