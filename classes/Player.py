import pygame as pg
import os
vector = pg.math.Vector2

class Player(pg.sprite.Sprite):

    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.winWidth = 500
        self.winLength = 281
        # movement of player
        self.pressKey = pg.key.get_pressed()
        self.speed = 0.8
        # velocity of player
        self.velocity = vector(0, 0)
        self.acc = vector(0, 0)
        self.pos = vector(x, y)
        self.fric = -0.15
        # rect of player
        path_to_idle = '../images/Ninja/Right/idle/R_idle_1.png'
        self.image = pg.image.load(path_to_idle).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.isDownR = False
        self.isDownL = False
        self.isRunR = False
        self.isRunL = False
        self.isJump = False
        self.isUpR = False
        self.isUpL = False
        self.isIdle = True
        self.isAtck = False
        self.isL = False
        self.isR = True
        self.isHurt = False
        self.isDead = False
        self.jumpC = 7
        self.walkC = 0
        self.runC = 0
        self.idle = 0
        self.atckUC = 0
        self.atckC = 0
        # formerly hrtC
        self.hurtCount = 0
        # formerly dthC
        self.deathCount = 0
        self.atckIsK = False
        self.atckIsI = False
        self.atckIsL = False

    def update(self):
        self.animation()
        # ============
        # KEYS INPUT
        # ============
        self.acc = vector(0, 0)
        if not self.isDead:
            if self.pressKey[pg.K_d] or self.pressKey[pg.K_RIGHT]:
                self.acc.x = self.speed
                self.isR = True
                self.isL = False
                self.isIdle = False
                self.isRunL = False
                self.isRunR = False
                self.isAtck = False
                self.atckC = 0
                self.atckUC = 0
            elif (self.pressKey[pg.K_s] or self.pressKey[pg.K_DOWN]):
                self.acc.x = self.speed * 2
                self.isR = False
                self.isL = False
                self.isRunR = True
                self.isIdle = False
                self.isRunL = False
                self.isAtck = False
                self.atckC = 0
                self.atckUC = 0
            elif self.pressKey[pg.K_k]:
                self.isAtck = True
                self.atckIsK = True
                self.atckIsL = False
                self.atckIsI = False
                self.isIdle = False
            elif self.pressKey[pg.K_i]:
                self.isAtck = True
                self.atckIsI = True
                self.atckIsK = False
                self.atckIsL = False
                self.isIdle = False
            elif self.pressKey[pg.K_l]:
                self.isAtck = True
                self.atckIsL = True
                self.atckIsI = False
                self.atckIsK = False
                self.isIdle = False
            else:
                self.idle += 1
                self.isIdle = True
                self.isAtck = False
                self.atckIsI = False
                self.atckIsK = False
                self.atckIsL = False

            # applies friction
            self.acc += self.velocity * self.fric

            # equations of motion
            self.velocity += self.acc
            self.pos += self.velocity + 0.5 * self.acc

            # changing screens

            if self.pos.x <= 10:
                self.pos.x = 40
                self.isR = True
                self.isL = False

            # changing position
            self.rect.center = self.pos

            # ==============
            # JUMPING
            # ==============

            if not self.isJump:
                if self.pressKey[pg.K_j] or self.pressKey[pg.K_SPACE]:
                    self.isJump = True
                    self.isIdle = False
                    self.walkC = 0
                    self.runC = 0
                    self.atckC = 0
                    self.atckUC = 0
            else:
                if self.jumpC >= -7:
                    n = 1
                    self.isUpR = True
                    self.isUpL = True
                    self.isDownR = False
                    self.isDownL = False
                    self.isIdle = False
                    if self.jumpC < 0:
                        n = -1
                        self.isDownR = True
                        self.isDownL = True
                        self.isUpR = False
                        self.isUpL = False
                        self.isIdle = False
                    self.pos.y -= ((self.jumpC ** 2) / 2) * n
                    self.jumpC -= 1
                else:
                    self.idle = 0
                    self.isJump = False
                    self.jumpC = 7
                    self.isIdle = True
                    self.isDownR = False
                    self.isUpR = False
                    self.isDownL = False
                    self.isUpL = False

    def animation(self):
        # Moving Right
        right_walk_path = '../images/Ninja/Right/walk'
        right_jump_path = '../images/Ninja/Right/jump'
        right_idle_path = '../images/Ninja/Right/idle'
        right_death_path = '../images/Ninja/Right/death'
        right_hurt_path = '../images/Ninja/Right/hurt'
        right_run_path = '../images/Ninja/Right/run'

        self.death_right = []
        self.walk_right = []
        self.jump_right = []
        self.idle_right = []
        self.hurt_right = []
        self.run_right = []

        for motion in sorted(os.listdir(right_walk_path)):
            image = '{}/{}'.format(right_walk_path, motion)
            self.walk_right.append(pg.image.load(image).convert_alpha())

        for motion in sorted(os.listdir(right_jump_path)):
            image = '{}/{}'.format(right_jump_path, motion)
            self.jump_right.append(pg.image.load(image).convert_alpha())

        for motion in sorted(os.listdir(right_idle_path)):
            image = '{}/{}'.format(right_idle_path, motion)
            self.idle_right.append(pg.image.load(image).convert_alpha())

        for motion in sorted(os.listdir(right_death_path)):
            image = '{}/{}'.format(right_death_path, motion)
            self.death_right.append(pg.image.load(image).convert_alpha())

        for motion in sorted(os.listdir(right_hurt_path)):
            image = '{}/{}'.format(right_hurt_path, motion)
            self.hurt_right.append(pg.image.load(image).convert_alpha())

        for motion in sorted(os.listdir(right_run_path)):
            image = '{}/{}'.format(right_run_path, motion)
            self.run_right.append(pg.image.load(image).convert_alpha())

        # self.run_right=(pg.image.load(right_walk_path).convert_alpha(),
        #     pg.image.load('../images/Ninja/R_run_2.png').convert_alpha(),
        #     pg.image.load('../images/Ninja/R_run_3.png').convert_alpha(),
        #     pg.image.load('../images/Ninja/R_run_4.png').convert_alpha(),
        #     pg.image.load('../images/Ninja/R_run_5.png').convert_alpha(),
        #     pg.image.load('../images/Ninja/R_run_6.png').convert_alpha())
        # self.walk_right=(pg.image.load(right_walk_path).convert_alpha(),
        #     pg.image.load('../images/Ninja/R_walk_2.png').convert_alpha(),
        #     pg.image.load('../images/Ninja/R_walk_3.png').convert_alpha(),
        #     pg.image.load('../images/Ninja/R_walk_4.png').convert_alpha())
        # self.idle_right=(pg.image.load(right_walk_path).convert_alpha(),
        #     pg.image.load('../images/Ninja/R_idle_2.png').convert_alpha())
        # self.jump_right=(pg.image.load(right_walk_path).convert_alpha(),
        #     pg.image.load('../images/Ninja/R_land.png').convert_alpha())
