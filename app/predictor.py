import pandas as pd
import re

# Load local cache (CSV)
df_cache = pd.read_csv("./data/response_cache.csv", encoding="utf-8")

def classify_exception(exception_text, notes=""):
    # Extract 2-digit exception code (e.g., 10, 15, etc.)
    match = re.search(r'\b(\d{2})\b', exception_text)

    if match:
        code = int(match.group(1))
        match_row = df_cache[df_cache['code'] == code]

        if not match_row.empty:
            return f"📄 **Explanation for Exception Code {code}:**\n\n{match_row.iloc[0]['response']}"
        else:
            return f"⚠️ No cached explanation found for exception code `{code}` in response_cache.csv."
    else:
        return "⚠️ Could not detect a valid 2-digit MRP exception code in your question."
