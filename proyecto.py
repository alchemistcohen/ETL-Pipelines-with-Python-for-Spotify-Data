import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd 
import pandasql as ps

client_id = 'dce0c8c8030a4d90bc10df2326796256'
client_secret = '98baff833a7c4e76b632004d65c6312e'

client_credentials_manager = SpotifyClientCredentials(client_id = client_id, client_secret = client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#https://open.spotify.com/playlist/37i9dQZEVXbL0GavIqMTeb?si=r2V1xIrISc-ou555mmIEYQ
#https://open.spotify.com/playlist/37i9dQZEVXbNLrliB10ZnX?si=mUoeo21QS9GOnq2iiHDvhQ
#https://open.spotify.com/playlist/37i9dQZEVXbOa2lmxNORXQ?si=WyVnD2GLSneotQXofhM_Eg
#https://open.spotify.com/playlist/37i9dQZEVXbO3qyFxbkOE1?si=sygeWYaVSkKiBktgJBtE7A
#https://open.spotify.com/playlist/37i9dQZEVXbMMy2roB9myp?si=4bMcdcMJTXO_ph7sKobHVQ
#https://open.spotify.com/playlist/37i9dQZEVXbJfdy5b0KP7W?si=HbrwsUr7RfSRA2wFaTgw0A
#https://open.spotify.com/playlist/1RaCS1KEq4x2UPAQFmWpZK?si=dz505R-zSPi3YmI16V6zbg

playlists = {
    '37i9dQZEVXbL0GavIqMTeb' : 'Chile',
    '37i9dQZEVXbNLrliB10ZnX' : 'Venezuela',
    '37i9dQZEVXbOa2lmxNORXQ' : 'Colombia',
    '37i9dQZEVXbO3qyFxbkOE1' : 'Mexico',
    '37i9dQZEVXbMMy2roB9myp' : 'Argentina',
    '37i9dQZEVXbJfdy5b0KP7W' : 'Peru',
    '1RaCS1KEq4x2UPAQFmWpZK' : 'El Salvador'
}

tracks_data = []


#Iteramos sobre cada playlist

for playlist_id, country in playlists.items():
    results = sp.playlist_tracks(playlist_id)
    for i, item in enumerate(results['items']):
        track = item['track']
        track_info = {
            'PosiciÃ³n': i + 1,
            'Nombre de la canciÃ³n': track['name'],
            'Artista(s)': ', '.join([artist['name'] for artist in track['artists']]),
            'Popularidad': track['popularity'],
            'PaÃ­s': country
        }
        tracks_data.append(track_info)

#Crear dataframe

df_tracks = pd.DataFrame(tracks_data)
#df_tracks.to_csv('top_tracks_latam.csv', index = False)

query = """
SELECT * FROM df_tracks
WHERE PaÃ­s IN ('Chile', 'Venezuela', 'Colombia', 'Mexico', 'Argentina', 'Peru', 'El Salvador' )
AND PosiciÃ³n IN (1, 2, 3)
ORDER BY PaÃ­s, PosiciÃ³n

"""

top_3_sql = ps.sqldf(query, locals())

nombre_del_archivo = 'Top_3_Latinoamerica.csv'
top_3_sql.to_csv(nombre_del_archivo, index= False)
print(top_3_sql)