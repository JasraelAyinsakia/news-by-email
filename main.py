import  requests
from send_email import send_email

api_key = "1e1d349ae7784d1bb51fedc690f36a25"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2025-02-28&sortBy=publishedAt&apiKey=" \
      "1e1d349ae7784d1bb51fedc690f36a25"

# make a request
request = requests.get(url)

#Get a dictionary
content = request.json()

#access the article titles and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"
body = body.encode("utf-8")
send_email(message=body)
