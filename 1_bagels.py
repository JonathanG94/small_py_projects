
import random

#Printing out the user's instructions
print('I am thinking of a 3 digit number. Try to guess what it is.')
print('Here are some clues:')
print('When I say:\t\tThat means:')
print('Pico\t\t\tOne digit is correct but in the wrong position.')
print('Fermi\t\t\tOne digit is correct and in the right position.')
print('Bagels\t\t\tNo digit is correct')
print('I have thought up a number.\nYou have ten guesses to get it.')


user_active = True

#Main loop for the game
while user_active:

    comp_num = str(random.randint(100,999))
    # print(comp_num) #Check line
    num_guesses = 1

    #Checking user guesses
    while num_guesses < 11:
        print(f"Guess #{num_guesses}")
        
        #checking that the input is valid
        while True:
            guess = str(input())
            if len(guess) != len(comp_num):
                print("Oops, that's not a 3 digit number - please guess again:")
            else:
                break
       
        #Checking If the user has guessed correctly, otherwise running the bagels 
        #check function
        if guess == comp_num:
            print('Congratulations! You guessed correctly!')
            break
        else: 
            bagels_check = True

            for i in range(len(guess)):
                if guess[i] == comp_num[i]:
                    print('Fermi')
                    bagels_check = False
                elif guess[i] in comp_num:
                    print('Pico')
                    bagels_check = False
            
            if bagels_check:
                print('Bagels') 

        num_guesses += 1

    print('Would you like to keep playing? (Y/N)')
    
    #Checking that input is valid
    while True:
        user_choice = input().upper()
        if user_choice == 'N' or user_choice == 'Y':
            break
        else:
            print("Whoops! I didn't understand that")

    #Checking if user wants to continue
    if user_choice == 'Y':
        print('Here we go again!')
    elif user_choice == 'N':
        break
