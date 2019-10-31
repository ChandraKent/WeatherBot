#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
import tweepy
import time
import json
import random
import requests as req
import datetime
import sys
import os

sys.path.append("../..")

consumer_key = os.environ.get("consumer_key")
consumer_secret = os.environ.get("consumer_secret")
access_token = os.environ.get("access_token")
access_token_secret = os.environ.get("access_token_secret")
weather_api_key = os.environ.get("weather_api_key")


# In[2]:


## Twitter API Keys
consumer_key = consumer_key
consumer_secret = consumer_secret
access_token = access_token
access_token_secret = access_token_secret


# In[3]:


# Weather API Key
#3df5bc1f742478ec52ffedc003c6955c


# In[4]:


# Create a function that gets the weather in London and Tweets it
def WeatherTweet():

    # Construct a Query URL for the OpenWeatherMap
    url = "http://api.openweathermap.org/data/2.5/weather?"
    city = "Washington, D.C."
    units = "imperial"
    query_url = url + "appid=" + weather_api_key + "&q=" + city + "&units=" + units

    # Perform the API call to get the weather

    weather_response = req.get(query_url)
    weather_json = weather_response.json()
    print(weather_json)
   
    # Twitter credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_acess_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    # Tweet the weather
    api_update_status("Weather in Washington D.C.:" +                      (dateime.dateime.now().strftime("%I:%M %p")+" " +                       str(weather_json["main"]["temp"])+"F"))
        

    # Print success message
    print("Tweeted succesfully!")


# In[5]:


# Set timer to run every 1 hour
while(True):
    WeatherTweet()
    time.sleep(3600)


# In[ ]:




