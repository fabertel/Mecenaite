import openai
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer



def find_similar_paintings(description_to_search, df, top_n=5):
    vectorizer = TfidfVectorizer()

    # Vectorize the search description
    vectorizer.fit([description_to_search])
    search_vector = vectorizer.transform([description_to_search])

    # Calculate similarity scores with each painting description
    similarity_scores = []
    for _, row in df.iterrows():
        painting_desc_vector = vectorizer.transform([row['description']])
        cosine_sim = cosine_similarity(search_vector, painting_desc_vector)[0][0]
        similarity_scores.append((row['painting_name'], cosine_sim))

    # Sort paintings based on similarity score
    similarity_scores.sort(key=lambda x: x[1], reverse=True)
    top_similar_paintings = similarity_scores[:top_n]

    return top_similar_paintings

# Example dataframe
data = {
    'painting_name': ['Mona Lisa', 'Starry Night','Starry Night clone','Starry Night clones', 'The Scream'],
    'description': ['A portrait of a woman with a mysterious smile.', 
                    'A swirling night sky over a small village.', 
                    'A swirling day sky over a large humunguis village.', chat
                    'A swirling day sky over a large humunguis city.', 
                    'An agonized figure against a blood red sky.']
}
df = pd.DataFrame(data)

# Example usage
description_to_search = "A painting featuring a night sky with stars and a small village."
top_paintings = find_similar_paintings(description_to_search, df)

for name, score in top_paintings:
    print(f"{name}: {score:.2f}")
