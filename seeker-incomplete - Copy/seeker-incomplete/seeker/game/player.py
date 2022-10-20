class Player:
    def __init__(self):
        self._guess = ""
        self._keep_playing = True
        pass

    def get_guess(self):
        _valid = False
        while (_valid != True):
            self._guess = input("Guess a letter [a-z]: ")

            if (len(self._guess) != 1):
                print("Invalid input please try again with a single letter")
                _valid = False
            elif (self._guess.isnumeric()):
                print("Invalid input numbers are not allowed")
                _valid = False
            else:
                _valid = True

        return self._guess

    def play_again(self):
        _valid = False
        while (_valid == False):
            response = input("Would you like to play again [y/n]? ")
            if (len(response) != 1):
                print(
                    "Invalid input please try again with a single letter [y/n]")
                _valid = False
            elif (response.isnumeric()):
                print("Invalid input numbers are not allowed")
                _valid = False
            elif (response.lower() == "y" or response.lower() == "n"):
                _valid = True
            else:
                print("Invalid response")
                _valid = False

        if response.lower() == "y":
            self._keep_playing = True
        else:
            self._keep_playing = False

        return self._keep_playing