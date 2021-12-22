![banner_image](./README_imgs/banner.jpg)

# Twitter Sentiment Streamlit Webapp
This webapp assigns a sentiment score to trending hashtags(#) or topics on Twitter. The overall score is assigned via [VADER](https://www.nltk.org/howto/sentiment.html), and the various components that make up the score can also be analyzed. 

The tweets/data is pulled using [Tweepy/Twitter API](https://www.tweepy.org/).

Contents
======
- [Twitter Sentiment Streamlit Webapp](#twitter-sentiment-streamlit-webapp)
- [Contents](#contents)
  - [Why?](#why)
  - [Tech Used](#tech-used)
  - [Installation](#installation)
  - [Features](#features)
  - [Want to Contribute?](#want-to-contribute)

## Why? 
The motivations for this web-app are:

- get the true meaning of people's statements on trending topics
- view how the public's opinion changes throughout a week's time
- experiment how the public reacts to topics that are worded differently 

## Tech Used
 - [Tweepy/Twitter API](https://www.tweepy.org/)
 - [Pandas](https://pandas.pydata.org/)
 - [Plotly](https://plotly.com/)
 - [Altair](https://altair-viz.github.io/index.html)
 - [StreamLit](https://streamlit.io/)

## Installation 
1. Sign up for Twitter Developer account and insert your `CONSUMER KEY`, `CONSUMER SECRET`, `ACCESS TOKEN`, and `ACCESS TOKEN SECRET` in `creds.py`

2.  Clone the repo `$ git clone https://github.com/JP-sDEV/twitter_sentiment_streamlit.git`

3. `cd` into the root of the project
4. Create a virtual environment `python3 -m venv /path/to/new/virtual/environment`
	- [Virtual environments in Python](https://docs.python.org/3/library/venv.html)
5. Install with `pip3`
    - `$ pip3 install requirements.txt`

6. Run app locally with `streamlit run main.py`

## Features
- input any trending hashtag(#) or topic/word to view the public's opinion 
- view the score(s)
  - with their respective distibutions
  - week distribution
- choose the types of tweets to analyze
  - popular tweets
  - recent tweets
  - mixed (popular + recent tweets)

<img src="./README_imgs/demo.gif" width="80%">

## Want to Contribute?
1. Clone the repo by following [Installation](#Installation)
2. Improve the web-app by:
	- add a feature
	- resolving an issue in the [Issues](https://github.com/JP-sDEV/twitter_sentiment_streamlit/issues) tab
	- refactor code
3. Test the new feature locally
4. Update the Features section in the README.md
5. Open a pull request with a detailed explanation of the changes
