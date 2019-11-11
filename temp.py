import pygame as pg
import random
# from setting import *
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
    
    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.ninja = Player(20, 188)
        self.sword = Attack()
        self.red = Enemy(470, 188)
        self.all_sprites.add(self.ninja)
        self.all_sprites.add(self.sword)
        self.all_sprites.add(self.red)
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
        self.all_sprites.update()
#         pg.display.update()
        
    def events(self):
        #Game loop -events
        #array of keys *each key is assigned a number*        
        self.keys = pg.key.get_pressed() 
         
        #checks for input
        for e in pg.event.get(): 
            if e.type == pg.QUIT or self.keys[pg.K_ESCAPE]:
                if self.playing:
                    self.playing = False
                self.running = False
    
    
    def draw(self):
        #Game loop -draw
        self.backgrounds = (pg.image.load('images/Backgrounds/bg_1.png').convert_alpha(),pg.image.load('images/Backgrounds/bg_2.png').convert_alpha(),pg.image.load('images/Backgrounds/bg_3.png').convert_alpha())
        self.bg_no = 0
        self.bg = self.backgrounds[self.bg_no]
        self.screen.blit(self.bg, (0,0))
        self.all_sprites.draw(self.screen)
        pg.display.flip()
    
    def show_start_screen(self):
        #start screen
        pass
    
    def show_go_screen(self):
        # game over/continue
        pass
    

