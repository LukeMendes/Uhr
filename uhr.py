import tkinter as tk
from datetime import datetime


def update_time():
    current_time = datetime.now()
    time_display = current_time.strftime('%H:%M:%S')
    clock_label['text'] = time_display
    root.after(1000, update_time)  # Update every second (1000 ms)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Uhr")
    root.geometry("200x50")

    clock_label = tk.Label(root, text='')
    clock_label.pack()

    update_time()  # Start the timer

root.mainloop()  # Keep the window open and update the time continuously