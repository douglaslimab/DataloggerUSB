from tkinter import *

temperature = 0

screen = Tk()
screen.title = "Datalogger"
screen.geometry("400x400")

def refresh():
    global timer
    print('.')
    label.configure(text=str(temperature))
    timer = screen.after(1000, refresh)


label = Label(screen, textvariable='')
label.pack()

btn = Button(screen, text="Refresh", command=refresh)
btn.pack()

screen.mainloop()
