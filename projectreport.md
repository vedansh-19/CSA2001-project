<h1 align="center">📊🎬 Movie Recommendation System - Project Report 🎬📊</h1>

<p align="center">
  <b>A Machine Learning based Content Recommendation System</b>
</p>

---

## 📌 1. Introduction

In today’s digital world, users are exposed to a vast number of choices, especially in entertainment platforms. Finding relevant content becomes challenging.  
This project focuses on building a **Movie Recommendation System** that suggests movies based on similarity in content such as **genre and language**.

The system uses **Natural Language Processing (NLP)** and **Machine Learning techniques** to provide meaningful recommendations.

---

## 🎯 2. Objectives

- To build a content-based movie recommendation system  
- To apply NLP techniques for text processing  
- To use similarity metrics for finding related movies  
- To create a simple and scalable project structure  

---

## 📚 3. Dataset Description

The project uses the **TMDB 5000 Movie Dataset** which contains:

- Movie titles  
- Overview (description)  
- Genres  
- Keywords  
- Language  

Two datasets are used:
- `tmdb_5000_movies.csv`  
- `tmdb_5000_credits.csv`  

These datasets are merged to create a unified dataset for analysis.

---

## 🧹 4. Data Preprocessing

Data preprocessing is a crucial step in the project. It includes:

- Removing unnecessary columns  
- Handling missing values using `dropna()`  
- Converting JSON-like strings into Python lists using `ast.literal_eval()`  
- Cleaning text data by removing spaces and formatting  

---

## 🧠 5. Feature Engineering

To improve recommendation quality, several features are processed:

- **Overview** → converted into word tokens  
- **Genres & Keywords** → extracted and cleaned  
- **Language** → included as a filtering feature  
- **Mood Feature** → derived from genres:
  - Action → exciting  
  - Comedy → funny  
  - Drama → emotional  
  - Horror → scary  

All features are combined into a single column called **tags**, which represents each movie.

---

## 🔤 6. Text Vectorization

The project uses **CountVectorizer** from Scikit-learn:

- Converts text data into numerical vectors  
- Removes common English stopwords  
- Limits features to the most relevant words  

This step enables the model to process textual information mathematically.

---

## 📐 7. Similarity Measurement

To find similar movies, **cosine similarity** is used:

- Measures similarity between vectors  
- Returns a value between 0 and 1  
- Higher value indicates more similarity  

This forms the core logic of the recommendation system.

---

## 🤖 8. System Design

The project follows a **modular structure**:

### 🔄 Workflow:


---

## 🎯 9. Implementation

The system provides two types of recommendations:

### 🔹 1. Movie-Based Recommendation
- User inputs a movie name  
- System suggests top 5 similar movies  

### 🔹 2. Preference-Based Recommendation
- User inputs:
  - Genre  
  - Language  
- System filters and displays matching movies  

---

## 🛠️ 10. Tools & Technologies

- **Python**  
- **Pandas** (data handling)  
- **NumPy** (numerical operations)  
- **Scikit-learn** (ML & NLP)  
- **AST** (data parsing)  

---

## 📊 11. Results

The system successfully recommends movies based on:
- Content similarity  
- User preferences  

Example Output:

---

## 💡 12. Advantages

- Simple and easy to understand  
- Fast execution  
- No need for user history  
- Works well with metadata  

---

## ⚠️ 13. Limitations

- No collaborative filtering  
- No user personalization  
- No rating-based recommendations  

---

## 🚀 14. Future Scope

- Develop a web application using Streamlit  
- Integrate movie posters using APIs  
- Use advanced NLP techniques (TF-IDF, embeddings)  
- Add hybrid recommendation system  

---

## 👨‍💻 15. Conclusion

This project demonstrates how machine learning and NLP techniques can be used to build a practical recommendation system.  
It provides a solid foundation for understanding **content-based filtering** and can be extended into more advanced systems.

---

## ✍️ 16. Author

**Vedansh Raj Singh**

---

<p align="center">
  ⭐ Thank you for reviewing this project!
</p>


