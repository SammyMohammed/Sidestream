import spotipy
import sys
import spotipy.util as util
import operator #referenced Ajisten on stackoverlow

scope = "user-library-read"
token = util.prompt_for_user_token("sammymohammed",scope,client_id='',client_secret='',redirect_uri='http://localhost/')

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
        #print tracks
        while results['next']:
            results = spotify.next(results)
            tracks.extend(results['items'])
        songids = []
        songnames = []
        for track in tracks:
            #print(track['name'])
            songnames.append(track['name'])
            id = track['id']
            if id not in songids:
                #print('id: ' + id)
                songids.append(id)
            # print()
            # print songids
            #print(track)
    songpops = []
    for id in songids:
        print spotify.track(id)['name'] +  " " + str(spotify.track(id)['popularity'])
        songpops.append(spotify.track(id)['popularity'])
    keys = songnames
    values = songpops #referenced stackoverlow for merging the two lists into a dict
    popularitydict = dict(zip(keys, values))
    sorted_popularity = sorted(popularitydict.items(), key=operator.itemgetter(1))
    print(sorted_popularity[0])
    #learning the lovely zip

get_artist()
