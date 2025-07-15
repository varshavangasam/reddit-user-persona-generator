import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def build_persona(user_data):
    texts = []
    for entry in user_data:
        texts.append(f"[{entry['type']} from r/{entry['subreddit']}]\n{entry['text']}\n(Source: {entry['permalink']})")

    prompt = f"""
Given the following Reddit activity, generate a user persona. Include:

- Estimated Age
- Possible Location
- Occupation / Interests
- Personality Traits
- Hobbies
- Writing Style
- Cite 1–2 Reddit sources for each trait

Text data:
{"\n\n".join(texts[:30])}
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # ← changed from "gpt-4"
        messages=[
            {"role": "system", "content": "You are a sociologist analyzing Reddit user behavior."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content

