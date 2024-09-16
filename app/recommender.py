# recommender.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Load the anime dataset
anime_df = pd.read_csv('data/anime.csv')

# Preprocess genres for TF-IDF vectorization
anime_df['genre'] = anime_df['genre'].fillna('')

# Create a TF-IDF vectorizer and fit on genre column
tfidf = TfidfVectorizer(stop_words='english')
anime_genre_matrix = tfidf.fit_transform(anime_df['genre'])

# Calculate cosine similarity between anime genres
anime_similarity = linear_kernel(anime_genre_matrix, anime_genre_matrix)

# Function to get recommendations
def get_recommendations(title, anime_df=anime_df, similarity_matrix=anime_similarity):
    # Get index of the anime
    idx = anime_df[anime_df['name'].str.contains(title, case=False)].index[0]

    # Get similarity scores for the anime
    sim_scores = list(enumerate(similarity_matrix[idx]))

    # Sort scores in descending order of similarity
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get top 10 most similar animes (excluding the first one, as it's the same anime)
    sim_scores = sim_scores[1:11]

    # Get anime indices
    anime_indices = [i[0] for i in sim_scores]

    # Return the names of the top 10 recommended animes
    return anime_df['name'].iloc[anime_indices].to_list()