class Player(pg.sprite.Sprite):

    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        #movement of player
        self.speed = 0.8
        self.vel = vector(0,0) #velocity of player
        self.acc = vector(0,0)
        self.pos = vector(x, y)
        self.fric = -0.12
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
        self.jumpC = 7
        self.walkC = 0
        self.runC = 0 
        self.idle = 0   
        
    def update(self):
        self.animation()
        #============
        #KEYS INPUT
        #============
        self.acc = vector(0,0)
        if g.keys[pg.K_a] or g.keys[pg.K_LEFT]:
            self.acc.x = -self.speed
            self.isL = True
            self.isIdle = False
            self.isR = False
            self.isRunL = False
            self.isRunR = False
            self.isAtck = False
            g.sword.atckC = 0
            g.sword.atckUC = 0
        elif g.keys[pg.K_d] or g.keys[pg.K_RIGHT]:
            self.acc.x = self.speed
            self.isR = True
            self.isIdle = False
            self.isL = False
            self.isRunL = False
            self.isRunR = False
            self.isAtck = False
            g.sword.atckC = 0
            g.sword.atckUC = 0
        elif (g.keys[pg.K_w] or g.keys[pg.K_UP]):
            self.acc.x = -self.speed * 2
            self.isRunL = True
            self.isIdle = False
            self.isRunR = False
            self.isR = False
            self.isL = False
            self.isAtck = False
            g.sword.atckC = 0
            g.sword.atckUC = 0
        elif (g.keys[pg.K_s] or g.keys[pg.K_DOWN]):
            self.acc.x = self.speed * 2
            self.isRunR = True
            self.isIdle = False
            self.isRunL = False
            self.isR = False
            self.isL = False 
            self.isAtck = False
            g.sword.atckC = 0
            g.sword.atckUC = 0
        elif g.keys[pg.K_k]:
            self.isAtck = True  
            g.sword.atckIsK = True 
            g.sword.atckIsL = False
            g.sword.atckIsI = False
            self.isIdle = False 
        elif g.keys[pg.K_i]:
            self.isAtck = True 
            g.sword.atckIsI = True
            g.sword.atckIsK = False  
            g.sword.atckIsL = False 
            self.isIdle = False 
        elif g.keys[pg.K_l]:
            self.isAtck = True 
            g.sword.atckIsL = True 
            g.sword.atckIsI = False
            g.sword.atckIsK = False  
            self.isIdle = False         
        else:
            self.idle += 1
            self.isIdle = True
            self.isAtck = False 
            g.sword.atckIsI = False
            g.sword.atckIsK = False   
            g.sword.atckIsL = False  

        #applies friction    
        self.acc += self.vel * self.fric    
        
        #equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        
        #changing screens
        if self.pos.x > g.winWidth:
            self.pos.x = 0   
            g.bg_no += 1
            if g.bg_no >=3:
                g.bg_no = 0
                
        if self.pos.x < 0:
            self.pos.x = 0
         
        #changing position
        self.rect.center = self.pos  
        g.sword.rect.center = self.pos  
          
        #==============
        #JUMPING
        #==============
    
        if not self.isJump:
            if g.keys[pg.K_j]:
                self.isJump = True
                self.isIdle = False
                self.walkC = 0
                self.runC = 0
                g.sword.atckC = 0
                g.sword.atckUC = 0
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
                g.sword.pos.y -= ((self.jumpC ** 2) / 2) * n 
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
        
        if not self.isIdle:

            if not self.isJump:

                if not self.isAtck:

                    if self.isL :
                        self.image = self.walkL[self.walkC//3]
                        g.sword.image = self.walkL[self.walkC//3]
                        self.walkC += 1
                        if self.walkC >= 12:
                            self.walkC = 0
                    elif self.isR: 
                        self.image = self.walkR[self.walkC//3]
                        g.sword.image = self.walkR[self.walkC//3]
                        self.walkC += 1
                        if self.walkC >= 12:
                            self.walkC = 0
                    elif self.isRunL:
                        self.image = self.runL[self.runC//2]
                        g.sword.image = self.runL[self.runC//2]
                        self.runC += 1
                        if self.runC >= 12:
                            self.runC = 0
                    elif self.isRunR:
                        self.image = self.runR[self.runC//2]
                        g.sword.image = self.runR[self.runC//2]
                        self.runC += 1
                        if self.runC >= 12:
                            self.runC = 0
        
                elif self.isAtck:
                    
                    g.sword.update()
     
            elif self.isJump:
               
                if self.isR or self.isRunR:               
                    if self.isUpR:
                        self.image = self.jumpR[0]
                        g.sword.image = self.jumpR[0]
                    elif self.isDownR:
                        self.image = self.jumpR[1]
                        g.sword.image = self.jumpR[1]
                elif self.isL or self.isRunL:               
                    if self.isUpL:
                        self.image = self.jumpL[0]
                        g.sword.image = self.jumpL[0]
                    elif self.isDownL:
                        self.image = self.jumpL[1] 
                        g.sword.image = self.jumpL[1]         
        elif self.isIdle:
    
            if self.isR or self.isRunR or self.isAtck: 
                self.image = self.ninR[self.idle//7]
                g.sword.image = self.ninR[self.idle//7]
            elif self.isL or self.isRunL or self.isAtck: 
                self.image = self.ninL[self.idle//7]
                g.sword.image = self.ninL[self.idle//7]
    
            if self.idle >= 13:
                self.idle = 0
        

class Attack(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = g.ninja.image
        self.rect = self.image.get_rect()
        self.pos = vector(g.ninja.pos.x, g.ninja.pos.y)
        self.rect.center = (g.ninja.rect.center[0], g.ninja.rect.center[1])
        self.atckUC = 0
        self.atckC = 0  
        self.atckIsK = False
        self.atckIsI = False
        self.atckIsL = False


    def update(self):
        #Attacking Right
        self.kAtckR = (pg.image.load('images/Ninja/R_attack_1.png').convert_alpha(),pg.image.load('images/Ninja/R_attack_2.png').convert_alpha(),pg.image.load('images/Ninja/R_attack_4.png').convert_alpha(),pg.image.load('images/Ninja/R_attack_6.png').convert_alpha())
        self.iAtckR = (pg.image.load('images/Ninja/R_attack_1.png').convert_alpha(),pg.image.load('images/Ninja/R_attack_2.png').convert_alpha(),pg.image.load('images/Ninja/R_attack_5.png').convert_alpha())
        self.lAtckR = (pg.image.load('images/Ninja/R_attack_1.png').convert_alpha(),pg.image.load('images/Ninja/R_attack_2.png').convert_alpha(),pg.image.load('images/Ninja/R_attack_3.png').convert_alpha())
 
        #===========
        #ACTIONS
        #===========
        
        if self.atckIsK:
                
            g.ninja.image = self.kAtckR[self.atckC//3]
            self.image = self.kAtckR[self.atckC//3]
            
            self.atckC += 1
            if self.atckC >= 11:
                self.atckC = 0
                
        elif self.atckIsI:

            g.ninja.image = self.iAtckR[self.atckUC//3]
            self.image = self.iAtckR[self.atckUC//3]
            
            self.atckUC += 1
            if self.atckUC >= 8:
                self.atckUC = 0
        
        elif self.atckIsL:
        
            g.ninja.image = self.lAtckR[self.atckUC//3]
            self.image = self.lAtckR[self.atckUC//3]
            
            self.atckUC += 1
            if self.atckUC >= 8:
                self.atckUC = 0


class Enemy(pg.sprite.Sprite):    

    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)    
        self.vel = vector(0,0) #velocity of player
        self.acc = vector(0,0)
        self.pos = vector(x, y)
        self.fric = -0.12
        self.hitC = 0
        self.idleC = 0
        self.hit = False
        self.isIdle = True
        self.image = pg.image.load('images/Enemys/enemy_1.png')   
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
    def update(self):  
        self.enemy = (pg.image.load('images/Enemys/enemy_1.png').convert_alpha(),pg.image.load('images/Enemys/enemy_2.png').convert_alpha(),pg.image.load('images/Enemys/enemy_3.png').convert_alpha(),pg.image.load('images/Enemys/enemy_4.png').convert_alpha())
        self.get_hit = (pg.image.load('images/Enemys/enemyH_1.png').convert_alpha(),pg.image.load('images/Enemys/enemyH_2.png').convert_alpha(),pg.image.load('images/Enemys/enemyH_3.png').convert_alpha(),pg.image.load('images/Enemys/enemyH_4.png').convert_alpha(),pg.image.load('images/Enemys/enemyH_5.png').convert_alpha())

        self.image = self.enemy[self.idleC//3]
        self.idleC += 1
        if self.idleC >= 12:
            self.idleC = 0        

g = Program()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()
    
pg.quit()