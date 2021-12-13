import spotipy
from spotipy import oauth2
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
PORT_NUMBER = 8080
SPOTIPY_CLIENT_ID = '69efb4fe809c40abbae3e0cf54dbb03c'
SPOTIPY_CLIENT_SECRET = 'ee16a0a613eb4aea906c98f70843bdac'
SPOTIPY_REDIRECT_URI = 'http://localhost:8080'
SCOPE = 'user-top-read user-modify-playback-state'
CACHE = '.spotipyoauthcache'

sp_oauth = oauth2.SpotifyOAuth( SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET,SPOTIPY_REDIRECT_URI,scope=SCOPE,cache_path=CACHE )

birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
kanye_uri = 'spotify:artist:5K4W6rqBFWDnAN6FQUkS6x'
token_info = sp_oauth.get_access_token()
access_token = ""
if token_info:
	print("Found cached token!")
	access_token = token_info['access_token']
else:
	print("Found Spotify auth code in Request URL! Trying to get valid access token...")
	token_info = sp_oauth.get_access_token(code)
	access_token = token_info['access_token']

print(access_token)
print(sp_oauth.validate_token(token_info))
spotify = spotipy.Spotify(access_token)
results = spotify.artist_albums(kanye_uri, album_type='album')
secondresults = spotify.artist(kanye_uri)
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])

print(secondresults)
related = spotify.artist_related_artists(kanye_uri)
for artist in related['artists']:
	name = artist['name']
	print(name)
test = spotify.current_user_top_tracks()
for song in test['items']:
	print(song['name'])
spotify.add_to_queue('spotify:track:6Hfu9sc7jvv6coyy2LlzBF')
