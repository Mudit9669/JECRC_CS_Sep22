import tkinter as ttk
import pandas as pd
from unittest import result
import warnings

warnings.filterwarnings('ignore')
app=ttk.Tk()
app.geometry('1000x600')
app.title('movie recommender') 
#ttk.Label(app, text='enter the movie that you have watched: ').place(x=15,y=15)
cols=['user_id','movie_id','rating','ts']
df=pd.read_csv('u.data', sep='\t', names=cols).drop('ts',axis=1)
item_cols = ['movie_id','title']+ [str(i) for i in range(22)]
df1=pd.read_csv('u.item', sep='|', encoding = "ISO-8859-1", names=item_cols)[['movie_id','title']]
#merge
movie=pd.merge(df,df1,on='movie_id')
result=ttk.Variable(app)
frame=ttk.Frame(app)
frame.place(x=10,y=10)
box=ttk.Listbox(frame,width=80 ,height=20)
box.place(x=10,y=10)
movie_pivot=movie.pivot_table(index='user_id',columns='title', values='rating')
def get_movie():
    movie_selected=box.get(box.curselection())
    corrs = movie_pivot.corrwith(movie_pivot[movie_selected])
    corrs_df=pd.DataFrame(corrs, columns=['correlation'])
    corrs_df['rating']=movie.groupby('title')['rating'].mean()
    corrs_df['count']=movie['title'].value_counts()
    #find top 2-3 recommendations
    top_recom=list(corrs_df[corrs_df['count']>50].sort_values(by='correlation', ascending=False).head(3).index)
    #important top_recom.remove(movie_selected)
    if movie_selected in top_recom:
        top_recom.remove(movie_selected)
    print(top_recom)
    result.set(top_recom[0])    
    

for title in movie['title'].unique():
    box.insert(ttk.END, title)
#box.grid(row = , column = )
box.pack(side='left', fill='y')
#box.place(x=10,y=10)

scroll=ttk.Scrollbar(frame, orient=ttk.VERTICAL)
scroll.config(command=box.yview)
box.config(yscrollcommand=scroll.set)
scroll.pack(side='right', fill='y')
        
ttk.Button(app, text='Find recommendations', font=('Arial'),width=22 ,command=get_movie).place(x=10,y=350)
ttk.Label(app, textvariable=result,font=('Arial',22)).place(x=20,y=500)

app.mainloop()