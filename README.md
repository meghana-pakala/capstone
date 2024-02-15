# AnaLyrics Engine: Predicting Music Genres with NLP
- This project leverages song lyrics and metadata to classify songs into distinct music genres.
- The dataset is comprised of ~2000 songs distributed across 4 genres: pop, rock, hip-hop, and country.

**Data Understanding**

The first step in building the dataset was identifying the prediction target- music genres. [Every Noise At Once](https://everynoise.com/engenremap.html) is “an ongoing attempt at an algorithmically-generated, readability-adjusted scatter-plot of the musical genre-space." The project was created in 2013 by Glenn McDonald, a former Spotify developer, based on data tracked and analyzed for ~6000 Spotify genres. (last updated November 2023)

The songs for each genre were collected from the playlists provided by the Every Noise project, and all of the song metadata and audio features were gathered using [Spotipy](https://spotipy.readthedocs.io/en/2.22.1/), a Python wrapper for the [Spotify API](https://developer.spotify.com/documentation/web-api). Next, lyrics for each song were scraped from [Genius](https://genius.com) using [LyricsGenius](https://lyricsgenius.readthedocs.io/en/master/reference/genius.html).

After combining all the data and dropping bad records, we were left with 2024 songs.


**Modeling**

To prepare the data for modeling, we performed preprocessing steps such as text cleaning, tokenization, and vectorization of lyrics. The full cleaning process is outined in the [data cleaning](code/data_cleaning) notebook.

We then trained various models including Naive Bayes and Random Forests on the labeled dataset. Using grid search and cross-validation techniques we tuned the paramaters to minimize observed overfitting.
