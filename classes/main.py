from Player import Player
from Health import Health
from Kunai import Kunai
from Enemy import Enemy
import pygame as pg
import math

vector = pg.math.Vector2


class Main:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        # dimension of window
        self.winWidth = 500
        self.winLength = 281
        # window set-up
        self.screen = pg.display.set_mode(size=(self.winWidth, self.winLength))
        pg.display.set_caption("Shinobi Warrior")
        self.keys = pg.key.get_pressed()
        self.clock = pg.time.Clock()
        self.background_no = 1
        self.last_update = 0
        self.playing = False
        self.running = True
        self.score = 0
        self.font2 = pg.font.Font('../fonts/Bank_Gothic_Medium_BT.ttf', 15)
        self.font = pg.font.Font('../fonts/Bank_Gothic_Medium_BT.ttf', 20)
        self.red = Enemy(420, 188)
        self.health_bar = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.kunais = pg.sprite.Group()

        self.red = Enemy(420, 188)

        self.health_bar.add(Health(30, 10))
        self.health_bar.add(Health(60, 10))
        self.health_bar.add(Health(90, 10))
        self.enemies.add(self.red)

        self.kunais.add(Kunai())

    def new(self):
        #  start a new game
        self.main_sprite = pg.sprite.Group()
        self.ninja = Player(40, 188)
        self.main_sprite.add(self.ninja)
        self.game_run()

    def high_score(self):
        score_file = open('../high_score.txt', 'r+', encoding='utf-8-sig')
        try:
            self.high_score = int(score_file.read())
        except(EnvironmentError):
            self.high_score = 0

        score_file.close()
        score_file.closed

    def game_run(self):
        # game loop
        self.playing = True
        while self.playing:
            # FPS
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game loop - Update
        self.main_sprite.update()
        if self.ninja.pos.x > self.winWidth:
            self.ninja.pos.x = 40
            self.background_no += 1
            self.red.isDead = False

            for kunai in self.kunais:
                kunai.pos = self.red.pos

            if self.background_no >= 5:
                self.background_no = 1
        self.health_bar.update()
        self.enemies.update()
        self.kunais.update()

        sword_atck = pg.sprite.spritecollide(self.ninja, self.enemies, False)

        kunai_hit = pg.sprite.spritecollide(self.ninja, self.kunais, False)

        for enmy in self.enemies:
            if not enmy.isDead:

                if sword_atck and self.ninja.isAtck:
                    self.score += 1
                    enemy_path = '../images/Enemys/enemyH_3.png'
                    enmy.image = pg.image.load(enemy_path).convert_alpha()
                    enmy.isDead = True

                for kunai in self.kunais:
                    now = pg.time.get_ticks()
                    x_position_change = self.ninja.pos.x - self.red.pos.x
                    y_position_change = self.ninja.pos.y - self.red.pos.y
                    dist = math.hypot(x_position_change, y_position_change)

                    if dist >= 100:
                        if now - self.last_update > 2500 or kunai_hit:
                            self.last_update = now
                            kunai.pos = vector(self.red.rect.center)
                            self.kunais.draw(self.screen)
                            self.kunais.update()

                        if kunai_hit:

                            self.kunais.remove(kunai)
                            self.health_bar.remove(
                                self.health_bar.sprites()[-1]
                            )

                            if len(self.health_bar) >= 1:
                                self.kunais.add(Kunai())
                            elif len(self.health_bar) <= 0:
                                self.kunais.empty()
                                self.ninja.isDead = True
                                self.playing = False

    def events(self):
        # Game loop -events
        # array of keys *each key is assigned a number*
        self.keys = pg.key.get_pressed()
        # checks for input
        for e in pg.event.get():
            if e.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        # Game loop -draw
        bg_image = '../images/Backgrounds/bg_{}.png'.format(self.background_no)
        self.background = pg.image.load(bg_image).convert_alpha()
        self.screen.blit(self.background, (0, 0))

        self.kunais.draw(self.screen)
        self.enemies.draw(self.screen)
        self.main_sprite.draw(self.screen)
        self.health_bar.draw(self.screen)
        score = 'Score: {}'.format(self.score)
        self.score_board = self.font.render(score, True, (0, 0, 0))
        self.screen.blit(self.score_board, (200, 0))
        pg.display.flip()

    def show_start_screen(self):

        self.high_score()
        bg_op_path = '../images/Backgrounds/openingScene.png'
        self.opn = pg.image.load(bg_op_path).convert_alpha()
        self.screen.blit(
            self.opn,
            (0, 0)
        )
        self.screen.blit(
            self.font.render(
                'Press Tab For Controls',
                True,
                (0, 0, 0),
                (255, 255, 255)
            ),
            (100, 150)
        )
        self.screen.blit(
            self.font.render(
                'Press Space To Play',
                True,
                (0, 0, 0),
                (255, 255, 255)
            ),
            (120, 200)
        )
        self.screen.blit(
            self.font2.render(
                'High Score: {}'.format(self.high_score),
                True,
                (0, 0, 0),
                (255, 255, 255)
            ),
            (350, 0)
        )
        pg.display.flip()
        self.enter_key()

    def game_over(self):
        #  game over/continue
        bg_path = '../images/Backgrounds/gameOver.png'
        self.gameOver = pg.image.load(bg_path).convert_alpha()
        self.screen.blit(
            self.gameOver,
            (0, 0)
        )
        self.screen.blit(
            self.font.render(
                'Press Tab For Controls',
                True,
                (0, 0, 0),
                (255, 255, 255)
            ),
            (100, 150)
        )
        self.screen.blit(
            self.font.render(
                'Press Space To Play',
                True,
                (0, 0, 0),
                (255, 255, 255)
            ),
            (120, 200)
        )

        if self.score > self.high_score:
            self.high_score = self.score
            self.screen.blit(
                self.font.render(
                    'New High Score: {}'.format(self.high_score),
                    True,
                    (0, 0, 0),
                    (255, 255, 255)
                ),
                (140, 250)
            )
            score_file = open('../high_score.txt', 'r+', encoding='utf-8-sig')

            score_file.write(str(self.high_score))

            score_file.close()
            score_file.closed

        self.screen.blit(
            self.font2.render(
                'High Score: {}'.format(self.high_score),
                True,
                (0, 0, 0),
                (255, 255, 255)
            ),
            (350, 0)
        )

        pg.display.flip()
        self.enter_key()

    def enter_key(self):
        waiting = True
        cntrls = False
        while waiting:
            self.clock.tick(60)
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if e.type == pg.KEYDOWN:
                    if e.key == pg.K_SPACE:
                        waiting = False
                        self.score = 0
                    if e.key == pg.K_TAB:
                        cntrls = not cntrls
                        path = '../images/Backgrounds/controls.png'
                        self.cntrls = pg.image.load(path).convert_alpha()
                        if cntrls:
                            self.screen.blit(self.cntrls, (0, 0))
                        else:
                            self.screen.blit(self.opn, (0, 0))
                            self.ctrls = self.font.render(
                                'Hold Tab For Controls',
                                True, (0, 0, 0),
                                (255, 255, 255)
                            )
                            self.play = self.font.render(
                                'Press Space To Play',
                                True,
                                (0, 0, 0),
                                (255, 255, 255)
                            )
                            self.screen.blit(self.ctrls, (100, 150))
                            self.screen.blit(self.play, (120, 200))
                        pg.display.flip()
