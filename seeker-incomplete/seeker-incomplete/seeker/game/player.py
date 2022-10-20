from game.terminal import Terminal
from game.jumper import Jumper
from game.word import Word

class Player:
    
    def __init__(self):

        self._word_guess = Word()
        self._jumper = Jumper()
        self._terminal = Terminal()
        
        
    def start_game(self):

        self._word_guess.draw_word()
        self._jumper.draw_jumper()
        
        while self._jumper.is_alive() and not self._word_guess.is_guessed():
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
        
    def _get_inputs(self):

        guess = self._terminal.read_text("\nGuess a letter [a-z]: ")
        
        if not self._word_guess.check_guess(guess):
            self._jumper.take_lives()
    
    def _do_updates(self):
        """"""
    
    def _do_outputs(self):

        self._word_guess.draw_word()
        self._jumper.draw_jumper()
        
        if not self._jumper.is_alive():
            self._terminal.write_text("Game Over!")
        elif self._word_guess.is_guessed():
            self._terminal.write_text("You guessed it! Congrats!")