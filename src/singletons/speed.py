from gameobjects.base import GameObject


ACCELERATION_FRAME_COUNT = 300 # 5 seconds

class __SpeedManager(GameObject):
    def __init__(self):
        super().__init__(None, [], [])
        self.y_speed = -6
        self.tick = 0

    def update(self, _events):
        self.tick += 1
        if self.tick > ACCELERATION_FRAME_COUNT:
            self.y_speed -= 1
            self.tick = 0

    def render(self, surface):
        pass

    def adjust_speed(self, inc):
        self.y_speed += inc
    
    def reset(self):
        self.y_speed = -4
        self.tick = 0

speed_manager = __SpeedManager()