import pygame

from config import POINTS_PER_BLOCK
from gameobjects.base import GameObject

#Setting up Fonts
pygame.font.init()
font = pygame.font.SysFont("Verdana", 20)

class __ScoreManager(GameObject):
    def __init__(self):
        super().__init__(None, [], [])
        self.score = 0

    def update(self, _events):
        pass

    def render(self, surface):
        pass

    def render_ui(self, surface):
        s = font.render(f'Score: {self.score}', True, (0,0,0), (255,255,255))
        surface.blit(s, (0,20))

    def inc_score(self):
        self.score += POINTS_PER_BLOCK

    def reset(self):
        self.score = 0

score_manager = __ScoreManager()