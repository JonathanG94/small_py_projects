
import random

comp_num = str(random.randint(100,999))

#Printing out the user's instructions
print('I am thinking of a 3 digit number. Try to guess what it is.')
print('Here are some clues:')
print('When I say:\t\tThat means:')
print('Pico\t\t\tOne digit is correct but in the wrong position.')
print('Fermi\t\t\tOne digit is correct and in the right position.')
print('Bagels\t\t\tNo digit is correct')
print('I have thought up a number.\nYou have ten guesses to get it.')

num_guesses = 1

while num_guesses < 11:
    print(f"Guess #{num_guesses}")
    
    #checking that the input is valid
    while True:
        guess = str(input())
        if len(guess) != len(comp_num):
            print("Oops, that's not a 3 digit number - please guess again:")
        else:
            break

    for i in len(guess):
        

    num_guesses += 1



