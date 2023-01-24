import requests

news_category = "technology"
API_KEY = 'fdfb4eb6b21e4ebea2c660e2d58676f0'
url = 'https://newsapi.org/v2/top-headlines?' \
      'country=in&' \
      'pageSize=5&' \
      'from=01-01-2023' \
      f'category={news_category}' \
      f'&apiKey={API_KEY}'

# sending a get request to API
response = requests.get(url)

# encode response to json format
content = response.json()

# Extract title and description of news to send over mail
news_content = ""
for article in content['articles']:
    if article['title'] and article['description'] and article['url'] is not None:
        news_content = news_content + article['title'] + '\n' + article['description'] + '\n' + article['url'] + 2*'\n'

print(news_content)
