# write stage of life with an if-elif-else chain
age = 25

if age < 2:
    print('(S)he is a baby.')
elif age < 4:
    print('(S)he is a toddler.')
elif age < 13:
    print('(S)he is a kid.')
elif age < 20:
    print('This person is a teenager.')
elif age < 65:
    print('This person is an adult.')
else:
    print('This person is an elder.')

# test our if-elif-else chain with iteration within an ages list

ages = [1, 3, 5, 15, 25, 67]

for age in ages:
    if age < 2:
        print('\n(S)he is a baby.')
    elif age < 4:
        print('(S)he is a toddler.')
    elif age < 13:
        print('(S)he is a kid.')
    elif age < 20:
        print('This person is a teenager.')
    elif age < 65:
        print('This person is an adult.')
    else:
        print('This person is an elder.')