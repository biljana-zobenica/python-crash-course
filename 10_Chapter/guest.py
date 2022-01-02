name = input("What is your name? ")

#filename = 'guest.txt'

with open ('10_Chapter/guest.txt', 'w') as n:
    n.write(name)