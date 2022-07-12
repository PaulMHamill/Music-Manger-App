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
    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def delete_all():
    sql = """
    DELETE FROM album"""
    run_sql(sql)

def select(id):
    albums = None
    sql = """SELECT * FROM album WHERE id = %s;"""
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        artist = artist_repository.select(result['artist_id'])
        albums = Album(result['title'], result['genre'], artist, result['id'])
    return albums


def selcet_all():
    albums = []
    sql = """SELECT * FROM album"""
    results = run_sql(sql)

    for row in results:
        artist = artist_repository.select(row['artist_id'])
        album = Album(row['title'], row['genre'], artist, row['id'])
        albums.append(album)
    return albums

def select_by_artist(artist):
    albums = []
    sql = """SELECT * FROM album WHERE artist_id = %s;"""
    values = [artist.id]
    results = run_sql(sql, values)

    for row in results:
        
        album = Album(row['title'], row['genre'], artist, row['id'])
        albums.append(album)
        
    return albums
