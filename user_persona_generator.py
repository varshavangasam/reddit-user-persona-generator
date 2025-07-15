import sys
from reddit_scraper import scrape_user_content
from persona_builder import build_persona

import os

def extract_username(profile_url):
    if "reddit.com/user/" not in profile_url:
        raise ValueError("❌ Invalid Reddit profile URL")
    return profile_url.strip("/").split("/")[-1]

def save_persona_to_file(username, persona_text):
    output_dir = "examples"
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, f"{username}_persona.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(persona_text)
    print(f"✅ Persona saved to {file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python user_persona_generator.py <reddit_profile_url>")
        sys.exit(1)

    profile_url = sys.argv[1]

    try:
        username = extract_username(profile_url)
        print(f"Scraping u/{username}...")

        user_data = scrape_user_content(username)

        # DEBUG: Check what user_data looks like
        if not isinstance(user_data, list):
            print("❌ user_data is not a list!")
            sys.exit(1)

        for entry in user_data:
            if not isinstance(entry, dict):
                print("❌ Entry in user_data is not a dictionary:", entry)
                sys.exit(1)

        persona = build_persona(user_data)
        save_persona_to_file(username, persona)

    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
