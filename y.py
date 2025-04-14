import streamlit as st
import requests
from googletrans import Translator

# Set Streamlit page configuration
st.set_page_config(page_title="Live News", page_icon="📰", layout="wide")

# GNews API Configuration
GNEWS_API_KEY = "APIKEY"
BASE_URL = "https://gnews.io/api/v4/top-headlines"

def get_news(category="general"):
    """Fetch news articles from GNews API based on category."""
    params = {
        "category": category,
        "apikey": GNEWS_API_KEY,
        "lang": "en",
        "max": 10  # Limit the number of articles
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json().get("articles", [])
    else:
        st.error("Failed to fetch news. Check API key or try later.")
        return []

def translate_text(text, target_lang):
    """Translate text to the selected language."""
    translator = Translator()
    try:
        return translator.translate(text, dest=target_lang).text
    except Exception as e:
        st.warning("Translation failed.")
        return text

# Language selection
languages = {"English": "en", "Hindi": "hi", "French": "fr", "Spanish": "es"}
selected_language = st.selectbox("Select language", list(languages.keys()))

# News Category Selection
categories = {"General": "general", "Technology": "technology", "Sports": "sports", "Business": "business"}
selected_category = st.selectbox("Select News Category", list(categories.keys()))

# Fetch news
news_articles = get_news(categories[selected_category])

# Display news
for news in news_articles:
    st.image(news['image'], width=700)
    translated_title = translate_text(news['title'], languages[selected_language])
    translated_description = translate_text(news['description'], languages[selected_language])
    st.markdown(f"### {translated_title}")
    st.write(f"{translated_description}")
    st.write(f"[Read More]({news['url']})")
    st.markdown("---")

