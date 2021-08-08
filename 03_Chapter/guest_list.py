guest_list = ['Celine Dion', 'Novak Djokovic']

print(f'Hi {guest_list[0]}, I would like you to come to my celebration dinner.')
print(f'Hi {guest_list[1]}, I would like you to come to my celebration dinner.')

print(f'\n{guest_list[0]} would not make it to the celebration dinner.\n')
guest_list[0] = 'Sandra Bullock'

print(f'Hi {guest_list[0]}, I would like you to come to my celebration dinner.')
print(f'Hi {guest_list[1]}, I would like you to come to my celebration dinner.')

print(f'\nHi everyone, I have just found a bigger dinner table. So, more guests will come.')

guest_list.insert(0, 'Ryan Gosling')
guest_list.insert(2, 'Jay Shetty')
guest_list.append('Eddie Murphy')

print(f'\n This is a new list:')
print(guest_list)

print(f'\nHi {guest_list[0]}, I would like you to come to my celebration dinner.')
print(f'Hi {guest_list[1]}, I would like you to come to my celebration dinner.')
print(f'Hi {guest_list[2]}, I would like you to come to my celebration dinner.')
print(f'Hi {guest_list[3]}, I would like you to come to my celebration dinner.')
print(f'Hi {guest_list[4]}, I would like you to come to my celebration dinner.')

print(f"\nUnfortunately, my new dinner table won't be delivered on time. I can invite only two guests.\n")
print(f"{guest_list[0]}, I am sorry, but I can't invite you to dinner.")
guest_list.pop(0)

print(f"{guest_list[0]}, I am sorry, but I can't invite you to dinner.")
guest_list.pop(0)

print(f"{guest_list[0]}, I am sorry, but I can't invite you to dinner.")
guest_list.pop(0)

print(f"\n{guest_list[0]}, you are still invited!")
print(f"{guest_list[1]}, you are still invited!")

print(guest_list)
del guest_list[0]
del guest_list[1]
print(guest_list)