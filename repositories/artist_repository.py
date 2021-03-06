from optparse import Values
from unittest import result
from db.run_sql import run_sql
from models.album import Album
from models.artist import Artist


def create(artist):
    sql = """
    INSERT INTO artist (name)
    VALUES (%s)
    RETURNING *
    """
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

def delete_all():
    sql = """
    DELETE FROM Artist"""
    run_sql(sql)

def select(id):
    artists = None
    sql = """SELECT * FROM artist WHERE id = %s;"""
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        artists = Artist(result['name'], result['id'])
    return artists

def select_all():
    artists = []

    sql = """
    SELECT * FROM artist
    """
    results = run_sql(sql)

    for row in results:
        artist = Artist(row['name'], row['id'])
        artists.append(artist)
    return artists
