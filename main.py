import  requests

api_key = "1e1d349ae7784d1bb51fedc690f36a25"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2025-02-28&sortBy=publishedAt&apiKey=" \
      "1e1d349ae7784d1bb51fedc690f36a25"

# make a request
request = requests.get(url)

#Get a dictionary
content = request.json()

#access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])