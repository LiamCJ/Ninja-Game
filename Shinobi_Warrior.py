from pygame import sprite, init, image, display, time, event, key, QUIT, K_a, K_s, K_d, K_w, K_j, K_k, K_l, K_i, K_UP, K_DOWN, K_LEFT, K_RIGHT

init()

bg = image.load('images/Backgrounds/bg_1.png')
#dimension of window
winWidth = 500
winLength = 281
#window set-up
win = display.set_mode(size=(winWidth, winLength))
display.set_caption("Shinobi Warrior")
clock = time.Clock()

run = True #when false SpaceInvaders will stop


class Player(sprite.Sprite):

    
    #Moving Right
    runR = (image.load('images/Ninja/R_run_1.png'),image.load('images/Ninja/R_run_2.png'),image.load('images/Ninja/R_run_3.png'),image.load('images/Ninja/R_run_4.png'),image.load('images/Ninja/R_run_5.png'),image.load('images/Ninja/R_run_6.png'))
    walkR = (image.load('images/Ninja/R_walk_1.png'),image.load('images/Ninja/R_walk_2.png'),image.load('images/Ninja/R_walk_3.png'),image.load('images/Ninja/R_walk_4.png'))
    ninR = (image.load('images/Ninja/R_idle_1.png'),image.load('images/Ninja/R_idle_2.png'))
    jumpR = (image.load('images/Ninja/R_jump.png'),image.load('images/Ninja/R_land.png'))

    #Moving Left
    runL = (image.load('images/Ninja/L_run_1.png'),image.load('images/Ninja/L_run_2.png'),image.load('images/Ninja/L_run_3.png'),image.load('images/Ninja/L_run_4.png'),image.load('images/Ninja/L_run_5.png'),image.load('images/Ninja/L_run_6.png'))
    walkL = (image.load('images/Ninja/L_walk_1.png'),image.load('images/Ninja/L_walk_2.png'),image.load('images/Ninja/L_walk_3.png'),image.load('images/Ninja/L_walk_4.png'))
    ninL = (image.load('images/Ninja/L_idle_1.png'),image.load('images/Ninja/L_idle_2.png'))
    jumpL = (image.load('images/Ninja/L_jump.png'),image.load('images/Ninja/L_land.png'))   

    def __init__(self, x, y, width, height):
        sprite.Sprite.__init__(self)
        #co-ordinates of player
        self.x = x
        self.y = y
        #dimension of player
        self.width = width
        self.height = height
        self.jumpC = 7
        self.walkC = 0
        self.runC = 0 
        self.idle = 0     
        self.vel = 5 #velocity of player
        self.isDownR = False
        self.isDownL = False
        self.isRunR = False
        self.isRunL = False
        self.isJump = False
        self.isUpR = False
        self.isUpL = False
        self.isIdle = True
        self.isL = False
        self.isR = True
         

    def draw(self, win):
