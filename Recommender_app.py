import streamlit as st
import pickle

# Load Trained Files

products = pickle.load(open("products.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))
product_index = pickle.load(open("product_index.pkl", "rb"))

# Recommended Function

def recommend_products(product_name, top_n=5):
    if product_name not in product_index:
        return []

    idx = product_index[product_name]
    similarity_scores = list(enumerate(similarity[idx]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    similarity_scores = similarity_scores[1:top_n + 1]

    recommended_indices = [i[0] for i in similarity_scores]

    return products.iloc[recommended_indices][[
        "product_name",
        "category",
        "brand",
        "price",
        "rating"
    ]]

# Streamlit UI
st.set_page_config(page_title="Product Recommender", layout="wide")

st.title("Personalized Product Recommendation System")
st.write("Smart recommendations using Content-Based Filtering")

product_list = sorted(products["product_name"].unique())
selected_product = st.selectbox("Select Product", product_list)

if st.button("Recommend"):
    result = recommend_products(selected_product)

    if len(result) == 0:
        st.warning("Product not found")
    else:
        st.subheader("Recommended Products")
        st.dataframe(result)

st.markdown("---")
st.subheader("Project Workflow")
st.write("""
1. Data Cleaning
2. Feature Engineering
3. Model Training
4. Save Trained Files
5. Streamlit Dashboard
6. Product Recommendation
""")

