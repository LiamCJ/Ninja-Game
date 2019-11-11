import pygame as pg
import random
vector = pg.math.Vector2


class Program:


    def __init__(self):
    #initialize game window, etc
        pg.init()
        pg.mixer.init()
        #dimension of window
        self.winWidth = 500
        self.winLength = 281
        #window set-up
        self.screen = pg.display.set_mode(size=(self.winWidth, self.winLength))
        pg.display.set_caption("Shinobi Warrior")
        self.clock = pg.time.Clock()
        self.running = True
        self.playing = False
        self.bg_no = 1
        self.score = 0
        self.last_update = 0
        self.font= pg.font.Font('fonts/Bank_Gothic_Medium_BT.ttf', 20)
    
    
    def new(self):
        # start a new game
        self.main_sprite = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.kunais = pg.sprite.Group()
        self.health_bar = pg.sprite.Group()
        
        self.ninja = Player(40, 188)
        self.red = Enemy(420, 188)
        
        self.main_sprite.add(self.ninja)
        self.enemies.add(self.red)
        self.health_bar.add(Health(30, 10))
        self.health_bar.add(Health(60, 10))
        self.health_bar.add(Health(90, 10))
        self.health_bar.add(Health(120, 10))
        self.health_bar.add(Health(150, 10))
        self.health_bar.add(Health(180, 10))
        
#         for k in (1,3): 
        self.kunais.add(Kunai())
        
        self.game_run()
    
    
    def game_run(self):
        #game loop
        self.playing = True
        while self.playing:
            self.clock.tick(60) #FPS
            self.events()
            self.draw()
            self.update()
    
    
    def update(self):
        #Game loop - Update
        self.main_sprite.update()
        self.enemies.update()
        self.kunais.update()
        self.health_bar.update()
        
        sword_atck = pg.sprite.spritecollide(self.ninja, self.enemies, False)
        
        kunai_hit = pg.sprite.spritecollide(self.ninja, self.kunais, False)
        
        for enmy in self.enemies:            
            if enmy.isDead == False: 
                
                if sword_atck and self.ninja.isAtck == True:
                    self.score += 1
                    enmy.image = pg.image.load('images/Enemys/enemyH_3.png').convert_alpha()
                    enmy.isDead = True
                    
                for kunai in  self.kunais:
                    now = pg.time.get_ticks()
                    if now - self.last_update > 2500 or kunai_hit:
                        self.last_update = now
                        kunai.pos = vector(self.red.rect.center)
                        self.kunais.draw(self.screen)
                        self.kunais.update()
                    
                    if kunai_hit:
                        
                        self.health_bar.remove(self.health_bar.sprites()[-1])
                        self.kunais.remove(kunai)
                        
                        if len(self.health_bar) >= 1 :
                            self.kunais.add(Kunai())
                        elif len(self.health_bar) <= 0:
                            self.kunais.empty()
                            self.ninja.isDead = True
                            self.playing = False
                            
        
    def events(self):
        #Game loop -events
        #array of keys *each key is assigned a number*        
        self.keys = pg.key.get_pressed() 
        #checks for input
        for e in pg.event.get(): 
            if e.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
                self.start = False
    
    
    def draw(self):
        #Game loop -draw
        self.bg = pg.image.load('images/Backgrounds/bg_{}.png'.format(self.bg_no)).convert_alpha()
        self.screen.blit(self.bg, (0,0))
        
        self.kunais.draw(self.screen)
        self.enemies.draw(self.screen)
        self.main_sprite.draw(self.screen)
        self.health_bar.draw(self.screen)
        
        self.score_board = self.font.render('Score: {}'.format(self.score), True, (0, 0, 0))
        self.screen.blit(self.score_board, (200,0))
        
        pg.display.flip()
    
    
    def show_start_screen(self):
            self.opn = pg.image.load('images/Backgrounds/openingScene.png').convert_alpha()
            self.screen.blit(self.opn, (0,0)) 
            self.ctrls = self.font.render('Press Tab For Controls', True, (0, 0, 0), (255, 255, 255))
            self.play = self.font.render('Press Space To Play', True, (0, 0, 0), (255, 255, 255))
            self.screen.blit(self.ctrls, (100,150))
            self.screen.blit(self.play, (120,200))          
            pg.display.flip()    
            self.enter_key()
            
               
    def game_over(self):
        # game over/continue
        self.gameOver = pg.image.load('images/Backgrounds/gameOver.png').convert_alpha()
        self.screen.blit(self.gameOver, (0,0)) 
        self.ctrls = self.font.render('Press Tab For Controls', True, (0, 0, 0), (255, 255, 255))
        self.play = self.font.render('Press Space To Play', True, (0, 0, 0), (255, 255, 255))
        self.screen.blit(self.ctrls, (100,150))
        self.screen.blit(self.play, (120,200))           
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
                    if e.key == pg.K_TAB:
                        cntrls = not cntrls
                        self.cntrls = pg.image.load('images/Backgrounds/controls.png').convert_alpha()
                        if cntrls:
                            self.screen.blit(self.cntrls, (0,0))
                        else:
                            self.screen.blit(self.opn, (0,0))  
                            self.ctrls = self.font.render('Hold Tab For Controls', True, (0, 0, 0), (255, 255, 255))
                            self.play = self.font.render('Press Space To Play', True, (0, 0, 0), (255, 255, 255))
                            self.screen.blit(self.ctrls, (100,150))
                            self.screen.blit(self.play, (120,200))      
                        pg.display.flip()  
                        
    
