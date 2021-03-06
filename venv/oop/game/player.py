"""
Modify the Player class so that the player's scores are increased 
by one thousand every time their level increases by one.

So if they jump up two levels, they will get a bonus of two thousand added to their score.

If the player drops back a level, they will lose one thousand for each level they drop back.

They cannot go below Level One, so your solution should prevent that from happening.

The aim of this challenge is to practice properties, so although it may make more sense
to add methods to increase and decrease the level, please do not do it that way - use a property.
"""

class Player:
    
    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("Cannot have negative lives")
            self._lives = 0

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if level > 0:
            delta = level - self._level
            self._score += delta * 1000
            self._level = level
        else:
            print("Level cannot be less than 1")

    lives = property(_get_lives, _set_lives)
    level = property(_get_level, _set_level)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score: {0.score}".format(self)
