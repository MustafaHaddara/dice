from config import ACCELERATION_AMOUNT, ACCELERATION_FRAME_COUNT, STARTING_SPEED, MAX_SPEED
from gameobjects.base import GameObject

class __SpeedManager(GameObject):
    def __init__(self):
        super().__init__(None, [], [])
        self.y_speed = STARTING_SPEED
        self.tick = 0

    def update(self, _events):
        self.tick += 1
        if self.tick > ACCELERATION_FRAME_COUNT:
            self.adjust_speed(ACCELERATION_AMOUNT)
            self.tick = 0

    def render(self, surface):
        pass

    def adjust_speed(self, inc):
        self.y_speed = round(self.y_speed + inc, 3)
        if self.y_speed > STARTING_SPEED:
            self.y_speed = STARTING_SPEED
        if self.y_speed < MAX_SPEED:
            self.y_speed = MAX_SPEED
    
    def reset(self):
        self.y_speed = STARTING_SPEED
        self.tick = 0

speed_manager = __SpeedManager()