from config import LEVEL_2, LEVEL_3, LEVEL_4
from gameobjects.base import GameObject

class __LevelManager(GameObject):
    def __init__(self):
        super().__init__(None, [], [])
        self.level = 1
        self.tick = 0

    def update(self, _events):
        self.tick += 1

    def render(self, surface):
        pass

    def current_level(self):
        if self.tick > LEVEL_4:
            return 4
        if self.tick > LEVEL_3:
            return 3
        if self.tick > LEVEL_2:
            return 2
        return 1

level_manager = __LevelManager()