#         # # Damage
#         # self.death_right=(pg.image.load(right_walk_path).convert_alpha(),
#         #     pg.image.load('../images/Ninja/R_death_2.png').convert_alpha(),
#         #     pg.image.load('../images/Ninja/R_death_3.png').convert_alpha(),
#         #     pg.image.load('../images/Ninja/R_death_4.png').convert_alpha(),
#         #     pg.image.load('../images/Ninja/R_death_5.png').convert_alpha(),
#         #     pg.image.load('../images/Ninja/R_death_6.png').convert_alpha(),
#         #     pg.image.load('../images/Ninja/R_death_7.png').convert_alpha(),
        #     pg.image.load('../images/Ninja/R_death_8.png').convert_alpha())

        if not self.isDead:

            if not self.isIdle:

                if not self.isJump:

                    if not self.isAtck:
                        self.direction()
                    elif self.isAtck:

                        self.attack()

                elif self.isJump:
                    self.jump()
            elif self.isIdle:
                #  self.idle()
                if self.isR or self.isRunR or self.isAtck:
                    self.image = self.idle_right[self.idle // 7]

                if self.idle >= 13:
                    self.idle = 0
        elif self.isDead:
            self.death_right()

    def attack(self):
        # Attacking Right
        right_attack_path = '../images/Ninja/Right/attack'

        self.attack_right = []

        for motion in sorted(os.listdir(right_attack_path)):
            image = '{}/{}'.format(right_attack_path, motion)
            self.attack_right.append(pg.image.load(image).convert_alpha())

        # self.attack_right=(pg.image.load('right_attack_path').convert_alpha(),
        # pg.image.load('../images/Ninja/R_attack_2.png').convert_alpha(),
        # pg.image.load('../images/Ninja/R_attack_4.png').convert_alpha(),
        # pg.image.load('../images/Ninja/R_attack_6.png').convert_alpha())
        # self.medAtckR=(pg.image.load('right_attack_path').convert_alpha(),
        # pg.image.load('../images/Ninja/R_attack_2.png').convert_alpha(),
        # pg.image.load('../images/Ninja/R_attack_5.png').convert_alpha())
        # self.strngAtckR=(pg.image.load('right_attack_path').convert_alpha(),
        # pg.image.load('../images/Ninja/R_attack_2.png').convert_alpha(),
        # pg.image.load('../images/Ninja/R_attack_3.png').convert_alpha())

        # ===========
        # ACTIONS
        # ===========

        if self.atckIsK:
            self.image = self.attack_right[self.atckC // 1]
            self.rect = self.image.get_rect()

            self.atckC += 1
            if self.atckC >= 4:
                self.atckC = 0

        elif self.atckIsI:
            self.image = self.attack_right[self.atckUC // 1]
            self.rect = self.image.get_rect()

            self.atckUC += 1
            if self.atckUC >= 4:
                self.atckUC = 0

        elif self.atckIsL:
            self.image = self.attack_right[self.atckUC // 1]
            self.rect = self.image.get_rect()
            self.atckUC += 1
            if self.atckUC >= 4:
                self.atckUC = 0

    # # #  NEW # # #
    def direction(self):
        if self.isL:
            self.image = self.walkL[self.walkC // 3]
            self.walkC += 1
            if self.walkC >= 12:
                self.walkC = 0
        elif self.isR:
            self.image = self.walk_right[self.walkC // 3]
            self.walkC += 1
            if self.walkC >= 12:
                self.walkC = 0
        elif self.isRunL:
            self.image = self.runL[self.runC // 2]
            self.runC += 1
            if self.runC >= 12:
                self.runC = 0
        elif self.isRunR:
            self.image = self.run_right[self.runC // 2]
            self.runC += 1
            if self.runC >= 12:
                self.runC = 0

    def jump(self):
        if self.isR or self.isRunR:
            if self.isUpR:
                self.image = self.jump_right[0]
            elif self.isDownR:
                self.image = self.jump_right[1]
        elif self.isL or self.isRunL:
            if self.isUpL:
                self.image = self.jumpL[0]
            elif self.isDownL:
                self.image = self.jumpL[1]

    def idle(self):
        if self.isR or self.isRunR or self.isAtck:
            self.image = self.idle_right[self.idle // 7]
        elif self.isL or self.isRunL or self.isAtck:
            self.image = self.ninL[self.idle // 7]

        if self.idle >= 13:
            self.idle = 0

    def dead(self):
        self.image = self.death_right[self.runC // 2]
        self.image = self.death_right[7]
        self.dthC += 1 * 2
        if self.dthC >= 16:
            self.dthC = 0
