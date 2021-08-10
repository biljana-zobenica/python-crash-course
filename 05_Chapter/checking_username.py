# create user lists
current_users = ['biksa', 'admin', 'eddie', 'spark', 'charlie']
new_users = ['biksa', 'jack', 'eddie', 'hugh', 'spike']

# apply list comprehension to lower each username in current_users
current_users_lower = [user.lower() for user in current_users]

# compare without case sensitivity impacting the result
for user in new_users:
    if user.lower() in current_users_lower:
        print(f'This username is already taken. Please, enter a new username.')
    else:
        print(f'This username is available.')