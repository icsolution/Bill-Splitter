import random
try:
    friends = int(input('Enter the number of friends joining (including you):\n'))
except ValueError:
    print('\nNo one is joining for the party')
else:
    if friends > 0:
        print('\nEnter the name of every friend (including you), each on a new line:')
        party = {input(): 0 for _ in range(friends)}
        bill = int(input('\nEnter the total bill value:\n'))

        lucky = input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:\n')
        if lucky == 'No':
            print('\nNo one is going to be lucky')
            print(f'\n{dict.fromkeys(party, round(bill / len(party), 2))}')
        else:
            name = random.choice(list(party.keys()))
            print(f'\n{name} is the lucky one!')
            amount = dict.fromkeys(party, round(bill / (len(party) - 1), 2))
            amount[name] = 0
            print(f'\n{amount}')
    else:
        print('\nNo one is joining for the party')

