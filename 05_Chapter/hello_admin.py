# hello messages to the users
usernames = ['biksa', 'admin', 'eddie', 'spark', 'charlie']

if usernames == []:
    print(f'We need to find some users!')
else:
    for user in usernames:
        if user == 'admin':
            print(f'Hello admin, would you like to see a status report?')
        else:    
            print(f'Hello {user}, thank you for logging in again.')

# check that the code works when the list is empty
usernames = []

if usernames == []:
    print(f'We need to find some users!')
else:
    for user in usernames:
        if user == 'admin':
            print(f'Hello admin, would you like to see a status report?')
        else:    
            print(f'Hello {user}, thank you for logging in again.')