import streamlit as st
import pickle
import pandas as pd
import requests


# Access the OMDb API key 
OMDB_API_KEY = st.secrets["api_keys"]["omdb"]

# Function to fetch movie poster from OMDb API using title
def fetch_poster(movie_title):
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={OMDB_API_KEY}"
    response = requests.get(url)
    data = response.json()
    if data.get('Response') == 'True' and data.get('Poster') != 'N/A':
        return data['Poster']
    else:
        # Return a placeholder if poster not available
        return "https://via.placeholder.com/300x445?text=No+Image"

# Function to recommend movies and return both titles and poster URLs
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movie_list:
        title = movies.iloc[i[0]].title
        recommended_movies.append(title)
        recommended_posters.append(fetch_poster(title))

    return recommended_movies, recommended_posters

# Load movie data
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
import os

def load_similarity_from_drive(url, filename):
    if not os.path.exists(filename):
        response = requests.get(url)
        with open(filename, 'wb') as f:
            f.write(response.content)

# Download similarity.pkl from Google Drive if not already downloaded
drive_url = "https://drive.google.com/uc?export=download&id=1Sm-kjq-V9OXZsImCAhv8CMFEEK0YZdZD"
similarity_file = "similarity.pkl"

load_similarity_from_drive(drive_url, similarity_file)
# Load similarity matrix
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit UI
st.title('Movie Recommender System 🎬')

# Dropdown to select a movie
selected_movie = st.selectbox('Select a movie:', movies['title'].values)

# Show recommendations when button is clicked
if st.button('Recommend'):
    names, posters = recommend(selected_movie)

    # Show 5 recommendations side by side
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.caption(names[i])
            st.image(posters[i], width=130)
