class Terminal_service:
    def __init__(self):
        self.parachute = ['  ___  ', ' /___\\ ', ' \\   / ', '  \\ /  ', '   0   ', '  /|\\  ', '  / \\  ', '', '^^^^^^^']
        self.word = ''

    def display_parachute(self):
        for each in self.parachute:
            print(each)

    def word_display(self):
        return print('_ _ _ _ _')

    def get_input(self, prompt):
        return input(prompt)

    def display_guesses(self, letter_list):
        word_guessed = ''

        for each in letter_list:
            word_guessed += f'{each} '
        print(word_guessed)