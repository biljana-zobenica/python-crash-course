glossary = {
    'variable':'used to assign labels to values',
    'string':'a series of characters, surrounded by single or double quotes',
    'f-string':'a format string which allows to use variables inside strings to build dynamic messages', 
    'list':'a series of items which are stored in a particular order',
    'tuple':'similar to lists, but the items in a tuple can not be modified',
    'dictionary':'a collection of connected pieces of information in a form of key-value pairs',
    }

word = 'variable'
print(f"{word.title()} is {glossary[word]}.")
word = 'string'
print(f"{word.title()} is {glossary[word]}.")
word = 'f-string'
print(f"{word.title()} is {glossary[word]}.")
word = 'list'
print(f"{word.title()} is {glossary[word]}.")
word = 'tuple'
print(f"{word.title()} is {glossary[word]}.")
word = 'dictionary'
print(f"{word.title()} is {glossary[word]}.")