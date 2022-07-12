import imp
import pdb
from pyexpat import model
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

artist1 = Artist("Guns and Roses")
artist_repository.create(artist1)

album1 = Album("Appetite for Destruction", "Rock", 1)
album_repository.create(album1)



# for thing in result:
#     print(thing.__dict__)

pdb.set_trace()