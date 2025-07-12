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
    Type your question in any format — but make sure to <strong>include the MRP exception code</strong> (like <code>10</code>, <code>15</code>, etc.).
    </p>
    <p>💡 Examples:</p>
    <ul>
        <li><em>Why am I seeing exception code 10 in plant 1001 for material 34567?</em></li>
        <li><em>Why exception code 20?</em></li>
        <li><em>Explain what is SAP exception code 30?</em></li>
    </ul>
    <p>This assistant will detect the code and give a smart explanation from SAP’s public best practices.</p>
</div>
""", unsafe_allow_html=True)

# 🚨 Disclaimer Block
st.markdown("""
🔍 **Disclaimer:**  
This assistant uses **OpenAI's ChatGPT 3.5 model**, which has not been trained on your company’s internal SAP system data.  
That means responses do **not reflect your live material master, inventory levels, purchase orders, or plant-specific planning rules**.  
Instead, the assistant draws from **publicly available SAP knowledge and common best practices** known to the model.

📌 Stay tuned for my next blog, where I’ll explain how to **train this assistant using your company’s real SAP data** — including MRP logs, planner notes, and exception handling workflows — to generate more accurate and customized recommendations.
""")

# Load MRP exception sample data
#df = pd.read_csv("../data/response_cache.csv", encoding="utf-8")
#row = st.selectbox("Choose an exception to analyze", df["response"])




# Optional long text input (to improve matching)
user_long_text = st.text_area("📝 Ask your MRP exception question in free text (must include exception code)")


# Submit
if st.button("🔍 Explain Exception"):
    result = classify_exception(user_long_text)
    st.subheader("✅ Suggested Insight")
    st.markdown(result)

    # 📊 Log user click to CSV
    log_path = Path("logs/usage_log.csv")
    log_path.parent.mkdir(exist_ok=True)
    with log_path.open("a", newline='', encoding='utf-8') as logfile:
        writer = csv.writer(logfile)
        if log_path.stat().st_size == 0:
            writer.writerow(["timestamp", "exception_text", "user_notes"])
        writer.writerow([datetime.now(),user_long_text])
