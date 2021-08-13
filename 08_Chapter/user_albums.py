# function make_album + songs
def make_album (artist_name, album_name, songs=None):
    """Return a dictionary of information about an album."""
    info = {'artist':artist_name, 'album':album_name}
    if songs:
        info['songs'] = songs.title()
    return info

# prompts for a user
album = '\nWhat album are you fond of? '
artist = "Who's the artist? "

# quit
print ("Enter 'quit' to exit the program.")

while True:
    album_name = input(album)
    if album_name == 'quit':
        break
    artist_name = input(artist)
    if artist_name == 'quit':
        break

    result = make_album(artist_name, album_name)
    print (result)
