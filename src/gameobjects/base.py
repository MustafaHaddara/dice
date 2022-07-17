from pygame import Rect, Surface


class GameObject:
    # image = image
    # pos = [x, y]
    # speed = [x, y]
    def __init__(self, image, pos, speed):
        self.image: Surface = image
        self.pos = pos
        self.speed = speed
        self.destroyed = False
        self.padding = [0, 0]

    def update(self, _events):
        self.pos[0] += self.speed[0]
        self.pos[1] += self.speed[1]

    def render(self, surface: Surface):
        surface.blit(self.image, self.pos)
    
    def render_ui(self, _surface: Surface):
        pass

    def get_rect(self):
        # todo clean this up
        pos = [self.pos[0] + self.padding[0], self.pos[1] + self.padding[1]]
        return Rect(pos, self.image.get_bounding_rect().size)

    def destroy(self):
        self.destroyed = True
