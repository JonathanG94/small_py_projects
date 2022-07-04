
import random

#Establishing global variables
month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
birthday_list = []

def birthday_generator(num_birthdays):
    '''Generates a list of birthdays to assess for duplicates'''
    for i in range(num_birthdays):
        month = month_list[random.randint(0, 11)]

        if month == 'Feb':
            day = random.randint(1, 29)
        elif month == 'April' or 'Jun' or 'Sep' or 'Nov':
            day = random.randint(1, 30)
        else:
            day = random.randint(1, 31)

        birthday = f'{day} {month}'
        birthday_list.append(birthday)

    return birthday_list

print('How many birthdays shall I generate? (Max 100)')

#Getting desired birthdays from user
while True:
    try:
        num_birthdays = int(input())
        if not 1 <= num_birthdays <= 100:
            print('Please enter a number between 1 & 100')
        else:
            break
    except:
        print('Please enter a number between 1 & 100')
        
print(f'Here are {num_birthdays} birthdays \n')
birthday_generator(num_birthdays)
print(birthday_list)

#Check for duplicates
duplicate_birthdays = {x for x in birthday_list if birthday_list.count(x) > 1}

#Telling the user if duplicate birthdays were found
if len(duplicate_birthdays) == 0:
    print("In this simulation, it doesn't look as though anyone shared \
a birthday")
else:    
    print(f"In this simulation, multiple people shared a \
birthday on {' & '.join(str(x) for x in duplicate_birthdays)}")

positive_sim = 0
number_sims = 100_000

print(f"""\nI'm now going to run {number_sims} simulations of {num_birthdays} \
birthdays. 
Press enter when you're ready""")

#Getting user confirmation that ready
while True:
    confirmation = input()
    if confirmation == "":
        break
    else:
        print("Press enter to confirm you're ready.")

#Running the simulations
for x in range(number_sims + 1):
    #clearing lists and sets
    birthday_list.clear()
    duplicate_birthdays.clear()

    if x % 10_000 == 0:
        print(f'{x} simulations run')

    birthday_generator(num_birthdays)
    duplicate_birthdays = {x for x in birthday_list if birthday_list.count(x) > 1}

    if len(duplicate_birthdays) > 0:
        positive_sim += 1

pc_positive = round(positive_sim/number_sims * 100, 2)

print(f"""\nOut of {number_sims} simulations of {num_birthdays} people, 
there was a matching birthday in that group {positive_sim} times.
This means that {num_birthdays} people have a {pc_positive}% chance of 
having a matching birthday. That's probably more than you thought!""")
