# -*- coding: utf-8 -*-

import random

IMAGES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

WORDS = ['carro', 'casa', 'registro', 'computadora', 'sala', 'leo', 'paola', 'licuadora']

def random_word(words):
    return words[random.randrange(0,len(words)-1)]

def display_board(hiden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hiden_word)
    print('')
    print('--- * --- * --- * --- * --- * --- * ')
    print('')

def run():
    word = random_word(WORDS)
    hiden_word = ['_']*len(word)
    tries = 0

    while True:
        display_board(hiden_word, tries)
        current_letter = str(input('Escoge una letra: '))

        letter_indexes = [idx for idx, x in enumerate(word) if x== current_letter]
        
        if len(letter_indexes) == 0:
            tries += 1

            if tries == 7:
                print('')
                print('¡Perdiste! La palabra correcta era ' + word.upper())
                break
        else:
            for i in letter_indexes:
                hiden_word[i] = current_letter
            letter_indexes = []
        
        try:
            hiden_word.index('_')
        except ValueError:
            print('')
            print('¡Felicidades! Ganaste.')
            break


if __name__ == '__main__':
    run()