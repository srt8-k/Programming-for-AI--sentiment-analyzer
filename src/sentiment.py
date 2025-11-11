from textblob import TextBlob

def polarity(text: str) -> float:
    if text is None:
        return 0.0
    s = str(text).strip()
    if not s:
        return 0.0
    return TextBlob(s).sentiment.polarity

def sentimentAnalyzer(text: str) -> str:
    score = polarity(text)
    if score < -0.2:
        return "Negative"
    elif score > 0.2:
        return "Positive"
    else:
        return "Neutral"
