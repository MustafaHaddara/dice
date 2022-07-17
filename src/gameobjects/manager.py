from config import SCREEN_HEIGHT
from gameobjects.background import Background
from gameobjects.base import GameObject
from gameobjects.player import Player

class GameObjectManager:
    def __init__(self):
        self.player = Player()
        self.backgrounds = [
            Background([0, 0]),
            Background([0, SCREEN_HEIGHT]),
        ]
        self.blocks = []
    
    def game_objects(self):
        return self.backgrounds + [self.player] + self.blocks
    
    def spawn_block(self, go: GameObject):
        self.blocks.append(go)

manager = GameObjectManager()

def spawn(layer, go: GameObject):
    manager.spawn_block(go)
