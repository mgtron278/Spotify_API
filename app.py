import requests
import base64

client_id = "92f7429968514a389eaa3072be714d5f"
client_secret = "91d0b3d67a644c228699c24bab0a26c2"

client_credentials =  f"{client_id}:{client_secret}"

client_credentials_base64 = base64.b64encode(client_credentials.encode())

#
token_url = 'https://accounts.spotify.com/api/token'
headers = {
    'Authorization': f'Basic {client_credentials_base64.decode()}'}

data = {'grant_type': 'client_credentials'}

response = requests.post(token_url, data=data, headers=headers)

if response.status_code==200:
    access_token = response.json()['access_token']
    print("succesfull")
else: 
    print("not successfull")
    exit()


import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def get_tredning_playlist(playlist_id, access_token):
    sp = spotipy.Spotify(auth=access_token)

    playlist_tracks = sp.playlist_tracks(playlist_id, fields='items(track(id,name,artists,album(id,name)))')

    music_tracks=[]

    for track_info in playlist_tracks['items']:
        track = track_info['track']
        track_name = track['name']
        artists = ','.join([artist['name'] for artist in track['artists'] if artist.get('name') is not None])

        album_name = track["album"]["name"]
        album_id = track['album']['id']
        track_id = track['id']

        audio_features = sp.audio_features(track_id)[0]if track_id != 'Not available' else None
        
        try:
            album_info = sp.album(album_id) if album_id != 'Not available' else None
            release_date = album_info['release_date'] if album_info else None
        except:
            release_date = None


        # get popularity of the track
        try:
            track_info = sp.track(track_id) if track_id != 'Not available' else None
            popularity = track_info['popularity'] if track_info else None
        except:
            popularity = None

        
            track_info = sp.track(track_id) if track_id != 'Not available' else None
            popularity = track_info['popularity'] if track_info else None
   
        # add additional track information to the track data
        track_data = {
            'Track Name': track_name,
            'Artists': artists,
            'Album Name': album_name,
            'Album ID': album_id,
            'Track ID': track_id,
            'Popularity': popularity,
            'Release Date': release_date,
            'Duration (ms)': audio_features['duration_ms'] if audio_features else None,
            'Explicit': track_info.get('explicit', None),
            'External URLs': track_info.get('external_urls', {}).get('spotify', None),
            'Danceability': audio_features['danceability'] if audio_features else None,
            'Energy': audio_features['energy'] if audio_features else None,
            'Key': audio_features['key'] if audio_features else None,
            'Loudness': audio_features['loudness'] if audio_features else None,
            'Mode': audio_features['mode'] if audio_features else None,
            'Speechiness': audio_features['speechiness'] if audio_features else None,
            'Acousticness': audio_features['acousticness'] if audio_features else None,
            'Instrumentalness': audio_features['instrumentalness'] if audio_features else None,
            'Liveness': audio_features['liveness'] if audio_features else None,
            'Valence': audio_features['valence'] if audio_features else None,
            'Tempo' : audio_features['tempo'] if audio_features else None,
        }

        music_tracks.append(track_data)
    df = pd.DataFrame(music_tracks)

    path = r"C:\Users\surya\Desktop\Kaggle\spotify_api\output.xlsx"
    return df.to_excel(path, index = False)

playlist_id ="0avYchjv4qqkt4bvj9PDyj"


music_eda = get_tredning_playlist(playlist_id,access_token)
