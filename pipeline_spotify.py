import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd 

client_id = 'dce0c8c8030a4d90bc10df2326796256'
client_secret = '98baff833a7c4e76b632004d65c6312e'

client_credentials_manager = SpotifyClientCredentials(client_id = client_id, client_secret = client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

nombre_artista = 'Canserbero'
resultado = sp.search(q='artist: ' + nombre_artista, type='artist')

artistas = resultado['artists']['items']

lista_artistas = []

for artista in artistas:
    nombre = artista['name']
    popularidad = artista['popularity']
    seguidores = artista['followers']['total']
    lista_artistas.append([nombre, popularidad, seguidores])

#Creamos el dataframe

df_artistas = pd.DataFrame(lista_artistas, columns=['nombre', 'popularidad', 'seguidores'])
print(df_artistas)