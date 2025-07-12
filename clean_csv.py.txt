import pandas as pd

df = pd.read_csv('./data/response_cache.csv', encoding='utf-8')

# Clean column names
df.columns = [col.strip().lower() for col in df.columns]

# Only keep 'code' and 'response' columns
df = df[['code', 'response']]

# Save cleaned version
df.to_csv('./data/response_cache.csv', index=False, encoding='utf-8')

print("✅ response_cache.csv cleaned successfully.")
