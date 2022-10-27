import tkinter as ttk
import pandas as pd

model = pd.read_pickle('CarPricePredictor.pickle')
cols = model.feature_names_in_

app = ttk.Tk()
app.geometry('380x300')
app.title('Used Car Price Predictor')
# Transmission Type

ttk.Label(app, text = 'Choose Transmission', padx=20,pady=20).grid(row=0,column=0)

trans = {
    'Manual':1,
    'Automatic':0
}

transVar = ttk.Variable(app)
transVar.set(trans['Manual'])
frame = ttk.Frame(app)
frame.grid(row=0,column=1)
for transmission,transvalue in trans.items():
    ttk.Radiobutton(frame, text = transmission , variable= transVar , value = transvalue).pack(side=ttk.LEFT)

# Power
ttk.Label(app, text='Enter Engine Power (BHP)',padx=20,pady=20).grid(row=1,column=0)
powerVar = ttk.DoubleVar(app)
powerVar.set(0.0)
ttk.Spinbox(app, from_=0,to= 5000, textvariable= powerVar).grid(row=1,column=1)

# Year
ttk.Label(app, text='Car Manufacturing Year ',padx=20,pady=20).grid(row=2,column=0)
yearVar = ttk.DoubleVar(app)
yearVar.set(0.0)
ttk.Spinbox(app, from_=1900,to= 2022, textvariable= yearVar).grid(row=2,column=1)

# Prediction Button
resultVar = ttk.Variable(app)
ttk.Label(app , textvariable=resultVar,font = ('Times New Roman',20)).grid(row=4,column=0,columnspan=2)

def find_Price():
    global model
    values = [[powerVar.get()],[yearVar.get()],[transVar.get()]]
    cols = model.feature_names_in_
    
    query_df = pd.DataFrame(dict(zip(cols,values)))
    pred = round(model.predict(query_df)[0],1)
    resultVar.set(f'{pred} Lacs')
    
    
ttk.Button(app, text = 'Check' , command=find_Price , padx = 20 , pady = 2).grid(row=3,column=0 , columnspan= 2)


app.mainloop()