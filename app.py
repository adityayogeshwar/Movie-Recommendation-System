import streamlit as st
import pandas as pd
import requests
import preprocessor, extract

movies = pd.read_csv('tmdb_5000_movies.csv')
cr = pd.read_csv('tmdb_5000_credits.csv')
similarity, df = preprocessor.preprocess(movies, cr)

st.title('Movie Recommender System')

selected_movie = extract.fetch_movies(df)
selected_movie_name=st.selectbox('Choose the movie', selected_movie)

# st.table(df)
def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=7bb6dc0fae4121c04009546001b4fb77&language=en-US'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']
def recommend(movie):
    mov = []
    img=[]
    movie_index = df[df['title'] == movie].index[0]
    distances = similarity[movie_index]
    top_distances = sorted(list(enumerate(distances)),reverse=True,key=lambda x: x[1])[1:6]
    for i in top_distances:
        movie_id=df.iloc[i[0]].id
        mov.append(df.iloc[i[0]].title)
        #fetch poster from API
        img.append(fetch_poster(movie_id))
    return mov,img

if st.button('Recommend Movie'):
   
    names,posters=recommend(selected_movie_name)
    col1,col2,col3,col4,col5=st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
