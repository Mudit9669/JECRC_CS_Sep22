import tkinter as ttk
from unittest import result
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from PIL import ImageTk,Image

data = pd.read_csv('treadmil-users.csv')

app=ttk.Tk()
app.geometry('600x300')
app.title('Treadmil User Analysis')

graphs=ttk.Variable(app)
values=['Select'] + list(data.columns)
value={'Pair Plot':'sns.pairplot(data = data)',
        'Joint Plot':"sns.jointplot(data = data,x='{col1}',y='{col2}')",
        'Bar Plot':"sns.barplot(data = data,x='{col1}',y='{col2}')",
        'Box Plot':"sns.boxplot(data = data,x='{col1}',y='{col2}')"
        }
graphs.set('Pair Plot')
y=10
for key,value in value.items():
    ttk.Radiobutton(app,text=key,variable=graphs,value=value).place(x=10,y=y)
    y += 20
## option menu
# option 1
col1 = ttk.Variable(app)
col1.set(values[0])
ttk.Label(app,text='Column 1').place(x=150,y=10)
ttk.OptionMenu(app,col1, *values).place(x=150,y=40)

col2 = ttk.Variable(app)
col2.set(values[0])
ttk.Label(app,text='Column 2').place(x=150,y=80)
ttk.OptionMenu(app,col2, *values).place(x=150,y=110)

col3 = ttk.Variable(app)
col3.set(values[0])
ttk.Label(app,text='Column 3').place(x=150,y=150)
ttk.OptionMenu(app,col3, *values).place(x=150,y=180)

# CANVAS
cnv=ttk.Canvas(app,width=250,height=200)
cnv.place(x=300,y=50)

#Lable
result = ttk.Variable(app)
ttk.Label(app,textvariable=result).place(x=300,y=240)

def show():
    global cnv
    global img
    #print(graphs.get())
    column1=col1.get()
    column2=col2.get()
    column3=col3.get()
    
    g=graphs.get()
    if 'col1' in g:
        if column1 == 'Select':
            result.set('column 1 must be selected')
            return
    if 'col2' in g:
        if column2 == 'Select':
            result.set('column 2 must be selected')
            return
    if 'col3' in g:
        if column3 == 'Select':
            result.set('column 3 must be selected')
            return
    
    fig=plt.figure(figsize=(5,2))
    eval(graphs.get().format(col1=column1,col2=column2,col3=column3))
    fig.savefig('graph.png')
    img=ImageTk.PhotoImage(Image.open('graph.png').resize((250,200)))

    
    cnv.create_image(0,0,anchor=ttk.NW,image=img)
    result.set("success")
    #plt.show()

ttk.Button(app,text='Show',command=show).place(x=400,y=10)
#win=ttk.Tk()
#win.geometry("750x270")
#create a canvas
#canvas=ttk.Canvas(win, width=600,height=400).pack()
#load image in the script
#img=ttk.ImageTk.PhotoImage(ttk.Image.open("download.png"))

#add Image to the canvas Items 
#canvas.create_image(10,10,snchor=ttk.NW,image=img)
#win.mainloop()

app.mainloop()
