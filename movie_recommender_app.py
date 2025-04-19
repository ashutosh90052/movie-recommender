# movie_recommender_app.py
import streamlit as st
from recommend import recommend

st.set_page_config(page_title="🎥 Movie Recommender", layout="centered")
st.title("🎬 Movie Recommender System")
st.markdown("Get top movie recommendations based on your favorite!")

movie_name = st.text_input("Enter a movie title")

if st.button("Recommend"):
    with st.spinner("Finding similar movies..."):
        recommendations = recommend(movie_name)
        st.success("Top Recommendations:")
        for i, title in enumerate(recommendations, start=1):
            st.write(f"{i}. {title}")
