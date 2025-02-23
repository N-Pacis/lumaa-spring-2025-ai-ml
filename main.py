import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import sys

def load_data():
    """
    Load movie data from a CSV file and preprocess textual data.

    Returns:
        pandas.DataFrame: DataFrame containing movie data.
    """
    df = pd.read_csv('movies.csv')
    df['keywords'] = df['keywords'].fillna('')
    df['overview'] = df['overview'].fillna('')
    df['text'] = df['overview'] + ' ' + df['keywords']
    return df

def preprocess_text(text):
    """Preprocesses the input text by converting it to lowercase and normalizing whitespace.

    Parameters:
        text (str): The raw input text that needs to be preprocessed.

    Returns:
        str: The preprocessed text with all lowercase letters and normalized spacing.
    """
    return ' '.join(text.lower().split())

def get_recommendations(query, df, top_n=5):
    """Return top N recommendations based on cosine similarity with scores and ranks.
    
    Args:
        query (str): Input query.
        df (pd.DataFrame): DataFrame with 'text', 'title', and 'overview'.
        top_n (int): Number of recommendations (default 5).
        
    Returns:
        pd.DataFrame: DataFrame with 'title', 'overview', and 'similarity' columns.
    """
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['text'])
    
    processed_query = preprocess_text(query)
    query_vec = tfidf.transform([processed_query])
    
    cosine_sim = cosine_similarity(query_vec, tfidf_matrix).flatten()
    
    top_indices = cosine_sim.argsort()[-top_n:][::-1]
    recommendations = df.iloc[top_indices].copy()
    recommendations['similarity'] = cosine_sim[top_indices]
    return recommendations[['title', 'overview', 'similarity']]

if __name__ == "__main__":
    query = sys.argv[1]
    df = load_data()
    recommendations = get_recommendations(query, df)
    print(recommendations)