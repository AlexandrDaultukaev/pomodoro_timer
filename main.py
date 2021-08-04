from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 3
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 7
reps = 1


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    start_button["state"] = "disabled"
    global reps

    if reps % 2 == 1:
        countdown(WORK_MIN)
    else:
        if reps == 8:
            countdown(LONG_BREAK_MIN)
        else:
            countdown(SHORT_BREAK_MIN)
    reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global reps
    min = int(count / 60)
    sec = count % 60
    if sec < 10:
        sec = "0" + str(sec)
    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
        window.after(1000, countdown, count - 1)
    if reps < 9 and count == 0:
        check_marks[reps - 2].place(x=48 + (reps - 2) * 35, y=430)
        window.after(1000, start_timer)
    elif reps == 9 and count == 0:
        check_marks[reps - 2].place(x=48 + (reps - 2) * 35, y=430)
        start_button["state"] = "normal"




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
                      activebackground="bisque")
reset_button.grid(column=2, row=2)

check_marks = []
for i in range(8):
    check_marks.append(Label(text="✔", font=(FONT_NAME, 18, "bold"), fg="olive drab", bg="bisque"))

window.mainloop()
