# File 1: model_trainer.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

# LOAD DATA

products = pd.read_csv("Products.csv")
reviews = pd.read_csv("Reviews.csv")
users = pd.read_csv("Users.csv")

# DATA CLEANING

products.drop_duplicates(inplace=True)
reviews.drop_duplicates(inplace=True)
users.drop_duplicates(inplace=True)

products.fillna("Unknown", inplace=True)
reviews.fillna("No Review", inplace=True)
users.fillna("Unknown", inplace=True)


# Feature Engineering

products["combined_features"] = (
    products["product_name"].astype(str) + " " +
    products["category"].astype(str) + " " +
    products["brand"].astype(str)
)


# MODEL TRAINING

vectorizer = TfidfVectorizer(stop_words="english")
feature_matrix = vectorizer.fit_transform(products["combined_features"])

similarity = cosine_similarity(feature_matrix)

product_index = pd.Series(
    products.index,
    index=products["product_name"]
).drop_duplicates()

# ==============================
# SAVE MODEL FILES
# ==============================

pickle.dump(products, open("products.pkl", "wb"))
pickle.dump(similarity, open("similarity.pkl", "wb"))
pickle.dump(product_index, open("product_index.pkl", "wb"))

print("Model training completed successfully.")


