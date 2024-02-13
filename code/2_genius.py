# scrape genius lyrics  

import pandas as pd
from tqdm import tqdm

#!pip install lyricsgenius
import lyricsgenius

# set personal access token for genius api
token = None
genius = lyricsgenius.Genius(token, timeout=30, retries=2, verbose=False)

# function to scrape lyrics given dataframe with track and artist columns
def get_genius_lyrics(df):
    lyrics_list = []
    for index, row in tqdm(df.iterrows(), total=len(df), desc='Genius Lyrics Search'):
        track = row['track']
        artist = row['artist']
        try:
            track_id = genius.search_song(track, artist=artist).id
            lyrics = genius.lyrics(track_id, remove_section_headers=False)
            lyrics_list.append(lyrics)
        except Exception as e:
            print(f"Error processing track {track}: {e}")
            lyrics_list.append(None)
    df['lyrics'] = lyrics_list
    return df


# each genre takes ~30 min to scrape

# pop
pop_1 = pd.read_csv('../data/sound_of/pop.csv') # 428 songs
pop_2 = pd.read_csv('../data/sound_of/dance_pop.csv') # 341 songs
pop_df = (pd.concat([pop_1, pop_2])
          .drop_duplicates(subset='id')
          .rename(columns={'playlist':'genre'})
          .assign(genre='pop'))
get_genius_lyrics(pop_df)
pop_df.to_csv('../data/pop_lyrics.csv')

# hip hop
hiphop_1 = pd.read_csv('../data/sound_of/hip_hop.csv') # 344 songs
hiphop_2 = pd.read_csv('../data/sound_of/rap.csv') # 344 songs
hiphop_df = (pd.concat([hiphop_1, hiphop_2])
             .drop_duplicates(subset='id')
             .rename(columns={'playlist':'genre'})
             .assign(genre= 'hip hop'))
get_genius_lyrics(hiphop_df)
hiphop_df.to_csv('../data/hiphop_lyrics.csv')

# rock
rock_1 = pd.read_csv('../data/sound_of/rock.csv') # 509 songs
rock_2 = pd.read_csv('../data/sound_of/modern_rock.csv') # 321 songs
rock_df = (pd.concat([rock_1, rock_2])
          .drop_duplicates(subset='id')
          .rename(columns={'playlist':'genre'})
          .assign(genre= 'rock'))
get_genius_lyrics(rock_df)
rock_df.to_csv('../data/rock_lyrics.csv')

# country
country_1 = pd.read_csv('../data/sound_of/country.csv') # 413 songs
country_2 = pd.read_csv('../data/sound_of/contemporary_country.csv') # 380 songs
country_df = (pd.concat([country_1, country_2])
              .drop_duplicates(subset='id')
              .rename(columns={'playlist':'genre'})
              .assign(genre= 'country'))
get_genius_lyrics(country_df)
country_df.to_csv('../data/country_lyrics.csv')


# reimport
pop_df = pd.read_csv('../data/sound_of/pop_lyrics.csv', index_col=0)
hiphop_df = pd.read_csv('../data/sound_of/hiphop_lyrics.csv', index_col=0)
rock_df = pd.read_csv('../data/sound_of/rock_lyrics.csv', index_col=0)
country_df = pd.read_csv('../data/sound_of/country_lyrics.csv', index_col=0)

# merge genre dataframes and drop nulls
df = (pd.concat([pop_df, hiphop_df, rock_df, country_df], 
                ignore_index=True)
      .dropna(subset=['lyrics']))

# export combined data
df.to_csv('../data/lyrics_data.csv')

