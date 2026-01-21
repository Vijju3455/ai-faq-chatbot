import json
import re
from difflib import SequenceMatcher
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_faq_data():
    file_path = os.path.join(BASE_DIR, "faq_data.json")
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["faqs"]

def find_best_match(user_query, faqs):
    best_match = None
    best_score = 0
    user_query_lower = user_query.lower()

    for faq in faqs:
        question_lower = faq["question"].lower()
        keywords = re.findall(r"\b\w+\b", user_query_lower)
        match_count = sum(1 for k in keywords if k in question_lower)
        score = match_count / len(keywords) if keywords else 0
        seq_score = SequenceMatcher(None, user_query_lower, question_lower).ratio()
        combined_score = (score + seq_score) / 2

        if combined_score > best_score:
            best_score = combined_score
            best_match = faq

    return best_match if best_score > 0.3 else None

def get_response(user_query):
    faqs = load_faq_data()
    match = find_best_match(user_query, faqs)
    if match:
        return match["answer"]
    return "Sorry, I don't have an answer for that."
