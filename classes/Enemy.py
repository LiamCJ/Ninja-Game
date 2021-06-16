import pygame as pg
import os
vector = pg.math.Vector2


class Enemy(pg.sprite.Sprite):

    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        # velocity of player
        self.velocity = vector(0, 0)
        self.acc = vector(0, 0)
        self.pos = vector(x, y)
        self.hitCount = 0
        self.idleCount = 0
        self.attackCount = 0
        self.throwCount = 0
        self.hit = False
        self.isDead = False
        self.image = pg.image.load('../images/Enemys/enemy_1.png')
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        death_path = '../images/Enemys/death'
        throw_path = '../images/Enemys/throw'

        self.throw = []
        self.death = []

        for motion in sorted(os.listdir(throw_path)):
            image = '{}/{}'.format(throw_path, motion)
            self.throw.append(pg.image.load(image).convert_alpha())

        for motion in sorted(os.listdir(death_path)):
            image = '{}/{}'.format(death_path, motion)
            self.death.append(pg.image.load(image).convert_alpha())

        if self.isDead:
            if self.idleCount <= 11:
                self.image = self.death[self.idleCount // 3]
                self.idleCount += 1
            else:
                path = '../images/Enemys/death/enemyD_4.png'
                self.image = pg.image.load(path).convert_alpha()
        else:
            self.image = self.throw[self.throwCount // 4]

            self.throwCount += 1

            if self.throwCount >= 20:
                self.throwCount = 0

    def getRect(self):
        return self.rec.center
