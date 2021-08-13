# definition of the 'make_shirt' function
def make_shirt(size = 'large', message = 'I love Python!'):
    """Displays the message which should be printed on the shirt."""
    print(f"On the {size.upper()} sized shirt, we will print this message {message}")

# make a large shirt with the default message
make_shirt('large')

# make a medium shirt with the default message
make_shirt('medium')

# make any size shirt with a new message
make_shirt(size = 'universal', message = 'Be authentic!')
