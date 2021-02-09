from random import randint

class De:
    def __init__(self, number):
        self.valeur = randint(1,number)
        self.face = number

    def reroll(self):
        self.valeur = randint(1,6)
        self.display_face()

    def display_face(self):
        print("Valeur: %s" % self.valeur)



class Game:
    def __init__(self):
        self.dice = De()

    def throw_dices(self):
        self.dice.reroll()


my_game = Game()
my_game.throw_dices()

my_game