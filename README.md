# 📊 Amazon Unlocked Phones Sentiment Analyzer (TextBlob)

This project analyzes Amazon reviews for unlocked smartphones and classifies them into **Positive**, **Neutral**, or **Negative** sentiments using **TextBlob**.  
The goal is to explore customer opinions, visualize sentiment results, and generate insights that can help improve product reputation and customer satisfaction.

---

## 🚀 Features

- Loads Amazon unlocked phone reviews dataset
- Cleans & processes review text
- Calculates sentiment polarity via `TextBlob`
- Classifies reviews into:
  - ✅ Positive  
  - 😐 Neutral  
  - ❌ Negative
- Generates sentiment distribution charts
- Extracts example reviews for each sentiment type
- Exports processed results to CSV

---

## 🧠 Technologies Used

| Tool / Library | Purpose |
|---|---|
Python | Programming
Pandas | Data handling & analysis
TextBlob | Sentiment extraction
Matplotlib | Visualization
Jupyter Notebook | Interactive development

---

## 📁 Project Structure

.
├── MyAIProject/
├── ├── data/
├── │   ├── raw/
├── │   └── processed/
├── ├── notebooks/
├── │   └── sentiment.ipynb
├── ├── src/
├── │   └── sentiment.py
├── ├── reports/
├── ├── README.md
└── └── .gitignore
---

## 🧩 Sentiment Logic

| Polarity Score | Output Label |
|---|---|
Score < -0.2 | Negative ❌  
-0.2 ≤ Score ≤ 0.2 | Neutral 😐  
Score > 0.2 | Positive ✅  

Implemented in `src/sentiment.py`:

```python
def sentimentAnalyzer(text):
    score = polarity(text)
    if score < -0.2:
        return "Negative"
    elif score > 0.2:
        return "Positive"
    else:
        return "Neutral"
