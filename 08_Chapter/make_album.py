def make_album (artist_name, album_name):
    """Return a dictionary of information about an album."""
    info = {'artist':artist_name, 'album':album_name}
    return info

album = make_album('queen', 'made in heaven')
print (album)
