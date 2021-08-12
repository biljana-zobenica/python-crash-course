# prompts

name_prompt = "What is your name? "
place_prompt = "If you could visit one place in the world,"
place_prompt += " where would you go? "

# create an empty dictionary
# store the responses { name : place }
responses = { }

# prompt user input messages
poll_active = True

while poll_active:
    # ask for inputs
    name = input(name_prompt)
    place = input(place_prompt)
    
    # store the prompts
    responses[name] = place

    # check for continue or break
    repeat = input("Whould you like to ask someone else to take the poll? (yes/no) ")
    if repeat == 'no':
        poll_active = False

# print the summary
print(f'--- Poll Results ---')
for name, place in responses.items():
    print(f'\t{name.title()} would like to visit {place.title()}.')