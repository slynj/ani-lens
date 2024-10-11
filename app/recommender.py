import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

anime_df = pd.read_csv('data/anime.csv')

anime_df['genre'] = anime_df['genre'].fillna('')

tfidf = TfidfVectorizer(stop_words='english')
anime_genre_matrix = tfidf.fit_transform(anime_df['genre'])

anime_similarity = linear_kernel(anime_genre_matrix, anime_genre_matrix)

def get_recommendations(title, anime_df=anime_df, similarity_matrix=anime_similarity):
    idx = anime_df[anime_df['name'].str.contains(title, case=False)].index[0]

    sim_scores = list(enumerate(similarity_matrix[idx]))

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    sim_scores = sim_scores[1:11]

    anime_indices = [i[0] for i in sim_scores]

    return anime_df['name'].iloc[anime_indices].to_list()