#         win.blit(bg, (0,0)) 

        #===========
        #ACTIONS
        #===========

        if not self.isIdle:

            if not self.isJump:

                if not self.isAtck:

                    if self.isL :
                        win.blit(self.walkL[self.walkC//3], (self.x,self.y))
                        self.walkC += 1
                        if self.walkC >= 12:
                            self.walkC = 0
                    elif self.isR: 
                        win.blit(self.walkR[self.walkC//3], (self.x,self.y))
                        self.walkC += 1
                        if self.walkC >= 12:
                            self.walkC = 0
                    elif self.isRunL:
                        win.blit(self.runL[self.runC//2],(self.x,self.y))
                        self.runC += 1
                        if self.runC >= 12:
                            self.runC = 0
                    elif self.isRunR:
                        win.blit(self.runR[self.runC//2],(self.x,self.y))
                        self.runC += 1
                        if self.runC >= 12:
                            self.runC = 0

                elif self.isAtck:

                    sword.draw(win)

            elif self.isJump:

                if self.isR or self.isRunR:               
                    if self.isUpR:
                        win.blit(self.jumpR[0],(self.x,self.y))
                    elif self.isDownR:
                        win.blit(self.jumpR[1],(self.x,self.y))
                elif self.isL or self.isRunL:               
                    if self.isUpL:
                        win.blit(self.jumpL[0],(self.x,self.y))
                    elif self.isDownL:
                        win.blit(self.jumpL[1],(self.x,self.y))              
        elif self.isIdle:

            if self.isR or self.isRunR or self.isAtck:
                win.blit(self.ninR[self.idle//4],(self.x,self.y))
            elif self.isL or self.isRunL or self.isAtck:
                win.blit(self.ninL[self.idle//4],(self.x,self.y))

            if self.idle >= 7:
                self.idle = 0
        

        display.update()  
  

class Attack(sprite.Sprite):


    #Attacking Right
    kAtckR = (image.load('images/Ninja/R_attack_1.png'),image.load('images/Ninja/R_attack_2.png'),image.load('images/Ninja/R_attack_4.png'),image.load('images/Ninja/R_attack_6.png'))
    iAtckR = (image.load('images/Ninja/R_attack_1.png'),image.load('images/Ninja/R_attack_2.png'),image.load('images/Ninja/R_attack_5.png'))
    lAtckR = (image.load('images/Ninja/R_attack_1.png'),image.load('images/Ninja/R_attack_2.png'),image.load('images/Ninja/R_attack_3.png'))
 

    def __init__(self):
        sprite.Sprite.__init__(self)
        self.x =  ninja.x
        self.y = ninja.y
        self.width = ninja.width
        self.height = ninja.height
        self.atckUC = 0
        self.atckC = 0  
        self.atckIsK = False
        self.atckIsI = False
        self.atckIsL = False


    def draw(self, win):

        #===========
        #ACTIONS
        #===========
        
        if self.atckIsK:
                
            win.blit(self.kAtckR[self.atckC//2],(ninja.x,ninja.y))
            
            self.atckC += 1
            
            if self.atckC >= 7:
                self.atckC = 0
                
        elif self.atckIsI:

            win.blit(self.iAtckR[self.atckUC//2],(ninja.x,ninja.y))
            
            self.atckUC += 1
           
            if self.atckUC >= 6:
                self.atckUC = 0
        
        elif self.atckIsL:
        
            win.blit(self.lAtckR[self.atckUC//2],(ninja.x,ninja.y))
            
            self.atckUC += 1
           
            if self.atckUC >= 6:
                self.atckUC = 0
                 

# class Enemies(sprite.Group):
#     
#     
#     enemy = (image.load('images/Enemys/enemy_1.png'),image.load('images/Enemys/enemy_2.png'),image.load('images/Enemys/enemy_3.png'),image.load('images/Enemys/enemy_4.png'))
#     
#     def __init__(self,x, y, width, height):
#         sprite.Sprite.__init__(self)
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#         self.idleC = 0
#         
#     def draw(self, win):
#         win.blit(self.enemy[self.idleC//3],(self.x,self.y))
#         self.idleC += 1
#         if self.idleC >= 12:
#             self.idleC = 0
    
    
    
class Enemy(sprite.Sprite):
    
    
    enemy = (image.load('images/Enemys/enemy_1.png'),image.load('images/Enemys/enemy_2.png'),image.load('images/Enemys/enemy_3.png'),image.load('images/Enemys/enemy_4.png'))
    
    def __init__(self,x, y, width, height):
        sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.idleC = 0
        
    def draw(self, win):
        win.blit(self.enemy[self.idleC//3],(self.x,self.y))
        self.idleC += 1
        if self.idleC >= 12:
            self.idleC = 0


ninja = Player(0, 155, 64, 64) 
sword = Attack()  
red = Enemy(410, 155, 27, 21)
# Enemies.add(red)

while run:       
    time.delay(100) 
    #checks for input
    for e in event.get():
        if e.type == QUIT:
            run = False

    #array of keys *each key is assigned a number*        
    keys = key.get_pressed()
    
#     if sprite.spritecollide(ninja, red, True, True):
#         print("KIll")
    
    #============
    #KEYS INPUT
    #============

    if (keys[K_a] or keys[K_LEFT]) and ninja.x > ninja.vel:
        ninja.x -= ninja.vel
        ninja.isL = True
        ninja.isIdle = False
        ninja.isR = False
        ninja.isRunL = False
        ninja.isRunR = False
        ninja.isAtck = False
        sword.atckC = 0
        sword.atckUC = 0
    elif (keys[K_d] or keys[K_RIGHT]) and ninja.x < winWidth - ninja.width:
        ninja.x += ninja.vel
        ninja.isR = True
        ninja.isIdle = False
        ninja.isL = False
        ninja.isRunL = False
        ninja.isRunR = False
        ninja.isAtck = False
        sword.atckC = 0
        sword.atckUC = 0
    elif (keys[K_w] or keys[K_UP]) and ninja.x > ninja.vel:
        ninja.x -= ninja.vel * 2
        ninja.isRunL = True
        ninja.isIdle = False
        ninja.isRunR = False
        ninja.isR = False
        ninja.isL = False
        ninja.isAtck = False
        sword.atckC = 0
        sword.atckUC = 0
    elif (keys[K_s] or keys[K_DOWN]) and ninja.x < winWidth - ninja.width:
        ninja.x += ninja.vel * 2
        ninja.isRunR = True
        ninja.isIdle = False
        ninja.isRunL = False
        ninja.isR = False
        ninja.isL = False 
        ninja.isAtck = False
        sword.atckC = 0
        sword.atckUC = 0
    elif keys[K_k]:
        ninja.isAtck = True  
        sword.atckIsK = True 
        sword.atckIsL = False
        sword.atckIsI = False
        ninja.isIdle = False 
    elif keys[K_i]:
        ninja.isAtck = True 
        sword.atckIsI = True
        sword.atckIsK = False  
        sword.atckIsL = False 
        ninja.isIdle = False 
    elif keys[K_l]:
        ninja.isAtck = True 
        sword.atckIsL = True 
        sword.atckIsI = False
        sword.atckIsK = False  
        ninja.isIdle = False         
    else:
        ninja.idle += 1
        ninja.isIdle = True
        ninja.isAtck = False  
        
#==============
#JUMPING
#==============

    if not ninja.isJump:
        if keys[K_j]:
            ninja.isJump = True
            ninja.isIdle = False
            ninja.walkC = 0
            ninja.runC = 0
            sword.atckC = 0
            sword.atckUC = 0
    else:
        if ninja.jumpC >= -7:
            n = 1
            ninja.isUpR = True
            ninja.isUpL = True
            ninja.isDownR = False
            ninja.isDownL = False
            ninja.isIdle = False
            if ninja.jumpC < 0:
                n = -1
                ninja.isDownR = True
                ninja.isDownL = True
                ninja.isUpR = False
                ninja.isUpL = False
                ninja.isIdle = False
            ninja.y -= ((ninja.jumpC ** 2) / 2) * n 
            ninja.jumpC -= 1
        else: 
            ninja.idle = 0
            ninja.isJump = False
            ninja.jumpC = 7
            ninja.isIdle = True
            ninja.isDownR = False
            ninja.isUpR = False
            ninja.isDownL = False
            ninja.isUpL = False
    
    win.blit(bg, (0,0))  
    red.draw(win)       
    ninja.draw(win)

quit()
                