import tkinter as ttk
import pandas as pd
from unittest import result
import warnings
warnings.filterwarnings('ignore')
app=ttk.Tk()
app.geometry('1080x1080')
app.title('movie recommender')
#ttk.Label(app, text='enter the movie that you have watched: ').place(x=15,y=15)
result=ttk.Variable(app)
box=ttk.Listbox(app, height=10)
box.place(x=10,y=10)
def get_movie():
    pass
cols=['user_id','movie_id','rating','ts']
df=pd.read_csv('u.data', sep='\t', names=cols).drop('ts',axis=1)
item_cols = ['movie_id','title']+ [str(i) for i in range(22)]
df1=pd.read_csv('u.item', sep='|', encoding = "ISO-8859-1", names=item_cols)[['movie_id','title']]
#merge
movie=pd.merge(df,df1,on='movie_id')
for row,val in movie.iterrows:
    box.insert(row+1, val['title'])
        
ttk.Button(app, text='Find recommendations', font=('Arial',22), command=get_movie).place(x=200,y=50)
ttk.Label(app, textvariable=result,font=('Arial',22)).place(x=200,y=100)

app.mainloop()