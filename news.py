# news.py
import requests

def get_news():
    api_key = "4f9e74b43bd64bda9d03f789aaf2b663"
    url = f"https://newsapi.org/v2/everything?q=INDIA&apiKey={api_key}"
    
    try:
        response = requests.get(url)
        data = response.json()

        if data["status"] == "ok":
            articles = data["articles"]
            news_list = []

            for article in articles[:5]:  # Top 5 headlines
                news_list.append(article["title"])

            return "\n".join(news_list)
        else:
            return "Unable to fetch news at the moment."
    except Exception as e:
        return f"Error: {str(e)}"