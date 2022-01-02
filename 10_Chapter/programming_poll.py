filename = 'programming_poll.txt'

responses = []

while True:
    response = input("\nWhy do you love programming? ")
    responses.append(response)
    
    continue_poll = input("Whould you like to write more reasons? (y/n) ")
    if continue_poll == 'n':
        break
    
with open('10_Chapter/programming_poll.txt', 'a') as n:
    for response in responses:
        n.write(f"{response}\n")
