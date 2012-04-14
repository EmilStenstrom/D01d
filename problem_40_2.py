import requests

#tweets = "https://api.twitter.com/1/statuses/user_timeline.json?screen_name=EmilStenstrom&count=1000"
tweets = "http://search.twitter.com/search.json?q=hej&rpp=100"
response = requests.get(tweets)
f = open("last_1000.json", "r+")
f.write(response.content)

