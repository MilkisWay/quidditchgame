from ball import *


class Throwable_Ball(BallModel):
    def __init__(self, pos, speed):
        super(Throwable_Ball,self).__init__(pos, speed)
        self._throw = False

    def set_throw(self,b:bool):
        self._throw = b
    def get_throw(self):
        return self._throw