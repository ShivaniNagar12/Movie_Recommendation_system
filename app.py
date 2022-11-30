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
similarity= pickle.load(open('https://doc-0o-60-docs.googleusercontent.com/docs/securesc/l5lrfphanqtec5c7451bvq9mjqu5uue6/r2kbs8pr2u1rfbe768c0qgk4ae3uqos4/1669790400000/03668417067594286521/03668417067594286521/1FPFavI_9RCp17iHyAZW7Go1jSnasOQc7?e=download&ax=AEKYgyQ9eGtg1Qc_St3zSAVgaTksEK-EEIIUkbpPuW-OU3fkJ3cAz7cAzRWd4QOav_ddEt47AsMqNkPiL6MXiaq6wmR5L_CeIGiNyA7WZN1ST_yHkGAv3YhlF1Sj-uFXSIAKA53ZrSL-n3tm4CN3q79bJS9RUnYr8j5T0JPqAgAwR92vIYSU3OILqMyrL8o8k8fkpSSyr9uaowjhI2hzh0bVjVnn3-259mf8jKqojExM6QzWTrSRDL3WAX1kB-K3wN4qbTdc7VRl-o4DOSDEtLmIW5ustiF_HTIcViAVDNyySaqnIysr2iQbw_lhOhmafStpiDpnw1TWTzdAPgasxxDY4X4kMDpqkPiOJUbhJNv2wEWOmfwaKS19e66mOSGcEY_EQb_Q3bjvaTculKh2lxXP1sfbvGAbKgoij_tOJtRUNevzkE-YW6h4w2BeOr1cWqSHYxMZTo5taFu8MFTQxPPm6LKpspKBN86i0byLbVlqkOguCrvLSK0rwqNi1RCuRud2XGIXJzgHxQrLHSCight6ZbsGXq54Ujec-zUhRN9m_NsZ7-EftwdeRbHWg2EP9UCJKHSkO9qx4L8TM0wOD9oCtt3M-ihQc9TdP7rSylK_SP9HfwmxYJOmnQ5ajXQoAN4cRZGhsw64X_pv2uBfQjToUNqNEs4dtoAxjM4bR36bDIzQvRjK26HewBpoMkWSVYI1K8Ve_X1kvG1eQAcKyM59BUnlyNPq08nxRy86KeXPanu-h6Q97RKbREn0TEPAn2mqMEde4dK4lv9ScSuetwUmk6Xq2oYLGyFeaMQvgk7ne26XojtH5IZBCr8600P2KJitXeuDX6tOTeMu8KLrCCzhLMJN7JsjMEedLKWI3e9et25KDrf4XfOfJ4RnDNTYCFHJ3OX-yX89VgjqJO9TyULkq90-sZmA6fPtbL6xxAyzoXFeg9wgHeFjuwwDg6I0PYa_G6sC1ger&uuid=9c155513-4ee0-4c08-97ce-4186ec025ba1&authuser=0','rb'))

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


