# 🧠 Smart MRP Exception Assistant | GenAI + SAP Simulation

This is a simulated **SAP Joule-style assistant** for explaining MRP exception messages (like those in MD06), built entirely with **Python + OpenAI + Streamlit**.

It mirrors SAP’s real-world GenAI lifecycle as taught in the **SAP AI Certification Journey**:
➡️ [Starting From Ideation to Productization](https://learning.sap.com/learning-journeys/navigating-large-language-models-fundamentals-and-techniques-for-your-use-case)

---

## 🧠 Simulated Use Case

**SAP Component**: PP / MRP  
**User Need**: "Why is this MRP message flagged, and what should I do?"  
**Assistant Action**: Explains the exception, root cause, and suggested action via GenAI.

---

## 🔄 SAP GenAI Lifecycle (Simulated)

| Phase | Example from this Project | Role |
|-------|---------------------------|------|
| **Ideation** | Interviewed planners about MD06 confusion | Functional Consultant |
| **Validation** | Ran GPT prompts on exception lines | Data Engineer |
| **Productization** | Created Streamlit UI + YAML-style flow | Python Developer |
| **Improvement** | Plan to collect user feedback on usefulness | UX Designer |

---

## 🛠️ Tools Used
- OpenAI GPT 3.5
- Streamlit
- Simulated MD06 CSV data
- YAML-based flow logic
- `.env` protected API

---

## 📘 Future Roadmap
- Replace Streamlit with SAP Fiori if connected to SAP BTP
- Integrate Joule-style chat input
- Add Gemini support for cost benchmarking

---

## 💬 Based on SAP Joule Use Case Logic

SAP Joule is SAP’s GenAI assistant. This repo mirrors what **Joule might do behind the scenes**:
- Interpret MRP messages
- Offer contextual reasoning
- Suggest planner action
