import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
ORANGE = "#F57328"
RED = "#CC3636"
GREEN = "#367E18"
YELLOW = "#FFE9A0"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
reps = 0
timer = None


def reset_clicked():
    print("Reset clicked")
    global reps
    reps = 0
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="25:00")
    check_label.config(text="")


def start_clicked():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="BREAK", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="BREAK", fg=ORANGE)
    else:
        count_down(work_sec)
        timer_label.config(text="WORK", fg=GREEN)


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_clicked()
        if reps % 2 == 0:
            mark = ""
            work_sessions = math.floor(reps / 2)
            for i in range(work_sessions):
                mark += check_mark
            check_label.config(text=mark)




window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_pic = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_pic)
timer_text = canvas.create_text(100, 130, text="25:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

timer_label = tkinter.Label(text="Timer", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(column=2, row=1)

check_mark = '✔'
check_label = tkinter.Label(font=(FONT_NAME, 20, "bold"), bg=YELLOW, fg=GREEN)
check_label.grid(column=2, row=4)

start_button = tkinter.Button(text="Start", command=start_clicked)
start_button.grid(column=1, row=3)

reset_button = tkinter.Button(text="Reset", command=reset_clicked)
reset_button.grid(column=3, row=3)












window.mainloop()
