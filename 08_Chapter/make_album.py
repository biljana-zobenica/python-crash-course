def make_album (artist_name, album_name, songs=None):
    """Return a dictionary of information about an album."""
    info = {'artist':artist_name, 'album':album_name}
    if songs:
        info['songs'] = songs.title()
    return info

album = make_album('queen', 'made in heaven', 'i was born to love you')
print (album)
