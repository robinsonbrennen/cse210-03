class Jumper:

    def __init__(self):
       self._lives = 5
       self._image = [" _____", 
                     "/_____\\"
                    ,"\     / "
                    , " \   /"
                    ,"  \ /"
                    ,  "   0"
                    ," / | \\"
                    , "  / \\"
                    ,"\n^^^^^^^^"]

    def draw_jumper(self):
        
        if self._lives < 1:
            self._image[0] = "   X"
        
        print("")
        for layer in self._image:
            print (layer)
        print("")

    def take_lives(self):
        self._lives -= 1
        self._image.pop(0)

    def is_alive(self):
        if self._lives == 0:
           return False 
        else: 
            return True