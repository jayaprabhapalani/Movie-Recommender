# 🎬 Movie Recommender System | Content-Based Filtering with Streamlit

This project is a **Content-Based Movie Recommender System** built using **Python**, **Pandas**, **Scikit-learn**, and **Streamlit**. It recommends movies based on metadata such as genres, keywords, cast, and crew information. The web app interface is deployed using **Streamlit**, and movie posters are fetched via the **OMDB API**.

---

## 📂 Dataset

The project uses the **TMDB 5000 Movie Dataset** from Kaggle:  
🔗 [TMDB Dataset on Kaggle](https://www.kaggle.com/tmdb/tmdb-movie)

It consists of two main files:
- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

These were merged using the `movie_id` to form a single comprehensive dataset.

---

## 📌 Features Used

From the combined dataset, the following columns were selected to create a **`tags`** column used for recommendations:

- `overview` → Movie plot
- `genres` → Main genres (e.g., Action, Comedy)
- `keywords` → Relevant descriptive terms
- `cast` → Top 3 leading actors
- `crew` → Only the director

---

## 🧠 NLP Preprocessing Steps

To prepare the text data for similarity comparison, the following steps were applied:

1. **Cleaning & Merging**: All selected features were combined into a single string `tags` column.
2. **Lowercasing**: To ensure uniformity.
3. **Removing Stopwords & Punctuation**
4. **Stemming**: Used NLTK's `PorterStemmer` to reduce words to their root form  
   _(e.g., "activities" → "activ")_ to eliminate redundancy.
5. **Vectorization**: Applied **Bag-of-Words (BoW)** using `CountVectorizer`:
   - Maximum 5000 words
   - Removed English stopwords
   - Converted each movie's `tags` into a 5000-dimensional sparse vector
6. **Similarity Calculation**:
   - Used **Cosine Similarity** to compare movies based on their vectorized tag content.

---

## 🧪 Pickled Files for Deployment

To make the app efficient and portable, the following files were saved using `pickle`:

'''python
pickle.dump(new_df, open('movies.pkl', 'wb'))              # DataFrame with tags
pickle.dump(new_df.to_dict(), open('movies_dict.pkl', 'wb')) # Dictionary version
pickle.dump(similarity, open('similarity.pkl', 'wb'))       # Similarity matrix
-----'''
# These files are used in the app.py file for real-time movie recommendations.
