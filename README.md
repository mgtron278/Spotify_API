
# Spotify API Data Retrieval and Analysis.

This project aims to demonstrate how to use the Spotify API to retrieve data about trending music playlists, analyze the retrieved data, and save it to an Excel file.

## Overview

The project consists of two main parts:

1. **Authorization**: Obtaining an access token from the Spotify API using client credentials flow.
2. **Data Retrieval and Analysis**: Fetching data from a specified Spotify playlist, extracting relevant information about each track, including audio features, and saving it to an Excel file.
3. 
## Requirements

- Python 3.x
- Required libraries: `requests`, `base64`, `pandas`, `spotipy`

## Setup

1. Install the required libraries:
   ```
   pip install requests base64 pandas spotipy
   ```

2. Obtain your Spotify API credentials (client ID and client secret) from the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).

3. Update the `client_id` and `client_secret` variables in the script with your credentials.

4. Specify the `playlist_id` of the Spotify playlist you want to analyze.

## Usage

Run the script `spotify_data_analysis.py`:

```
python spotify_data_analysis.py
```

The script will retrieve data from the specified playlist, analyze it, and save the results to an Excel file.

## Output

The script generates an Excel file containing the following information for each track:

- Track Name
- Artists
- Album Name
- Album ID
- Track ID
- Popularity
- Release Date
- Duration (ms)
- Explicit
- External URLs
- Danceability
- Energy
- Key
- Loudness
- Mode
- Speechiness
- Acousticness
- Instrumentalness
- Liveness
- Valence
- Tempo

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
