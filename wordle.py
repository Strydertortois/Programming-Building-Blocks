## Python

## For randint()

from ast import While
import random

## Set the play_again variable to yes to the loop will start
number_of_guesses = 0
guessed = False
correct_word = 'nephi'
while (guessed != True):
    ## Set word as variable:
    
    correct_word_list = list(correct_word)

        ## Ask the user for a guess of word
    guessed_word = input('Input your guess: ')
    
    guessed_word_list = list(guessed_word)
    ## Create the output list
    output = []
    ## Fill the output with _
    for o_count, o_value in enumerate(correct_word_list):
        output.append('_')
    ## Output the Output list


    ## loop guess
    for g_count, g_value in enumerate(guessed_word_list):
        ## loop secret work in the guess
        for c_count, c_value in enumerate(correct_word_list):
            ## if secret word letter and guess word letter
            if(c_value == g_value):
                if(c_count == g_count):
                    output[c_count] = c_value.upper()
                else:
                    output[c_count] = c_value.lower()

    ## Final Output
    final_output = ''.join(map(str, output))

    number_of_guesses = number_of_guesses + 1
    print(final_output)
    print('You have guessed ' + str(number_of_guesses) + ' times.')
    if (correct_word.lower() == guessed_word.lower()):
        print('You got it correct! It took ' + str(number_of_guesses) + ' attempts to guess the word.')
        guessed = True
    ## letting user know they got it correct 
## print(f'{guessed_word} is the correct word - well done.  It took {number_of_guesses} to guess the word.')
## print(f'{correct_word} is the word.')
