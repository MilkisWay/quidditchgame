import pygame
import os
import sys
from pygame.locals import *
from object import *


class NonMovableObject(Object):
    def __init__(self, x, y):
        super(NonMovableObject,self).__init__(x,y)
        self._pos = pygame.math.Vector2(x,y)
        self.type=None

class NonMovableObjectView(ObjectView):
    def __init__(self):
        super(NonMovableObjectView,self).__init__()
    pass

class NonMovableObjectController(ObjectController):
    def __init__(self):
        super(NonMovableObjectController,self).__init__()
    pass