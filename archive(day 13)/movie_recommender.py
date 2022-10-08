import pandas as pd
import warnings
warnings.filterwarnings('ignore')
def movie_recommend(movie_selected='Star Wars (1977)'):
    cols=['user_id','movie_id','rating','ts']
    df=pd.read_csv('u.data', sep='\t', names=cols).drop('ts',axis=1)
    item_cols = ['movie_id','title']+ [str(i) for i in range(22)]
    df1=pd.read_csv('u.item', sep='|', encoding = "ISO-8859-1", names=item_cols)[['movie_id','title']]
    #merge
    movie=pd.merge(df,df1,on='movie_id')
    #movie_pivot
    movie_pivot=movie.pivot_table(index='user_id',columns='title', values='rating')
    #find similarities for selected movie
    corrs = movie_pivot.corrwith(movie_pivot[movie_selected])
    corrs_df=pd.DataFrame(corrs, columns=['correlation'])
    corrs_df['rating']=movie.groupby('title')['rating'].mean()
    corrs_df['count']=movie['title'].value_counts()
    #find top 2-3 recommendations
    top_recom=list(corrs_df[corrs_df['count']>50].sort_values(by='correlation', ascending=False).head(3).index)
    top_recom.remove(movie_selected)
    
    return top_recom
    
    
print(movie_recommend(input("enter the name of movie you watched: ")))