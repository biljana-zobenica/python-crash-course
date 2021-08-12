# input question
number_of_people = input("Please, provide the number of people in your dinner group? ")

# convert the input into integer (by default it is considered to be a string)
number_of_people = int(number_of_people)

# output message
if number_of_people > 8:
    print(f"Sorry, you will have to wait for a table.")
else:
    print(f"Your table is ready.")