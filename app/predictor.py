import os
import pandas as pd
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

# Load environment variables from .env
load_dotenv(find_dotenv())
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Load local cache (CSV)
df_cache = pd.read_csv("../data/response_cache.csv", encoding="utf-8")

def classify_exception(exception_text, notes=""):
    # Step 1: Try finding a cached explanation
    match = df_cache[df_cache['response'].str.contains(exception_text, case=False, na=False)]

    if not match.empty:
        return f"📄 **Cache Match Found:**\n\n{match.iloc[0]['response']}"

    # Step 2: Fallback to GPT
    try:
        with open("../prompts/base_prompt.txt") as f:
            base_prompt = f.read()
    except FileNotFoundError:
        return "⚠️ Prompt template not found. Please ensure prompts/base_prompt.txt exists."

    final_prompt = base_prompt.replace("{{exception_text}}", exception_text)
    if notes:
        final_prompt += f"\nAdditional planner notes: {notes}"

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": final_prompt}]
        )
        return f"🤖 **AI Suggestion (GPT-3.5):**\n\n{response.choices[0].message.content}"

    except Exception as e:
        return f"❌ GPT API error: {str(e)}"
