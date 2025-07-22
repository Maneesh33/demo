import requests

# API key (sign up at newsapi.org for a free key)
api_key = "f7247ce817624a05819748ae158eaf90"  # Verify this key
url = f"https://newsapi.org/v2/everything?q=Artificial Intelligence&domains=techcrunch.com,bbc.co.uk&from=2025-07-01&to=2025-07-21&apiKey={api_key}"

try:
    response = requests.get(url)
    response.raise_for_status()  # Check for HTTP errors
    data = response.json()
    print(f"Total articles available: {len(data.get('articles', []))}")
    articles = data.get("articles", [])[:10]  # Top 10 articles
    
    with open("robotics_news.txt", "w", encoding="utf-8") as f:
        for i, article in enumerate(articles, 1):
            title = article.get("title", "No title")
            f.write(f"{i}. {title}\n")
            print(f"{i}. {title}")
    print("News saved to robotics_news.txt successfully!")
except Exception as e:
    print(f"Error: {e}")
    print("Check API key or internet connection.")
