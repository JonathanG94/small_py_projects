
import random

num_digits = 3
max_guesses = 10

def main():
    print(f'''I am thinking of a {num_digits}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:     That means:
Pico            One digit is correct but in the wrong position.
Fermi           One digit is correct and in the right position.
Bagels          No digit is correct.'

For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.''')

    while True: #Main game loop.
        # This stores the secret number the player has to guess
        secret_num = get_secret_num()
        print('I have thought up a number.')
        print(f'You have {max_guesses} guesses to get it')

        num_guesses = 1
        while num_guesses <= max_guesses:
            guess = ''
            #keep looping until they enter a valid guess:
            while len(guess) != num_digits or not guess.isdecimal():
                print(f'Guess #{num_guesses}:')
                guess = input()

            clues = get_clues(guess, secret_num) 
            print(clues)
            num_guesses += 1

            if guess == secret_num:
                break 
            if num_guesses > max_guesses:
                print('You ran out of guesses.')        
                print(f'The answer was {secret_num}')

        #Ask player if they want to play again.
        print('Do you want to play again? (yes/no)')
        if not input().lower().startswith('y'):
            break

    print('Thanks for playing!')

def get_secret_num():
    """Returns a string of num_digits unique random digits"""
    numbers = [i for i in range(10)] #used list comprehension here
    random.shuffle(numbers)

    #Get the first num_digits digits in the list for the secret number.

    secret_num = ''
    for i in range(num_digits):
        secret_num += str(numbers[i])
    return secret_num

def get_clues(guess, secret_num):
    """Returns a string withcles for a guess and secret number pair"""
    if guess == secret_num:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            # A correct digit is in the correct place
            clues.append('Fermi')
        elif guess[i] in secret_num:
            # A correct digit is in the wrong place.
            clues.append('Pico')

    if len(clues) == 0: 
        return 'Bagels' #Clever way of returning this for no correct digits
    else:
        #Sort the clues into alphabetical order so their original order
        #doesn't give information away.
        sorted_clues = sorted(clues)
        return ' '.join(sorted_clues)

#If the program is run instead of imported run the game:
if __name__ == '__main__':
    main()