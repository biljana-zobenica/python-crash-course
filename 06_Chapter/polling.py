favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c', 
    'edward' : 'ruby', 
    'phil' : 'python',
    }

persons = ['jen', 'mark', 'steve', 'sarah']

for person in persons:
    if person in favorite_languages.keys():
        print(f"Thank you for taking the poll, {person.title()}!")
    else:
        print(f"{person.title()}, what is your favorite programming language?")