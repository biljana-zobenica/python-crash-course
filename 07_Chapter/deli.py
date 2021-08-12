sandwich_orders = ['avocado', 'veggie', 'tomato', 'greek', 'tuna']
finished_sandwiches = []
 
while sandwich_orders:
    current_sandwich = sandwich_orders.pop() # pop the list item in the list
    print(f"I made your {current_sandwich} sandwich.") # print the message by using the popped item
    finished_sandwiches.append(current_sandwich) # fill in the finished list

print(f"Here you are the finished sandwiches: ")
for sandwich in finished_sandwiches:    
    print(f"\t{sandwich}")