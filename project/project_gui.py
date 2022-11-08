import tkinter as ttk
import pandas as pd

app = ttk.Tk()

model = pd.read_pickle('model.pickle')

app.geometry('400x500')
app.title('used-car resell price prediction')

year = ttk.Variable(app)
year.set('0')
ttk.Label(app, text="Enter the Year",padx=10,pady=10).place(x=20,y=30)
ttk.Spinbox(app, from_=1942,to=2019 ,textvariable=year, width='20',).place(x=20,y=70)

engine = ttk.Variable(app)
engine.set('0')
ttk.Label(app, text="Enter the Engine Capacity",padx=10,pady=10).place(x=200,y=30)
ttk.Spinbox(app, from_=0,to=10 ,textvariable=engine).place(x=200,y=70)

trans={'Mechanical':[1],
        'Automatic':[0],
        }

y=140
transmission = ttk.Variable(app)
ttk.Label(app, text="Transmission Type of your car ",padx=10,pady=10).place(x=20,y=100)
for key,value in trans.items():
    ttk.Radiobutton(app, text=key ,variable=transmission,value=value).place(x=20,y=y)
    y=y+20

val=['Gasoline',
     'Diesel'
    
]

Odometer = ttk.Variable(app)
Odometer.set('0')
ttk.Label(app, text="Enter the Odometer value",padx=10,pady=10).place(x=200,y=100)
ttk.Spinbox(app, from_=0, to=100000 ,textvariable=Odometer, width='20',).place(x=200,y=140)

ttk.Label(app, text="Enter the Engine Type",padx=10,pady=10).place(x=20,y=200)
frame=ttk.Frame(app)
frame.place(x=20,y=250)
box=ttk.Listbox(frame,width=20 ,height=3)
box.place(x=10,y=10)
for type in val:
    box.insert(ttk.END, type)
box.pack(side='left', fill='y')

result = ttk.Variable(app)

def pred():
    global model
    x=box.get(box.curselection())
    if x=='Gasoline':
        x=1
    else:
        x=0
    query_data={'odometer_value':[eval(Odometer.get())],
                'year_produced':[eval(year.get())],
                'engine_capacity':[eval(engine.get())],
                'transmission_mechanical':[transmission.get()],
                'engine_type_gasoline':[x]
                }
    prediction = model.predict(pd.DataFrame(query_data))
    result.set(round(prediction[0],2))

ttk.Button(app, text="Predict", command=pred, font=('Times New Roman',20)).place(x=120,y=370)
ttk.Label(app, text="Amount is in USD ($)", font=('Times New Roman',12)).place(x=100,y=430)

ttk.Label(app, textvariable=result, font=(22)).pack(side=ttk.BOTTOM)

app.mainloop()