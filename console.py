import pdb
from pyexpat import model
from unittest import result
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

# artist1 = Artist("Guns and Roses")
# artist_repository.create(artist1)

# album1 = Album("Appetite for Destruction", "Rock", artist1)
# album_repository.create(album1)

artist2 = Artist("Nirvana")
artist_repository.create(artist2)
album2 = Album("Nevermind", "Rock", artist2)
album_repository.create(album2)
album3 = Album("In Utero", "Rock", artist2)
album_repository.create(album3)

# album = album_repository.select(7)
# artist = artist_repository.select(7)
# print(album.__dict__)
# print(artist.__dict__)
# album_repository.delete_all()
# artist_repository.delete_all()

# result_album = album_repository.selcet_all()
# result_artist = artist_repository.select_all()
# artist2 = artist_repository.select(2)
result_album = album_repository.select_by_artist(artist2)

for album in result_album:
    print(album.__dict__)

# print(artist2)

# for artist in result_artist:
#     print(artist.__dict__)

pdb.set_trace()