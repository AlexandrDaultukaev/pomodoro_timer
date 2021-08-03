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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

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
canvas.create_text(120, 145, text="00:00", fill="white", font=(FONT_NAME, 26, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", bg="bisque", fg="tomato", highlightthickness=0, bd=0, font=("Arial", 15, "bold"))
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", bg="bisque", fg="tomato", highlightthickness=0, bd=0, font=("Arial", 15, "bold"))
reset_button.grid(column=2, row=2)

check_mark = Label(text="✔", font=(FONT_NAME, 18, "bold"), fg="olive drab", bg="bisque")
check_mark.grid(column=1, row=3)

window.mainloop()
