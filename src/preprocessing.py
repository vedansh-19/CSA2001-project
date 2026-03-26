import pandas as pd
import ast


def load_and_clean_data():
    movies = pd.read_csv("./data/tmdb_5000_movies.csv")
    credits = pd.read_csv("./data/tmdb_5000_credits.csv")

    movies = movies.merge(credits, on='title')

    movies = movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'original_language']]
    movies = movies.dropna()

    def convert(text):
        data = []
        for i in ast.literal_eval(text):
            data.append(i['name'])
        return data

    movies['genres'] = movies['genres'].apply(convert)
    movies['keywords'] = movies['keywords'].apply(convert)

    def clean_list(data):
        return [i.replace(" ", "") for i in data]

    movies['genres'] = movies['genres'].apply(clean_list)
    movies['keywords'] = movies['keywords'].apply(clean_list)

    movies['overview'] = movies['overview'].apply(lambda x: x.split())

    def get_mood(genres):
        mood = []
        for g in genres:
            if g in ['Action', 'Adventure']:
                mood.append('exciting')
            elif g in ['Comedy']:
                mood.append('funny')
            elif g in ['Drama', 'Romance']:
                mood.append('emotional')
            elif g in ['Horror']:
                mood.append('scary')
        return mood

    movies['mood'] = movies['genres'].apply(get_mood)
    movies['mood'] = movies['mood'].apply(clean_list)

    movies['original_language'] = movies['original_language'].apply(lambda x: [x])

    movies['tags'] = (
        movies['overview'] +
        movies['genres'] +
        movies['keywords'] +
        movies['mood'] +
        movies['original_language']
    )

    new_df = movies[['movie_id', 'title', 'tags']]
    new_df['tags'] = new_df['tags'].apply(lambda x: " ".join(x))

    return new_df
