import requests




def get_news_by_source(source):
    api_url = "https://newsapi.org/v2/everything?q=tesla&source="+ source +"&from=2022-07-10&sortBy=publishedAt&apiKey=API_KEY"
    response = requests.get(api_url)
    return response.json()
    
    
    