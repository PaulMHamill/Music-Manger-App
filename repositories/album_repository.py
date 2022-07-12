from optparse import Values
from unittest import result
from db.run_sql import run_sql
from models.album import Album
from models.artist import Artist
import repositories.artist_repository as artist_repository

def create(album):
    sql = """
    INSERT INTO album (title, genre, artist_id)
    VALUES (%s, %s, %s)
    RETURNING *
    """
    values = [album.title, album.genre, album.artist]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album