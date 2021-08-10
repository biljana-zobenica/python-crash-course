players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(f'The first three items in the list are:')
for player in players[:3]:
    print(player.title())

print(f'\nThree items from the middle of the list are:')
for player in players[1:4]:
    print(player.title())

print(f'\nThe last three items in the list are:')
for player in players[-3:]:
    print(player.title())
