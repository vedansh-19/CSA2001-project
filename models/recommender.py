from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def build_model(new_df):
    cv = CountVectorizer(max_features=5000, stop_words='english')
    vectors = cv.fit_transform(new_df['tags']).toarray()
    similarity = cosine_similarity(vectors)
    return similarity


def recommend(movie, new_df, similarity):
    if movie not in new_df['title'].values:
        print("Movie not found")
        return

    index = new_df[new_df['title'] == movie].index[0]
    scores = similarity[index]

    movies = sorted(list(enumerate(scores)), key=lambda x: x[1], reverse=True)[1:6]

    print("\nRecommended movies:\n")
    for i in movies:
        print(new_df.iloc[i[0]].title)


def recommend_by_preferences(new_df, genre=None, language=None):
    filtered = new_df.copy()

    if genre:
        filtered = filtered[filtered['tags'].str.contains(genre.replace(" ", ""), case=False)]

    if language:
        filtered = filtered[filtered['tags'].str.contains(language, case=False)]

    print("\nFiltered recommendations:\n")

    for i, movie in enumerate(filtered['title'].head(10), start=1):
        print(f"{i}. {movie}")
