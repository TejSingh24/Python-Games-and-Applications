import math
import tkinter as tk


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
timer_clock = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer_clock)
    timer_label.config(text='Timer')
    canvas.itemconfig(timer_text, text='00:00')
    check_marks.config(text='')
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 1:
        timer_label.config(text='Work Time', fg=RED)
        count_down(work_sec)
    elif reps % 8 == 0:
        timer_label.config(text='Long Break', fg=PINK)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text='Short Break', fg=GREEN)
        count_down(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer_clock
        timer_clock = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ''
        for _ in range(math.floor(reps/2)):
            marks += '✓'
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title('Pomodoro')
window.config(padx=100, pady=100, bg=YELLOW)



#Timer
timer_label = tk.Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 34, 'bold'))
timer_label.grid(column=1, row=0)

#Canvas
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

tomato = tk.PhotoImage(file='app_brewery-365 days code\\pomodoro-start\\tomato.png')
canvas.create_image(100,112, image=tomato)
timer_text = canvas.create_text(100,130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
# count_down(5)

canvas.grid(column=1, row=1)


#start
start_button = tk.Button(text='Start', highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

#reset
reset_button = tk.Button(text='Reset', highlightthickness=0, command=reset)
reset_button.grid(column=2, row=2)

check_marks = tk.Label(text='', fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()