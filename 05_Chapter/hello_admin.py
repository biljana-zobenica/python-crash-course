usernames = ['biksa', 'admin', 'eddie', 'spark', 'charlie']

for user in usernames:
    if user == 'admin':
        print(f'Hello admin, would you like to see a status report?')
    else:    
        print(f'Hello {user}, thank you for logging in again.')