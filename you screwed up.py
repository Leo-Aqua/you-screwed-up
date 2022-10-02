from random import randint
from tkinter import *
def messageWindow():
    for i in range(randint(5,100)):
        win = Toplevel()
        win.geometry(f'+{randint(0,1920)}+{randint(0,1080)}')
        win.title('warning')
        message = "You screwed up"
        Label(win, text=message).pack()
        Button(win, text='Ok', command=messageWindow).pack()
        win.protocol("WM_DELETE_WINDOW", messageWindow)
        win.attributes("-topmost", True)  
root = Tk()
root.title('warning')
root.protocol("WM_DELETE_WINDOW", messageWindow)
Label(root, text='You Screwed up').pack()
Button(root, text='Ok', command=messageWindow).pack()
root.attributes("-topmost", True)
root.mainloop()