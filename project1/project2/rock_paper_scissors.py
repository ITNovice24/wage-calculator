#using built-in python modules to use random choice & sleep method
import random, time

#list for computer rps selection
list = ['r','p', 's']


user_input = input('Please choose r, p, or s for Rock, Paper, or Scissors... ')


#initializing game to build suspense with 1 second time delays
print('Ready?')
time.sleep(1)
print('ROCK')
time.sleep(1)
print('PAPER')
time.sleep(1)
print('SCISSORS')
time.sleep(1)
print('SHOOOT')
time.sleep(1)

#computer choice is a random selection from the list
computer_choice = random.choice(list) 

#created class Game which contains each of the three main functions
class Game:

        def is_tie():
                if user_input == 'r' and computer_choice == 'r' or user_input == 's' and computer_choice == 's' or user_input == 'p' and computer_choice == 'p':
                        print(f'It\'s a tie! We chose {computer_choice}, choose again!')
                        
        def is_win():
                if user_input != computer_choice:
                        if user_input == 'r' and computer_choice == 's' or user_input == 's' and computer_choice == 'p' or user_input == 'p' and computer_choice == 'r':
                                print(f'You win! We chose {computer_choice}.')

        def is_lose():
                if user_input != computer_choice:
                        if user_input == 'r' and computer_choice == 'p' or user_input == 's' and computer_choice == 'r' or user_input == 'p' and computer_choice == 's':
                                print(f'You lose! We chose {computer_choice}.')
