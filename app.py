"""import pandas as pd
import streamlit
# goto doc.streamlit

#use this command on terminal (streamlit run E:/Movie-Recommendation-System/app.py)

import streamlit as st
#for make website you can use flask but we can use streamlit

import pickle

movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

#to display text
st.title('Movie Recommendation System')
#automatic a web page open on a machine and we get page with this title

#need form related thing from streamlit
st.selectbox
Streamlit Version
Display a select widget.
option = st.selectbox(
'How would you like to be contacted?',
movies['title'].values)

st.write('You selected:', option)

#show the list of movies to in the ('Email', 'Home phone', 'Mobile phone') option, use """

import streamlit as st
import pickle
import pandas as pd
import requests
#we give id and this hit the API, for hit a lib. called request need
def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=8469fa1c061f018a47ff28d4e022c4f6&language=en-US".format(movie_id))
    #store the response in data in json
    data=response.json()

    #return the data' poster path
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    # i got index
    distances = similarity[movie_index]
    # index of similarity matrix
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:7]

#from movie list , we take inside of it
    recommended_movies = []
    #make a new var. empty list
    recommended_movies_posters = []

    # print the list of movies , we get tuple
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        #fetch poster from API
        recommended_movies.append(movies.iloc[i[0]].title)
        #print(new_df.iloc[i[0]].title)

        #append the poster we het to recoo_mov_posters
        # fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters
#recommend('Avatar')



movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

#write a import state for similatrity.pjl
similarity= pickle.load(open('/site/wwwroot/similarity.pkl','rb'))

st.title('Movie Recommendation System')
selected_movie_name = st.selectbox(
"HEY , THERE TELL ME AND I'LL RECOMMEND YOU ",
movies['title'].values)

#add button
if st.button('Recommend'):
    names,posters= recommend(selected_movie_name)

    col1, col2, col3, col4, col5, col6 = st.columns(6)

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
    with col6:
        st.text(names[5])
        st.image(posters[5])


