import google.generativeai as genai
import requests
import schedule
import time
import os

# -- Set API Keys (insert your actual keys below)
NEWS_API_KEY = "f7247ce817624a05819748ae158eaf90"
GEMINI_API_KEY = "AIzaSyD9u0qTCcZJ4Ncdfq8ATFy9Nhq2gYcSRi4"
TELEGRAM_BOT_TOKEN = "7882859016:AAHjc-ikCW2tIXKhX7lgVQVNoHboNiU0Y5E"
TELEGRAM_CHAT_ID = "1979708991"

# -- Configure Gemini
genai.configure(api_key=GEMINI_API_KEY) 
# 🔍 Print available models (debug only)
for m in genai.list_models():
    print("✅ Available model:", m.name)
model = genai.GenerativeModel("models/gemini-1.5-flash")



def fetch_ai_news():
    url = f"https://newsapi.org/v2/everything?q=artificial%20intelligence&sortBy=publishedAt&pageSize=5&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    articles = response.json().get("articles", [])
    
    headlines = []
    for article in articles:
        title = article['title']
        url_link = article['url']
        headlines.append(f"📰 {title}\n🔗 {url_link}")
    
    return "\n\n".join(headlines)

def summarize_news_with_gemini(news_text):
    prompt = f"""
    Summarize the following AI news headlines into a concise daily update suitable for a Telegram post. Add bullet points or emojis to make it clear and readable.

    Headlines:
    {news_text}
    """
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Failed to summarize: {str(e)}"

def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    requests.post(url, data=payload)

def job():
    print("🔁 Running daily AI news agent...")
    news = fetch_ai_news()
    summary = summarize_news_with_gemini(news)
    send_to_telegram(summary)
    print("✅ Telegram post sent!")

# Run at 9:00 AM daily
schedule.every().day.at("16:21").do(job)

print("⏰ Agent scheduled for Daily")
while True:
    schedule.run_pending()
    time.sleep(60)

