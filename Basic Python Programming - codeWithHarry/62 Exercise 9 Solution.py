import requests
import json


def speak(str):
    from win32com.client import Dispatch
    speaks = Dispatch("SAPI.SpVoice")
    speaks.Speak(str)


if __name__ == '__main__':
    speak("News for today.. Lets begin")
    url = "http://newsapi.org/v2/top-headlines?country=us&apiKey=a8e3" \
          "4cff68394009a9e6a477e07de89a"
    news = requests.get(url).text
    news_dict = json.loads(news)
    print(news_dict["articles"])
    arts = news_dict["articles"]
    for article in arts:
        speak(article["title"])
        speak("Moving on to the next news... Listen carefully")

    speak("Thanks for listening...")
