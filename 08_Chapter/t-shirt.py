# definition of the 'make_shirt' function
def make_shirt(size, message):
    """Displays the message which should be printed on the shirt."""
    print(f"On the {size.upper()} sized shirt, we will print this message {message}")

# call the function by using positional arguments
make_shirt('m', 'Keep calm and just smile!')

# call the function by using keyword arguments
make_shirt(message = 'Be brave!', size = 'xl')
