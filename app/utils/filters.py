from dotenv import load_dotenv
import openai

load_dotenv()

SYSTEM_PROMPT = "You are a strict classifier. Only accept questions related to education: technology, science, engineering, math, business, history, physiology, innovation, economics, politics, or current affairs. Reject all sports, games, movies, celebrities, violence, entertainment, or unrelated topics."


def is_valid_question(question: str) -> bool:
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Classify this query: '{question}' as ACCEPT or REJECT."}
        ],
        temperature=0
    )
    decision = response.choices[0].message.content.lower()
    return "accept" in decision
