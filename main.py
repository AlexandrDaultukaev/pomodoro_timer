from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

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


# ---------------------------- SETTINGS ------------------------------- #
def close_set(setting):
    """
    Activates start and settings button when settings window closed
    """
    start_button["state"] = "normal"
    settings_button["state"] = "normal"
    setting.destroy()


def set_apply(work, short, long):
    """Sets work and breaks time"""
    global WORK_MIN, SHORT_BREAK_MIN, LONG_BREAK_MIN
    try:
        work = int(work)
        short = int(short)
        long = int(long)
    except ValueError:
        messagebox.showerror(title="Error", message="Enter only numbers!")
    else:
        WORK_MIN = work * 60
        SHORT_BREAK_MIN = short * 60
        LONG_BREAK_MIN = long * 60


def settings():
    """Sets up work settings window"""
    start_button["state"] = "disabled"
    settings_button["state"] = "disabled"

    setting = Toplevel(window)
    setting.maxsize(500, 500)
    setting.minsize(500, 500)
    setting.title("Settings")
    setting.config(bg="coral1", padx=70, pady=10)
    image = Image.open("tomato.png")
    resized_image = image.resize((125, 125))
    imag = ImageTk.PhotoImage(resized_image)
    image_label = Label(setting, image=imag)
    image_label.config(bg="coral1")
    image_label.place(x=120, y=55)

    work_min = Entry(setting, font=(FONT_NAME, 18, "bold"), width=5, bg="salmon1", highlightthickness=0, bd=0)
    work_min.insert(END, string=str(int(WORK_MIN / 60)))
    work_min_text = Label(setting, font=(FONT_NAME, 18, "bold"), text="WORK\nmin", bg="coral1")
    work_min.place(x=10, y=210)
    work_min_text.place(x=10, y=250)

    break_min = Entry(setting, font=(FONT_NAME, 18, "bold"), width=5, bg="salmon1", highlightthickness=0, bd=0)
    break_min.insert(END, string=str(int(SHORT_BREAK_MIN / 60)))
    break_min_text = Label(setting, font=(FONT_NAME, 18, "bold"), text="BREAK\nmin", bg="coral1")
    break_min.place(x=145, y=210)
    break_min_text.place(x=145, y=250)

    long_break_min = Entry(setting, font=(FONT_NAME, 18, "bold"), width=5, bg="salmon1", highlightthickness=0,
                           bd=0)
    long_break_min.insert(END, str(int(LONG_BREAK_MIN / 60)))
    long_break_min_text = Label(setting, font=(FONT_NAME, 18, "bold"), text="LONG BREAK\nmin", bg="coral1")
    long_break_min.place(x=280, y=210)
    long_break_min_text.place(x=250, y=250)

    apply_button = Button(setting, text="Apply", bg="coral1", fg="white", highlightthickness=0, bd=0, font=("Arial", 15, "bold"),
                          disabledforeground="salmon1", activeforeground="orange red",
                          activebackground="bisque", command=lambda: set_apply(work_min.get(), break_min.get(),
                                                                               long_break_min.get()))
    apply_button.place(x=150, y=400)
    setting.protocol("WM_DELETE_WINDOW", lambda: close_set(setting))
    setting.mainloop()


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    """Resets timer and check marks to zero"""
    global reps
    window.after_cancel(timer)
    reps = 0
    text_timer.config(text="Pomodoro\nTimer", fg=GREEN)
    start_button["state"] = "normal"
    settings_button["state"] = "normal"
    reset_button["state"] = "disabled"
    canvas.itemconfig(timer_text, text=f"00:00")
    check_mark.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """Activates timer"""
    settings_button["state"] = "disabled"
    start_button["state"] = "disabled"
    reset_button["state"] = "normal"
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
        settings_button["state"] = "normal"
        start_button["state"] = "normal"


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    """Sets up countdown mechanism and changes numbers in timer every second"""
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
                      activebackground="bisque", command=reset_timer, state="disabled")
reset_button.grid(column=2, row=2)

settings_button = Button(text="Settings", bg="bisque", fg="tomato", highlightthickness=0, bd=0, font=("Arial", 15, "bold"),
                         disabledforeground="salmon1", activeforeground="orange red",
                         activebackground="bisque", command=settings)
settings_button.place(x=-50, y=20)

check_mark = Label(text="✔", font=(FONT_NAME, 18, "bold"), fg="olive drab", bg="bisque")

window.mainloop()
