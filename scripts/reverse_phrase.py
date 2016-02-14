#! /ust/bin/env python

# Header
"""
:Description:   Given a string sentence, reverse the order of the words

:Execute:
                >>> python reverse_string

:Input(s):      User Input (string)

:Output(s):     Reverse word of input

:Author:        Tommy LeBlanc
                http://astrocaribe.com

:Revisions:
                - Written by Tommy LeBlanc, Feb 2016
"""

# Import necessary modules
from __future__ import print_function
from sys import version_info

# Functions
# --------------------------------------------------------------------------

# Check python version. Returns 'True' for Python3, else returns 'False'
# for Python2
def is_python3( version ):
    return version > 2


# Reverse the word order of an input phrase
def reverse_the_phrase( phrase ):
    # Split phrase by spaces
    words = phrase.split(' ')

    # Reverse word order, and join resulting array into a reversed string
    # phrase with spaces reinserted
    reversed_phrase = ' '.join( words[::-1] )

    return reversed_phrase


def main():
    repeat_process = True

    while repeat_process:
        # Accept user input of a phrase
        if is_python3( version_info[0] ):
            phrase = input('Please enter a phrase below to reverse: \n')
        else:
            phrase = raw_input('Please enter a phrase below to reverse: \n')

        # Print reversed phrase
        print()
        print( reverse_the_phrase(phrase) + '\n')

        # Give use the choice to quit
        valid_input = False

        while not valid_input:
            user_input = raw_input('Would you like to enter another phrase? [y/n] ' )
            if ( user_input == 'y' or user_input == 'n'):
                valid_input = True
                print()
            else:
                print("Please enter [y/n]")

        # Return user's choice
        if ( valid_input and user_input == 'y' ):
            repeat_process = True
        else:
            print('Goodbye!')
            repeat_process = False



# Main script
# --------------------------------------------------------------------------
if __name__ == '__main__':
    main()
