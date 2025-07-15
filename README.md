# reddit-user-persona-generator
Scrape Reddit user posts/comments and generate user personas using LLMs.
# Reddit User Persona Generator

# Reddit User Persona Generator 🧠

This project scrapes Reddit user data (posts and comments) and generates a user persona by analyzing their content using an LLM (Large Language Model).

---

## ✨ Features

- 🔍 Scrapes **Reddit user posts and comments** using the PRAW API
- 📄 Generates a **detailed user persona** (age, location, hobbies, traits, etc.)
- 💬 Includes **source citations** for each trait from the scraped content
- 💾 Saves the final persona in a `.txt` file
- ✅ Easy to use and **can be integrated with free LLMs** (like GPT4All, OpenAI)
- 🔐 Secure with environment variables for credentials

---
Dependencies:

praw – for Reddit scraping
openai – for persona generation
python-dotenv – for reading .env file


Setup Instructions
1. Create a Reddit App
Go to https://www.reddit.com/prefs/apps
Scroll down to "Developed Applications" and click "Create App"
Fill details:
Name: Anything (e.g., RedditPersona)
Type: Script
Redirect URI: http://localhost:8080
After saving, you'll see:
client_id → Under the app name
client_secret → Clearly labeled


2. Get OpenAI API Key (Optional)

If using OpenAI:
Go to https://platform.openai.com/account/api-keys

Create a secret key.
Create a .env File
Create a .env file in the project folder with this format:

REDDIT_CLIENT_ID=your_client_id_here
REDDIT_CLIENT_SECRET=your_client_secret_here
REDDIT_USER_AGENT=your_app_name_or_username
OPENAI_API_KEY=your_openai_api_key_here  # optional if using OpenAI

If you're not using OpenAI, just leave OPENAI_API_KEY blank or use a local LLM.

🚀 How to Run for a New Reddit Profile
Open a terminal and run:
python user_persona_generator.py https://www.reddit.com/user/username/
Replace username with the Reddit user's name (e.g., kojied)

✅ Output will be saved as username.txt in the same folder.

File	Description
user_persona_generator.py	     Main script – combines scraping + persona generation
reddit_scrapper.py	           Scrapes comments & posts using praw
persona_builder.py	           Uses OpenAI API to generate persona
test_reddit.py	               Script to test Reddit credentials
requirements.txt	             Python packages needed
.env	                         Your Reddit/OpenAI API credentials

🧠 Sample Output
Example output (saved to kojied.txt):

User Persona /kojied

- Age: 22–28
- Location: Likely USA or Canada
- Occupation: Student or Tech Enthusiast
- Traits: Curious, Analytical, Social
- Writing Style: Casual, opinionated
- Cited Sources:
  - r/technology: “In my opinion, the best privacy tools are...”
  - r/AskReddit: “Here’s what I did last time...”

❗ Troubleshooting
401 Error → Check your client_id, client_secret, and user_agent in .env

Quota Exceeded → If using OpenAI, you might’ve run out of free usage

Model Not Found → Check that you're using a valid model like gpt-3.5-turbo







