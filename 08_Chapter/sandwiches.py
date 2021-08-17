def make_sandwich(*items):
    """Make a sandwich with desired items picked by a user."""
    print("I will make a sandwich for you, please pick your items:")
    for item in items:
        print(f"{item} has been added. Go ahead.")
    print("Your sandwich is ready. Bon apetit!")

make_sandwich('pepperoni', 'origano', 'tomato')
make_sandwich('pepperoni', 'origano', 'tomato', 'pickles', 'chili')
