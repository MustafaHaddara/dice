from random import randint

from gameobjects.base import GameObject
from sprites.dice import DICE_IMAGES
from singletons.score import score_manager
from singletons.speed import speed_manager

class Block(GameObject):
    def __init__(self, pos):
        super().__init__(None, pos, [0, -4])
        self.value = randint(1,6)
        self.image = DICE_IMAGES[self.value]
        self.tick = 0
        self.padding = [4,4]

    def update(self, events):
        super().update(events)
        self.speed[1] = speed_manager.y_speed

        if self.pos[1] < (-1 * self.image.get_height()):
            score_manager.inc_score()
            self.destroy()
