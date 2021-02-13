import requests
import urllib.parse 
import json

#search song and return uri
def get_spotify_uri(token, song, artist):
    query = urllib.parse.quote(f'{song}')
    url = f"https://api.spotify.com/v1/search?q={query}&type=track"
    response = requests.get(
        url,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }
    )
    response_json = response.json()
    results = response_json['tracks']['items']
    if results:
        return results[0]['uri']
    else:
        return None

#creating a new Playlist name "New Automated Playlist"
def createPlaylistSpotify(token,user_id):
    request_body = json.dumps({
        "name": "01.12.2020",
        "description": "New playlist description",
        "public": False
    })
    
    url = f"https://api.spotify.com/v1/users/{user_id}/playlists"
    response = requests.post(
        url,
        data=request_body,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }
    )
    response_json = response.json()
    return response_json['id']

#adding songs to playlist 
def add_song_playlist(token,song_dic,user_id):
    playlist_id = createPlaylistSpotify(token,user_id)
    uris = []
    for song in song_dic:
        spotify_url = get_spotify_uri(token,song['song_name'], song['artist'])
        if(spotify_url!=None):
            print(song,"added")
            uris.append(spotify_url)

    request_data = json.dumps(uris)
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    response = requests.post(
        url,
        data=request_data,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }
    )
    response_json = response.json()
    return response_json