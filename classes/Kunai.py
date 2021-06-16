import pygame as pg
vector = pg.math.Vector2


class Kunai(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('../images/Enemys/kunai.png')
        self.rect = self.image.get_rect()
        self.rect.center = (420, 188)
        self.speed = 8
        # velocity of player
        self.velocity = vector(0, 0)
        self.acc = vector(0, 0)
        self.pos = vector(420, 188)

    def update(self):
        self.pos.x -= self.speed

        # changing position
        self.rect.center = self.pos
