import streamlit as st
import pandas as pd
from predictor import classify_exception
from pathlib import Path
import csv
from datetime import datetime

# Set Streamlit page config
st.set_page_config(page_title="MRP Exception Assistant", layout="centered")

# 🎯 Title
st.title("🧠 MRP Exception Analyzer (GenAI-Powered)")

# 👥 Count analyzed exceptions
log_file = Path("logs/usage_log.csv")
click_count = 0
if log_file.exists():
    with log_file.open() as f:
        click_count = sum(1 for line in f) - 1  # skip header
st.markdown(f"👥 **Total Users Analyzed Exceptions**: `{click_count}`")

# 📘 Instructions (HTML block)
st.markdown("""
<div style="background-color: #f5f5f5; padding: 15px; border-radius: 8px; border: 1px solid #ddd;">
    <h4>🧾 How to Use This Assistant</h4>
    <p style="margin-bottom: 10px;">
    Ask your MRP question in any format — just make sure to <strong>include the exception code</strong> (like <code>10</code>, <code>15</code>, <code>30</code>).
    </p>
    <p>💡 Examples:</p>
    <ul>
        <li><em>Why am I seeing exception code 10 in plant 1001 for material 34567?</em></li>
        <li><em>What does exception code 15 mean in MRP run?</em></li>
        <li><em>Explain SAP MRP exception 30</em></li>
    </ul>
    <p>The assistant will detect the exception code and return a matching explanation from standard SAP best practices.</p>
</div>
""", unsafe_allow_html=True)


# ⚠️ Disclaimer
st.markdown("""
#### 🔍 Disclaimer
This assistant uses a predefined set of explanations based on publicly available SAP knowledge.  
It does **not reflect your live SAP data, material master, or planning rules**.  
For site-specific logic, consult your SAP team.  

📌 In future versions, we plan to integrate actual planning logs and exceptions from your SAP system.
""")

# 📝 Long text input
user_input = st.text_area("📝 Ask your MRP exception question (must include a 2-digit exception code):")

# 🔍 Submit
if st.button("🔍 Explain Exception"):
    if user_input.strip():
        result = classify_exception(user_input)
        st.subheader("✅ Suggested Insight")
        st.markdown(result)

        # Log input
        log_file.parent.mkdir(exist_ok=True)
        with log_file.open("a", newline='', encoding='utf-8') as logfile:
            writer = csv.writer(logfile)
            if log_file.stat().st_size == 0:
                writer.writerow(["timestamp", "exception_text"])
            writer.writerow([datetime.now(), user_input])
    else:
        st.warning("Please enter your question including the exception code.")
