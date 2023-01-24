import requests

news_category = "technology"
API_KEY = 'fdfb4eb6b21e4ebea2c660e2d58676f0'
url = 'https://newsapi.org/v2/top-headlines?' \
      'country=in&' \
      'from=01-01-2023' \
      f'category={news_category}' \
      f'&apiKey={API_KEY}'

# sending a get request to API
response = requests.get(url)

# encode response to json format
content = response.json()
