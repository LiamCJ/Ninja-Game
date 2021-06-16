import pygame as pg


class Health(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        path = "../images/Ninja/health.png"
        self.image = pg.image.load(path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
