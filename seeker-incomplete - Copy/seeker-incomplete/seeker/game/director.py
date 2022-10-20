from player import Player
from secret_word import Secret_word
from terminal_service import Terminal_service


class Director:

    def __init__(self):
        self._player = Player()
        self._secret_word = Secret_word()
        self._terminal_service = Terminal_service()

        self._keep_playing = Player._keep_playing
        self._win = False
        pass

    def start_game(self):
        while self._keep_playing:
            self._do_outputs()
            self._get_inputs()
            self._do_updates()

        if self._win == False:
            print("Game over! You lost!")
        else:
            print("Game over! Congrats, You won!\n")

        self._keep_playing == Player.play_again()

        if self._keep_playing:
            self.start_game()
        else:
            pass
        pass

    def _get_inputs(self):
        self._guess = self._player.get_guess()
        pass

    def _do_updates(self):
        self._word = self._secret_word._secret_word

        if self._secret_word.compare_guess(self._guess):
            pass
        else:
            self._terminal_service.parachute.pop(0)

    def _do_outputs(self):
        self._terminal_service.word_display()
        self._terminal_service.display_parachute(self)