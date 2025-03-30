EDUCATIONAL_TOPICS = [
    "technology", "science", "engineering", "mathematics", "history",
    "physiology", "innovation", "business", "economics", "current affairs", "politics"
]

REJECTED_TOPICS = ["sports", "entertainment", "games", "violence", "celebrities", "movies"]

def is_educational(question: str) -> bool:
    lower_q = question.lower()
    return any(topic in lower_q for topic in EDUCATIONAL_TOPICS) and not any(bad in lower_q for bad in REJECTED_TOPICS)
