sandwich_orders = ['avocado', 'pastrami', 'veggie', 'pastrami', 'greek', 'pastrami']
finished_sandwiches = []

print("The deli has run out of pastrami sandwiches.\n")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
 
while sandwich_orders:
    current_sandwich = sandwich_orders.pop() # pop the list item in the list
    print(f"I made your {current_sandwich} sandwich.") # print the message by using the popped item
    finished_sandwiches.append(current_sandwich) # fill in the finished list

print(f"\nHere you are the finished sandwiches: ")
for sandwich in finished_sandwiches:    
    print(f"\t{sandwich}")