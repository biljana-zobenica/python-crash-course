guest_list = ['Celine Dion', 'Novak Djokovic']

#print(f'Hi {guest_list[0]}, I would like you to come to my celebration dinner.')
#print(f'Hi {guest_list[1]}, I would like you to come to my celebration dinner.')

#print(f'\n{guest_list[0]} would not make it to the celebration dinner.\n')
guest_list[0] = 'Sandra Bullock'

#print(f'Hi {guest_list[0]}, I would like you to come to my celebration dinner.')
#print(f'Hi {guest_list[1]}, I would like you to come to my celebration dinner.')

#print(f'\nHi everyone, I have just found a bigger dinner table. So, more guests will come.')

guest_list.insert(0, 'Ryan Gosling')
guest_list.insert(2, 'Jay Shetty')
guest_list.append('Eddie Murphy')

print(f'This is a new list:')
print(guest_list)

print(f'I am so happy that {len(guest_list)} guests will come to my celebration dinner!')