from random import randint
from unittest.result import failfast
class Word:
    
    def __init__(self):

        word_list = ['happy',
                    'sad',
                    'grumpy',]
        
        random_index = randint(0, len(word_list) - 1)
        self._word = word_list[random_index]
        self._letters_guessed = ""
                                        
    def draw_word(self):

        print("")
        for letter in self._word:
            if letter in self._letters_guessed:
                print(f"{letter}", end="")
            else:
                print("_", end="")
        print("")
        
    def check_guess(self, guess):

        if guess in self._word:
            self._letters_guessed += guess
            return True
        else:
            return False

    def is_guessed(self):

        fail_count = 0

        for letter in self._word:
            if letter not in self._letters_guessed:
                fail_count += 1

        return (fail_count == 0)