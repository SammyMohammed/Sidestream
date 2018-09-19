import spotipy
import sys
import spotipy.util as util

scope = "user-library-read"
token = util.prompt_for_user_token("sammymohammed",scope,client_id='',client_secret='',redirect_uri='http://localhost/')

spotify = spotipy.Spotify(auth=token) #creating a Spotify object




artist = raw_input("What artist's least popular song do you want to see?" )
results = spotify.search(q='artist:' + artist, type='artist')
print results
