# Personalized Product Recommendation System

## Problem Statement
This project aims to build a personalized product recommendation system for e-commerce users. It suggests relevant products to users based on product similarity, ratings, category, and customer preferences.

## Dataset Used
The project uses 3 CSV files:

### Product.csv
- product_id
- product_name
- category
- brand
- price
- rating

### Review.csv
- review_id
- order_id
- product_id
- user_id
- rating
- review_text
- review_date

### User.csv
- user_id
- name
- email
- gender
- city
- signup_date

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- GitHub
- Excel (Data Cleaning)

## Features
- Product similarity recommendation
- Category-based filtering
- Brand-based suggestions
- Price comparison
- Rating-based recommendation
- Interactive frontend using Streamlit

## How to Run

```bash
pip install -r requirements.txt
streamlit run Recommender_app.py
App Link: https://recommender-for-ecommerce-tuxp9ttss2kalkuk9bfg5b.streamlit.app/

