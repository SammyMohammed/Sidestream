import spotipy
import sys
import spotipy.util as util

scope = "user-library-read"
token = util.prompt_for_user_token("sammymohammed",scope,client_id='ff3d8adb2922425888f320204ee7d6b2',client_secret='96ff1baac76a4d05861239f3aecb6138',redirect_uri='http://localhost/')

spotify = spotipy.Spotify(auth=token) #creating a Spotify object


def get_artist():
    artist = raw_input("What artist's least popular song do you want to see? ")
    results = spotify.search(q='artist:' + artist, type='artist')
    items = results['artists']['items']
    if (len(items) > 0):
        #print items[0]
        artist = items[0]
    else:
        return None
    #album code used spotipy documentation as reference
    albums = []
    albumresults = spotify.artist_albums(artist['id'], album_type ='album')
    #print albumresults
    albums.extend(albumresults['items'])
    while albumresults['next']:
        albumresults = spotify.next(albumresults) #.next is used to switch to the next item in the list, it seems
        albums.extend(albumresults['items'])
    seen = set()
    for album in albums:
        name = album['name']
        if name not in seen:
            print(' ' + name)
            seen.add(name)

    tracks = []
    for album in albums:

        results = spotify.album_tracks(album['id'])
        #print results
        tracks.extend(results['items'])
        print tracks
        while results['next']:
            results = spotify.next(results)
            tracks.extend(results['items'])
        for track in tracks:
            print('  ', track['name'], track['popular'])
            print()
            #print(track)

get_artist()
