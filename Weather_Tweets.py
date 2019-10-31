

# #!/usr/bin/env python
# coding: utf-8
​
# In[6]:
​
​
# Dependencies
import os
import tweepy
import time
import json
import random
import requests as req
import datetime
consumer_key = os.environ.get("consumer_key")
consumer_secret = os.environ.get("consumer_secret")
access_token = os.environ.get("access_token")
access_token_secret = os.environ.get("access_token_secret")
weather_api_key = os.environ.get("weather_api_key")
​
# In[7]:
​
​
​
​
# In[8]:
​
​
# Weather API
# weather_api_key
​
​
# In[9]:
​
​
# Create a function that gets the weather in London and Tweets it
def WeatherTweet():
​
    # Construct a Query URL for the OpenWeatherMap
    url = "http://api.openweathermap.org/data/2.5/weather?"
    city = "Washington, D.C."
    units = "imperial"
    query_url = url + "appid=" + weather_api_key + "&q=" + city + "&units=" + units
    print(query_url)
​
    # Perform the API call to get the weather
    weather_response = req.get(query_url)
    weather_json = weather_response.json()
    print(weather_json)
​
    # Twitter credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
​
    # Tweet the weather
    api.update_status(
        "Hello World! Weather in Washington D.C.:" +\
        (datetime.datetime.now().strftime("%I:%M %p") + " " +\
         str(weather_json["main"]["temp"])+"F"))
​
    # Print success message
    print("Tweeted successfully!")
​
​
# In[ ]:
​
​
# Set timer to run every 1 minute
while(True):
    WeatherTweet()
    time.sleep(60)
Collapse








Message #class-activities-mon-wed


About this channel


