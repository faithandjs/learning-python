import streamlit as st
from pymongo import MongoClient
import random

client = MongoClient("mongodb://localhost:27017/")
db = client["movie_db"]
collection = db["favorite_movies"]

st.title("🎬 Favorite Movie Picker")


# movie_name = st.text_input("Enter your favorite movie: ", key="movie_input")
# print(f'Movie name: {movie_name}')

with st.form("movie_form", clear_on_submit=True):
    movie_name = st.text_input("Enter your favorite movie: ")
    submitted = st.form_submit_button("Save movie")
    # suggested = st.button("Suggest Me a Movie")

    if submitted:
        if movie_name.strip():
            collection.insert_one({"movie": movie_name.strip()})
            print(f'Saved movie: {movie_name}')
            st.success(f'"{movie_name}" has been saved!')
        else:
            st.warning("Please enter movie name.")

    # if suggested:
    #     movies = list(collection.find())
    #     print(f'Movies: {movies}')
    #     if movies:
    #         suggestion = random.choice(movies)
    #         print(f'Suggestion: {suggestion}')
    #         st.info(f"Today's movie suggestion: **{suggestion['movie']}**")
    #     else:
    #         st.error('No movies found in the database.')

# if st.button("Save movie"):
#     if movie_name.strip():
#         collection.insert_one({"movie": movie_name.strip()})
#         print(f'Collection: {collection}')
#         st.success(f'"{movie_name}" has been saved!')

#     else:
#         st.warning("Please enter movie name.")


if st.button("Suggest Me a Movie"):
    movies = list(collection.find())
    print(f'Movies: {movies}')
    if movies:
        suggestion = random.choice(movies)
        print(f'Suggestion: {suggestion}')
        st.info(f"Today's movie suggestion: **{suggestion['movie']}**")
    else:
        st.error('No movies found in the database.')
