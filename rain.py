
import pygame as pg
from random import randint
vec3 = pg.Vector3

class drop():
    def __init__(self, dim) -> None:
        self.dim = dim
        self.reset()

    def reset(self):
        self.vec = vec3(randint(0, self.dim[0]), randint(0, self.dim[1])-self.dim[1], randint(0, 20))

