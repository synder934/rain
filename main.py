import pygame as pg
from random import randint

pg.init()
vec3 = pg.Vector3
DIM = [1000, 700]
clock = pg.time.Clock()
rain = [vec3(randint(0, DIM[0]), randint(0, DIM[1])-DIM[1], randint(0, 20)) for i in range(250)]
disp = pg.display.set_mode(DIM)
pg.display.set_caption('rain')
FPS = 60


running = 1
while running:
    pg.display.update()
    disp.fill((0,0,0))
    for e in pg.event.get():
        if e.type == pg.QUIT:
            running = 0

    for dp in rain:
        pg.draw.rect(
            disp,
            (50, 70, 255),
            ((dp.x, dp.y), (2+(dp.z/8), 10+(dp.z)))
        )
        dp.y += 5+(dp.z/4)
        if dp.y > DIM[1]:
            dp.x, dp.y, dp.z = randint(0, DIM[0]), randint(0, DIM[1])-DIM[1], randint(0, 20)

    clock.tick(FPS)