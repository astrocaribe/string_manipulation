#! /ust/bin/env python

# Header
"""
:Description:   Given an English sentence, outputs a pig latin translation of
                that sentence.

:Execute:
                >>> python reverse_phrase

:Input(s):      User Input (string)

:Output(s):     Pig latin translated sentence

:Author:        Tommy LeBlanc
                http://astrocaribe.com

:Revisions:
                - Written by Tommy LeBlanc, Feb 2016
"""

# Import necessary modules
from __future__ import print_function
from sys import version_info

import re


# Functions
# --------------------------------------------------------------------------

# Check python version. Returns 'True' for Python3, else returns 'False'
# for Python2
def is_python3( version ):
    return version > 2


def apply_vowel_rule( word ):
    root_word, punctuation = split_punctuation( word )

    translated_word = root_word + 'yay' + punctuation

    return translated_word


def apply_consonant_rule( word, index ):
    root_word, punctuation = split_punctuation( word )

    begin_split_word = root_word[:index]
    end_split_word = root_word[index:]

    translated_word = end_split_word + begin_split_word + 'ay' + punctuation

    return translated_word


# Split punctuation, if avaiable
def split_punctuation( word ):

    unpunctuated_word = re.findall(r"[\w']+", word)

    if word != unpunctuated_word[0]:
        return unpunctuated_word[0], word[-1]
    else:
        return unpunctuated_word[0], ''



def main():
    repeat_process = True

    while repeat_process:
        # Accept user input of a phrase
        if is_python3( version_info[0] ):
            sentence = input('Please enter an english sentence below to translate: \n')
        else:
            sentence = raw_input('Please enter an english sentence below to translate: \n')

        # Split inout sentence into words
        words = sentence.split()

        vowels = 'aeiou'
        translated_sentence = []

        # Apply translation rules to each word
        for ii in range(0, len( words )):
            if words[ii][0] in vowels:
                translated_word = apply_vowel_rule( words[ii] )
            else:
                vowel_index = [w in vowels for w in words[ii]].index( True )
                translated_word = apply_consonant_rule( words[ii], vowel_index )

            translated_sentence.append( translated_word )

        # Capitalize first letter in first word, removing other cases
        translated_sentence[0] = translated_sentence[0].lower().capitalize()

        # Join word array into a sentence
        translated_sentence = ' '.join(translated_sentence)
        print(translated_sentence, '\n')


        # Give use the choice to quit
        valid_input = False

        while not valid_input:
            if is_python3( version_info[0] ):
                user_input = input('Would you like to translate another sentence? [y/n] ' )
            else:
                user_input = raw_input('Would you like to translate another sentence? [y/n] ' )

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
