
import streamlit as st
import pickle
import pandas as pd
import requests
def poster_fetch(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=1f6cf6ecfcc169655c179b899cfba30d&language=en-US'.format(movie_id))
    data = response.json()
    print(data)
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']



def overview_fetch(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=1f6cf6ecfcc169655c179b899cfba30d&language=en-US'.format(movie_id))
    data = response.json()
    return data['overview']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_poster = []
    recommended_overview = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        # fetch poster from API
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(poster_fetch(movie_id))
        recommended_overview.append(overview_fetch(movie_id))
    return recommended_movies,recommended_movies_poster, recommended_overview

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender system')

select_movie = st.selectbox(
"how would you like to contact?",
movies['title'].values)

if st.button('recommend'):
    names, poster, overviews = recommend(select_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(poster[0])
        st.write(overviews[0])
    with col2:
        st.text(names[1])
        st.image(poster[1])
        st.write(overviews[1])

    with col3:
        st.text(names[2])
        st.image(poster[2])
        st.write(overviews[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
        st.write(overviews[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])
        st.write(overviews[4])



