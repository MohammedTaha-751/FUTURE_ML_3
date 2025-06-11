import json
import os
from sklearn.feature_extraction.text import TfidfVectorizer # type: ignore
from sklearn.metrics.pairwise import cosine_similarity # type: ignore

class Chatbot:
    def __init__(self, faq_path=None):
        # Use the given path or load from environment variable, or default
        self.faq_path = faq_path or os.getenv("FAQ_PATH", "data/faq.json")
        
        # Load the FAQ data
        with open(self.faq_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            self.questions = [item["question"] for item in data["faqs"]]
            self.answers = [item["answer"] for item in data["faqs"]]

        # Create TF-IDF vectors for all questions
        self.vectorizer = TfidfVectorizer()
        self.q_vectors = self.vectorizer.fit_transform(self.questions)

    def get_response(self, user_input):
        # Convert user input to vector
        user_vec = self.vectorizer.transform([user_input])
        
        # Compare with stored question vectors
        similarity = cosine_similarity(user_vec, self.q_vectors)
        best_match_index = similarity.argmax()
        confidence = similarity[0, best_match_index]

        # Return the best matched answer and its confidence score
        return self.answers[best_match_index], float(confidence)
