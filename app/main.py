import streamlit as st
import pandas as pd
from predictor import classify_exception
from pathlib import Path
import csv
from datetime import datetime

# Set Streamlit page
st.set_page_config(page_title="MRP Exception Assistant", layout="centered")
st.title("🧠 MRP Exception Analyzer (GenAI-Powered)")

# 👥 Display total click count
log_file = Path("logs/usage_log.csv")
click_count = 0
if log_file.exists():
    with log_file.open() as f:
        click_count = sum(1 for line in f) - 1  # exclude header
st.markdown(f"👥 **Total Users Analyzed Exceptions**: `{click_count}`")

# 📘 Instruction Block
st.markdown("""
<div style="background-color: #f5f5f5; padding: 15px; border-radius: 8px; border: 1px solid #ddd;">
    <h4>🧾 How to Use This Assistant</h4>
    <p style="margin-bottom: 10px;">
    Ask your MRP question in any format — just make sure to <strong>include the exception code</strong> (like <code>10</code>, <code>15</code>, etc.).
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

# 🚨 Disclaimer Block
st.markdown("""
🔍 **Disclaimer:**  
This assistant uses a predefined set of explanations based on publicly available SAP knowledge.  
It does **not reflect your live SAP data, material master, or planning rules**.  
For site-specific MRP logic, consult your SAP team.

📌 In the next version, we’ll show how to train this assistant using real planning logs and exceptions from your SAP system.
""")

# 📝 Long Text Input
user_long_text = st.text_area("📝 Ask your MRP exception question in free text (must include exception code)")

# 🔍 Submit Button
if st.button("🔍 Explain Exception"):
    result = classify_exception(user_long_text)
    st.subheader("✅ Suggested Insight")
    st.markdown(result)

    # 📊 Log user input
    log_path = Path("logs/usage_log.csv")
    log_path.parent.mkdir(exist_ok=True)
    with log_path.open("a", newline='', encoding='utf-8') as logfile:
        writer = csv.writer(logfile)
        if log_path.stat().st_size == 0:
            writer.writerow(["timestamp", "exception_text", "user_notes"])
        writer.writerow([datetime.now(), user_long_text])
