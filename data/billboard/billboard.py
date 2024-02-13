# scrape billboard music for annual song charts

import requests
from bs4 import BeautifulSoup
import pandas as pd

# function to get billboard hot 100 songs
def scrape_billboard(year):
    url = f'https://www.billboard.com/charts/year-end/{year}/hot-100-songs'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    # create lists containing song rankings and artists
    chart_items = soup.find_all('span', class_='c-label')
    chart_text = [item.get_text(strip=True) for item in chart_items]
    rankings = [text for text in chart_text if text.isnumeric()]
    artists = [text for text in chart_text if not text.isnumeric()]
    # create list containing song titles    
    song_titles = soup.find_all('h3', class_='c-title')
    songs = [song.get_text(strip=True) for song in song_titles]
    # set limit to remove extra h3 page headers
    songs = songs[:len(artists)]
    # return as dataframe
    chart_df = pd.DataFrame({'rank': rankings, 'track': songs, 'artist': artists})
    return chart_df

# get all available charts and combine in dataframe
billboard_charts = []
for year in range(2006, 2024):
    chart_df = scrape_billboard(year)
    billboard_charts.append(chart_df)

billboard_df = pd.concat(billboard_charts, ignore_index=True)

# export to csv
billboard_df.to_csv('../data/billboard_charts.csv', index=False)