from tkinter import *
import time

root = Tk()

def task():
    print("hello")

    root.after(2000, task)  # reschedule event in 2 seconds
    for i in range(10):
        time.sleep(1.5)
        print(i)

root.after(2000, task)
root.mainloop()