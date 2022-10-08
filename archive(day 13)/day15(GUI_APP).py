#GUI - Graphical User Interface
#libraries:
#1. Tkinter
#2. PyQT
#3. Turtle

import tkinter as ttk
app=ttk.Tk()

app.title('My App')
app.geometry('600x400')
ttk.Label(app, text='A simple Text Label').place(x=240,y=180)
ttk.Label(app, text="app made by MUDIT").place(x=240,y=200)

app.mainloop()