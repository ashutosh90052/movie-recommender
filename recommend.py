# recommend.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("tmdb_5000_movies.csv")
df["overview"] = df["overview"].fillna("")

# TF-IDF Vectorization
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(df["overview"])

# Cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Reverse map of indices and movie titles
indices = pd.Series(df.index, index=df["title"]).drop_duplicates()

def recommend(title, n=5):
    if title not in indices:
        return ["Movie not found. Try a different one."]
    
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:n+1]
    movie_indices = [i[0] for i in sim_scores]
    return df["title"].iloc[movie_indices].tolist()
