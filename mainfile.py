from src.preprocessing import load_and_clean_data
from models.recommender import build_model, recommend, recommend_by_preferences


new_df = load_and_clean_data()
similarity = build_model(new_df)


print("\n1. Recommend by movie")
print("2. Recommend by preferences")

choice = input("Enter choice: ")

if choice == "1":
    movie_name = input("Enter movie name: ").title()
    recommend(movie_name, new_df, similarity)

elif choice == "2":
    genre = input("Enter genre (Action, Comedy, Drama, etc): ")
    language = input("Enter language (en, hi, etc): ")

    recommend_by_preferences(new_df, genre, language)

else:
    print("Invalid choice")
