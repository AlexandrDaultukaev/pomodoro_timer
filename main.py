from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1500
SHORT_BREAK_MIN = 300
LONG_BREAK_MIN = 1200
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    reps = 0
    text_timer.config(text="Pomodoro\nTimer", fg=GREEN)
    start_button["state"] = "normal"
    canvas.itemconfig(timer_text, text=f"00:00")
    check_mark.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    start_button["state"] = "disabled"
    global reps
    if reps == 0:
        check_mark.config(text="")
    reps += 1
    if reps < 9:
        if reps % 2 == 1:
            countdown(WORK_MIN)
            text_timer.config(text="\nWork", fg=GREEN)
        else:
            if reps == 8:
                countdown(LONG_BREAK_MIN)
                text_timer.config(text="Long\nBreak", fg=PINK)
            else:
                countdown(SHORT_BREAK_MIN)
                text_timer.config(text="\nBreak", fg=PINK)
    else:
        text_timer.config(text="Pomodoro\nTimer", fg=GREEN)
        check_mark.config(text="Done!", fg="olive drab", font=(FONT_NAME, 18, "bold"))
        reps = 0
        start_button["state"] = "normal"


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global timer
    count_min = int(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = "0" + str(count_sec)
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    if reps < 9 and count == 0:
        marks = ""
        for _ in range(reps):
            marks += "✔"
        check_mark.config(text=marks)
        check_mark.grid(column=1, row=3)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.minsize(500, 500)
window.maxsize(500, 500)
window.config(bg="bisque", padx=70, pady=10)

text_timer = Label(text="Pomodoro\nTimer", font=(FONT_NAME, 38, "bold"), fg=GREEN, bg="bisque")
text_timer.grid(column=1, row=0)

img = PhotoImage(file="tomato.png")
canvas = Canvas(width=250, height=250, bg="bisque", highlightthickness=0)
# peach puff; pale goldenrod; bisque
canvas.create_image(120, 125, image=img)
timer_text = canvas.create_text(120, 145, text="00:00", fill="white", font=(FONT_NAME, 26, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", bg="bisque", fg="tomato", highlightthickness=0, bd=0, font=("Arial", 15, "bold"),
                      command=start_timer, disabledforeground="salmon1", activeforeground="orange red",
                      activebackground="bisque")
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", bg="bisque", fg="tomato", highlightthickness=0, bd=0, font=("Arial", 15, "bold"),
                      disabledforeground="salmon1", activeforeground="orange red",
                      activebackground="bisque", command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark = Label(text="✔", font=(FONT_NAME, 18, "bold"), fg="olive drab", bg="bisque")

window.mainloop()