class Player(pg.sprite.Sprite):


    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        #movement of player
        self.speed = 0.8
        self.vel = vector(0,0) #velocity of player
        self.acc = vector(0,0)
        self.pos = vector(x, y)
        self.fric = -0.15
        #rect of player
        self.image = pg.image.load('images/Ninja/R_idle_1.png').convert_alpha()
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
        self.hrtC = 0
        self.dthC = 0
        self.atckIsK = False
        self.atckIsI = False
        self.atckIsL = False 
 
        
    def update(self):
        self.animation()
        #============
        #KEYS INPUT
        #============
        self.acc = vector(0,0)
        if not self.isDead:
            if g.keys[pg.K_a] or g.keys[pg.K_LEFT]:
                self.acc.x = -self.speed
                self.isL = True
                self.isR = False
                self.isIdle = False
                self.isRunL = False
                self.isRunR = False
                self.isAtck = False
                self.atckC = 0
                self.atckUC = 0
            elif g.keys[pg.K_d] or g.keys[pg.K_RIGHT]:
                self.acc.x = self.speed
                self.isR = True
                self.isIdle = False
                self.isL = False
                self.isRunL = False
                self.isRunR = False
                self.isAtck = False
                self.atckC = 0
                self.atckUC = 0
            elif (g.keys[pg.K_w] or g.keys[pg.K_UP]):
                self.acc.x = -self.speed * 2
                self.isRunL = True
                self.isIdle = False
                self.isRunR = False
                self.isR = False
                self.isL = False
                self.isAtck = False
                self.atckC = 0
                self.atckUC = 0
            elif (g.keys[pg.K_s] or g.keys[pg.K_DOWN]):
                self.acc.x = self.speed * 2
                self.isRunR = True
                self.isIdle = False
                self.isRunL = False
                self.isR = False
                self.isL = False 
                self.isAtck = False
                self.atckC = 0
                self.atckUC = 0
            elif g.keys[pg.K_k]:
                self.isAtck = True  
                self.atckIsK = True 
                self.atckIsL = False
                self.atckIsI = False
                self.isIdle = False 
            elif g.keys[pg.K_i]:
                self.isAtck = True 
                self.atckIsI = True
                self.atckIsK = False  
                self.atckIsL = False 
                self.isIdle = False 
            elif g.keys[pg.K_l]:
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
    
            #applies friction    
            self.acc += self.vel * self.fric    
            
            #equations of motion
            self.vel += self.acc
            self.pos += self.vel + 0.5 * self.acc
            
            #changing screens
            if self.pos.x > g.winWidth:
                self.pos.x = 0   
                g.bg_no += 1
                g.red.isDead = False
                if g.bg_no >= 5:
                    g.bg_no = 1
                    
            if self.pos.x <= 20:
                self.pos.x = 30
                self.isR = True
                self.isL = False
             
            #changing position
            self.rect.center = self.pos  
              
            #==============
            #JUMPING
            #==============
        
            if not self.isJump:
                if g.keys[pg.K_j]:
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
        #Moving Right
        self.runR = (pg.image.load('images/Ninja/R_run_1.png').convert_alpha(),pg.image.load('images/Ninja/R_run_2.png').convert_alpha(),pg.image.load('images/Ninja/R_run_3.png').convert_alpha(),pg.image.load('images/Ninja/R_run_4.png').convert_alpha(),pg.image.load('images/Ninja/R_run_5.png').convert_alpha(),pg.image.load('images/Ninja/R_run_6.png').convert_alpha())
        self.walkR = (pg.image.load('images/Ninja/R_walk_1.png').convert_alpha(),pg.image.load('images/Ninja/R_walk_2.png').convert_alpha(),pg.image.load('images/Ninja/R_walk_3.png').convert_alpha(),pg.image.load('images/Ninja/R_walk_4.png').convert_alpha())
        self.ninR = (pg.image.load('images/Ninja/R_idle_1.png').convert_alpha(),pg.image.load('images/Ninja/R_idle_2.png').convert_alpha())
        self.jumpR = (pg.image.load('images/Ninja/R_jump.png').convert_alpha(),pg.image.load('images/Ninja/R_land.png').convert_alpha())
    
        #Moving Left
        self.runL = (pg.image.load('images/Ninja/L_run_1.png').convert_alpha(),pg.image.load('images/Ninja/L_run_2.png').convert_alpha(),pg.image.load('images/Ninja/L_run_3.png').convert_alpha(),pg.image.load('images/Ninja/L_run_4.png').convert_alpha(),pg.image.load('images/Ninja/L_run_5.png').convert_alpha(),pg.image.load('images/Ninja/L_run_6.png').convert_alpha())
        self.walkL = (pg.image.load('images/Ninja/L_walk_1.png').convert_alpha(),pg.image.load('images/Ninja/L_walk_2.png').convert_alpha(),pg.image.load('images/Ninja/L_walk_3.png').convert_alpha(),pg.image.load('images/Ninja/L_walk_4.png').convert_alpha())
        self.ninL = (pg.image.load('images/Ninja/L_idle_1.png').convert_alpha(),pg.image.load('images/Ninja/L_idle_2.png').convert_alpha())
        self.jumpL = (pg.image.load('images/Ninja/L_jump.png').convert_alpha(),pg.image.load('images/Ninja/L_land.png').convert_alpha())   
        
        #Damage
        #self.hurt = (pg.image.load('images/Ninja/R_hurt_1.png').convert_alpha(),pg.image.load('images/Ninja/R_hurt_2.png').convert_alpha(),pg.image.load('images/Ninja/R_hurt_3.png').convert_alpha(),pg.image.load('images/Ninja/R_hurt_4.png').convert_alpha(),pg.image.load('images/Ninja/R_hurt_5.png').convert_alpha())
        self.dead = (pg.image.load('images/Ninja/R_death_1.png').convert_alpha(),pg.image.load('images/Ninja/R_death_2.png').convert_alpha(),pg.image.load('images/Ninja/R_death_3.png').convert_alpha(),pg.image.load('images/Ninja/R_death_4.png').convert_alpha(), pg.image.load('images/Ninja/R_death_5.png').convert_alpha(), pg.image.load('images/Ninja/R_death_6.png').convert_alpha(), pg.image.load('images/Ninja/R_death_7.png').convert_alpha(), pg.image.load('images/Ninja/R_death_8.png').convert_alpha())
        
        if not self.isDead:
            
            if not self.isIdle:
    
                if not self.isJump:
    
                    if not self.isAtck:
                            
                            if self.isL :
                                self.image = self.walkL[self.walkC//3]
                                self.walkC += 1
                                if self.walkC >= 12:
                                    self.walkC = 0
                            elif self.isR: 
                                self.image = self.walkR[self.walkC//3]
                                self.walkC += 1
                                if self.walkC >= 12:
                                    self.walkC = 0
                            elif self.isRunL:
                                self.image = self.runL[self.runC//2]
                                self.runC += 1
                                if self.runC >= 12:
                                    self.runC = 0
                            elif self.isRunR:
                                self.image = self.runR[self.runC//2]
                                self.runC += 1
                                if self.runC >= 12:
                                    self.runC = 0
                                
                    elif self.isAtck:
                        
                        self.attack()
         
                elif self.isJump:
                   
                    if self.isR or self.isRunR:               
                        if self.isUpR:
                            self.image = self.jumpR[0]
                        elif self.isDownR:
                            self.image = self.jumpR[1]
                    elif self.isL or self.isRunL:               
                        if self.isUpL:
                            self.image = self.jumpL[0]
                        elif self.isDownL:
                            self.image = self.jumpL[1]         
            elif self.isIdle:
        
                if self.isR or self.isRunR or self.isAtck: 
                    self.image = self.ninR[self.idle//7]
                elif self.isL or self.isRunL or self.isAtck: 
                    self.image = self.ninL[self.idle//7]
        
                if self.idle >= 13:
                    self.idle = 0
        elif self.isDead:
            self.image = self.dead[self.runC//2]
            self.image = self.dead[7]
            self.dthC += 1 * 2
            if self.dthC >= 16:
                self.dthC = 0
 
    def attack(self):
        #Attacking Right
        self.kAtckR = (pg.image.load('images/Ninja/R_attack_1.png').convert_alpha(),pg.image.load('images/Ninja/R_attack_2.png').convert_alpha(),pg.image.load('images/Ninja/R_attack_4.png').convert_alpha(),pg.image.load('images/Ninja/R_attack_6.png').convert_alpha())
        self.iAtckR = (pg.image.load('images/Ninja/R_attack_1.png').convert_alpha(),pg.image.load('images/Ninja/R_attack_2.png').convert_alpha(),pg.image.load('images/Ninja/R_attack_5.png').convert_alpha())
        self.lAtckR = (pg.image.load('images/Ninja/R_attack_1.png').convert_alpha(),pg.image.load('images/Ninja/R_attack_2.png').convert_alpha(),pg.image.load('images/Ninja/R_attack_3.png').convert_alpha())
 
        #===========
        #ACTIONS
        #===========
        
        if self.atckIsK:          
            self.image = self.kAtckR[self.atckC//1]
            self.rect = self.image.get_rect()
           
            self.atckC += 1
            if self.atckC >= 4:
                self.atckC = 0
                
        elif self.atckIsI:
            self.image = self.iAtckR[self.atckUC//1]
            self.rect = self.image.get_rect()
            
            self.atckUC += 1
            if self.atckUC >= 3:
                self.atckUC = 0
        
        elif self.atckIsL:
            self.image = self.lAtckR[self.atckUC//1]
            self.rect = self.image.get_rect()
            
            self.atckUC += 1
            if self.atckUC >= 3:
                self.atckUC = 0
  
   
    def idle(self):
        pass
    
    
    def walk(self):
        pass
    
    
    def run(self):
        pass
    
    
    def jump(self):
        pass
             
        
class Enemy(pg.sprite.Sprite):    


    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)    
        self.vel = vector(0,0) #velocity of player
        self.acc = vector(0,0)
        self.pos = vector(x, y)
        self.hitC = 0
        self.idleC = 0
        self.atckC = 0
        self.thrwC = 0
        self.hit = False
        self.isDead = False
        self.image = pg.image.load('images/Enemys/enemy_1.png')   
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
      
        
    def update(self):  
        self.thrw = (pg.image.load('images/Enemys/enemyT_1.png').convert_alpha(), pg.image.load('images/Enemys/enemyT_2.png').convert_alpha(),pg.image.load('images/Enemys/enemyT_3.png').convert_alpha(),pg.image.load('images/Enemys/enemyT_4.png').convert_alpha(),pg.image.load('images/Enemys/enemyT_5.png').convert_alpha())
        self.dth = (pg.image.load('images/Enemys/enemyD_1.png').convert_alpha(),pg.image.load('images/Enemys/enemyD_2.png').convert_alpha(),pg.image.load('images/Enemys/enemyD_3.png').convert_alpha(),pg.image.load('images/Enemys/enemyD_4.png').convert_alpha())
        
        
        if self.isDead:
            if self.idleC <= 11:
                self.image = self.dth[self.idleC//3]
                self.idleC += 1
            else:
                self.image =  pg.image.load('images/Enemys/enemyD_4.png').convert_alpha()
        else:     
            self.image = self.thrw[self.thrwC//4]
            
            self.thrwC += 1
            
            if self.thrwC >= 20:
                self.thrwC = 0


class Kunai(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)    
        self.image = pg.image.load('images/Enemys/kunai.png')
        self.rect = self.image.get_rect()
        self.rect.center = g.red.rect.center    
        self.speed = 8
        self.vel = vector(0,0) #velocity of player
        self.acc = vector(0,0)
        self.pos = vector(g.red.rect.center)
    
    def update(self):  
        self.pos.x -= self.speed
            
        #changing position
        self.rect.center = self.pos 
  
        
class Health(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)   
        self.image = pg.image.load("images/Ninja/health.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        
        
    
    
g = Program()
g.show_start_screen()
while g.running:
    g.new()
    g.game_over()
    
pg.quit()

"""
Make kunai stop for periods then continue
Make only throw enemies so that user has to dodge them and their is no confusion in collision
remove True & False conditions, and make each animation a function
"""