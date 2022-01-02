# solution 1
name = input("What is your name? ")
print(f"Hello {name.title()}!")

with open('10_Chapter/guest_book.txt', 'a') as n:
    n.write(f"{name}\n")

# solution 2
filename = 'guest_book.txt'

print("Enter 'quit' when you are finished.")

while True:
    name = input("\nWhat is your name? ")
    if name == 'quit':
        break
    else:
        with open('10_Chapter/guest_book.txt', 'a') as n:
            n.write(f"{name}\n")
        print(f"Hi {name.title()}, you have been added to the guest list.")