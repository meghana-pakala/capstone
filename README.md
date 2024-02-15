# AnaLyrics Engine: Predicting Music Genres with NLP
Meghana Pakala
February 2024

## Business Understanding
This project leverages song lyrics and metadata to classify songs into distinct music genres. Genre classification is not an exact science, and given the vast diversity of music today, there are innumerable categories a song could belong to.

As a passionate music lover and avid concert goer, I tend to have a curated playlist for every possible mood and occassion. This is a tedious task to do manually, and I have often thought how nice it would be to be able to input my current mood and desired music style (ex: sad bangers) and have a playlist made personally for me.

Spotify has attempted to do this with their [daylist](https://newsroom.spotify.com/2023-09-12/ever-changing-playlist-daylist-music-for-all-day/)- a personalized playlist that "ebbs and flows with unique vibes, bringing together the niche music and microgenres you usually listen to during particular moments in the day or on specific days of the week."

The daylist updates organically throughout the day and is based on your past listening habits. This project attempts to build on that concept by curating a playlist based on a user's desired vibe. In order to get to an end goal of song recommendations based on lyrics and audio features, the first step was to build a supervised model trained to predict a song's genre based purely on the words it contains.

## Data Collection

The first step in building the dataset was identifying the prediction target- music genres. [Every Noise At Once](https://everynoise.com/engenremap.html) is “an ongoing attempt at an algorithmically-generated, readability-adjusted scatter-plot of the musical genre-space." The project was created in 2013 by Glenn McDonald, a former Spotify developer, based on data tracked and analyzed for ~6000 Spotify genres. (last updated November 2023)

The songs for each genre were collected from the playlists provided by the Every Noise project, and all of the song metadata and audio features were gathered using [Spotipy](https://spotipy.readthedocs.io/en/2.22.1/), a Python wrapper for the [Spotify API](https://developer.spotify.com/documentation/web-api). Next, lyrics for each song were scraped from [Genius](https://genius.com) using [LyricsGenius](https://lyricsgenius.readthedocs.io/en/master/reference/genius.html). The Python code for this data collection is available [here](/code).

To prepare the data for modeling, we performed preprocessing steps such as text cleaning, tokenization, and vectorization of lyrics. The text cleaning process before model preprocessing is outined in the [data cleaning](code/data_cleaning) notebook.

After combining all the data and dropping bad records, we were left with 2024 songs.

## Modeling & Evaluation
We then trained various models including Naive Bayes and Random Forests on the labeled dataset. Using grid search and cross-validation techniques we tuned the paramaters to minimize observed overfitting.





