import pygame

from asset_loader import asset_path
from gameobjects.base import GameObject
from singletons.speed import speed_manager

BACKGROUND_IMAGE = pygame.image.load(asset_path('background.jpg'))

class Background(GameObject):
    def __init__(self, pos):
        super().__init__(BACKGROUND_IMAGE, pos, [0, -4])

    def update(self, events):
        super().update(events)
        self.speed[1] = speed_manager.y_speed

        if self.pos[1] < -self.image.get_height():
            self.pos[1] = 2*self.image.get_height()
