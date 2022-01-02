name = input("What is your name? ")
print(f"Hello {name.title()}!")

with open('10_Chapter/guest_book.txt', 'a') as n:
    n.write(f"{name}\n")