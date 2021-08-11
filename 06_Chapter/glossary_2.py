glossary = {
    'variable':'used to assign labels to values',
    'string':'a series of characters, surrounded by single or double quotes',
    'f-string':'a format string which allows to use variables inside strings to build dynamic messages', 
    'list':'a series of items which are stored in a particular order',
    'tuple':'similar to lists, but the items in a tuple can not be modified',
    'dictionary':'a collection of connected pieces of information in a form of key-value pairs',
    'conditional test':'a comparison between two values',
    'float':'a numerical value with a decimal component',
    'key':'the first item in a key-value pair in a dictionary',
    'value':'an item associated with a key in a dictionary',
    'boolean expression':'an expression that evaluates to True or False',
    }

for word, definition in glossary.items():
    print(f"{word.title()}: {definition}.")