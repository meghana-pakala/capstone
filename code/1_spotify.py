
# get spotify data

import pandas as pd
import time

#pip install spotipy --upgrade
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# set personal access token for spotify api
client_id = None
client_secret = None
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

# playlists from every noise at once / sound of spotify
sound_of_playlists = ['https://open.spotify.com/playlist/6gS3HhOiI17QNojjPuPzqc', # pop - 428 songs
                      'https://open.spotify.com/playlist/2ZIRxkFuqNPMnlY7vL54uK', # dance pop - 341 songs
                      'https://open.spotify.com/playlist/6MXkE0uYF4XwU4VTtyrpfP', # hip hop - 344 songs
                      'https://open.spotify.com/playlist/6s5MoZzR70Qef7x4bVxDO1', # rap - 344 songs
                      'https://open.spotify.com/playlist/7dowgSWOmvdpwNkGFMUs6e', # rock - 509 songs
                      'https://open.spotify.com/playlist/5HufsVvMDoIPr9tGzoJpW0', # modern rock - 321 songs
                      'https://open.spotify.com/playlist/4mijVkpSXJziPiOrK7YX4M', # country - 413 songs
                      'https://open.spotify.com/playlist/0VZfpqcbBUWC6kpP1vVrvA'] # contemporary country - 380 songs

# function to return dataframe of metadata and audio features for each track in given playlist
def get_track_data(playlist_id):
    # get metadata for each track
    metadata = []
    # spotify api limits to 100 tracks, set offset to retrieve in batches
    for i in range(0, 1000, 100):
        playlist_info = sp.playlist_tracks(playlist_id, limit=100, offset=i)['items']
        for item in playlist_info:
            metadata.append({
                'id': item['track']['id'],
                'track': item['track']['name'],
                'artist': [artist['name'] for artist in item['track']['artists']],
                'album': item['track']['album']['name'],
                'release_date': pd.to_datetime(item['track']['album']['release_date']),
                'release_year': pd.to_datetime(item['track']['album']['release_date']).year,
                'length_ms': item['track']['duration_ms'],
                'explicit': item['track']['explicit'],
                'popularity': item['track']['popularity']})
    metadata_df = pd.DataFrame(metadata)
    # insert column for input playlist name
    playlist_name = sp.playlist(playlist_id)['name']
    metadata_df.insert(0, 'playlist', playlist_name)
    
    # get audio features for each track
    track_ids = metadata_df['id'].tolist()
    features = []
    for i in range(0, len(track_ids), 100):
        batch_ids = track_ids[i:i+100]
        batch_features = sp.audio_features(batch_ids)
        features.extend(batch_features)
    select_cols = ['id', 'danceability', 'energy', 'key', 'loudness', 'mode','speechiness',
                   'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']
    features_df = pd.DataFrame(features, columns=select_cols)

    # merge and return full dataframe
    playlist_df = pd.merge(metadata_df, features_df, on='id')
    return playlist_df



# ideally this should run without hitting rate limits but IDK 
for playlist in sound_of_playlists:
    df = get_track_data(playlist)
    name = df['playlist'].iloc[0]
    df.to_csv(f'{name}.csv', index=False)
    time.sleep(5)


# or run manually
pop = 'https://open.spotify.com/playlist/6gS3HhOiI17QNojjPuPzqc', # 428 songs
dance_pop = 'https://open.spotify.com/playlist/2ZIRxkFuqNPMnlY7vL54uK' # 341 songs
hip_hop = 'https://open.spotify.com/playlist/6MXkE0uYF4XwU4VTtyrpfP', # 344 songs
rap = 'https://open.spotify.com/playlist/6s5MoZzR70Qef7x4bVxDO1' # 344 songs
rock = 'https://open.spotify.com/playlist/7dowgSWOmvdpwNkGFMUs6e' # 509 songs
modern_rock = 'https://open.spotify.com/playlist/5HufsVvMDoIPr9tGzoJpW0' # 321 songs
country = 'https://open.spotify.com/playlist/4mijVkpSXJziPiOrK7YX4M' # 413 songs
contemporary_country = 'https://open.spotify.com/playlist/0VZfpqcbBUWC6kpP1vVrvA' # 380 songs

# run this for each playlist
df = get_track_data(pop) # sub in each variabele
genre = 'pop' # and title as string
df.to_csv(f'{genre}.csv', index=False)


