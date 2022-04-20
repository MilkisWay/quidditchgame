from ball import *


class Throwable_Ball(BallModel):
    def __init__(self, pos, speed):
        super(Throwable_Ball,self).__init__(pos, speed)
        self._pos = pygame.math.Vector2(pos)
        self.rect = pygame.Rect(self.pos.x,self.pos.y, 0, 0)
        self._speed = pygame.math.Vector2(speed)
        self._throw = False

    def set_throw(self,b:bool):
        self._throw = b
    def get_throw(self):
        return self._throw