import pdb
from pyexpat import model
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

# artist1 = Artist("Guns and Roses")
# artist_repository.create(artist1)

# album1 = Album("Appetite for Destruction", "Rock", artist1)
# album_repository.create(album1)

# album = album_repository.select(7)
# artist = artist_repository.select(7)
# print(album.__dict__)
# print(artist.__dict__)
# album_repository.delete_all()
# artist_repository.delete_all()

result_album = album_repository.selcet_all()
result_artist = artist_repository.select_all()

for album in result_album:
    print(album.__dict__)

for artist in result_artist:
    print(artist.__dict__)

pdb.set_trace()