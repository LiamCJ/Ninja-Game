from pygame import *

init()

bg = image.load('images/Backgrounds/Landscape.gif')
#dimension of window
winWidth = 500
winLength = 281
#window set-up
win = display.set_mode(size=(winWidth, winLength))
display.set_caption("Shinobi Warrior")
clock = time.Clock()

run = True #when false SpaceInvaders will stop

class Player():
    #Moving Right
    runR = (image.load('images/Ninja/R_run_1.png'),image.load('images/Ninja/R_run_2.png'),image.load('images/Ninja/R_run_3.png'),image.load('images/Ninja/R_run_4.png'),image.load('images/Ninja/R_run_5.png'),image.load('images/Ninja/R_run_6.png'))
    walkR = (image.load('images/Ninja/R_walk_1.png'),image.load('images/Ninja/R_walk_2.png'),image.load('images/Ninja/R_walk_3.png'),image.load('images/Ninja/R_walk_4.png'))
    ninR = (image.load('images/Ninja/R_idle_1.png'),image.load('images/Ninja/R_idle_2.png'))
    jumpR = (image.load('images/Ninja/R_jump.png'),image.load('images/Ninja/R_land.png'))
    #Attacking Right
    kAtckR = (image.load('images/Ninja/R_attack_1.png'),image.load('images/Ninja/R_attack_2.png'),image.load('images/Ninja/R_attack_4.png'),image.load('images/Ninja/R_attack_6.png'))
    iAtckR = (image.load('images/Ninja/R_attack_1.png'),image.load('images/Ninja/R_attack_2.png'),image.load('images/Ninja/R_attack_5.png'))
    lAtckR = (image.load('images/Ninja/R_attack_1.png'),image.load('images/Ninja/R_attack_2.png'),image.load('images/Ninja/R_attack_3.png'))
    #Moving Left
    runL = (image.load('images/Ninja/L_run_1.png'),image.load('images/Ninja/L_run_2.png'),image.load('images/Ninja/L_run_3.png'),image.load('images/Ninja/L_run_4.png'),image.load('images/Ninja/L_run_5.png'),image.load('images/Ninja/L_run_6.png'))
    walkL = (image.load('images/Ninja/L_walk_1.png'),image.load('images/Ninja/L_walk_2.png'),image.load('images/Ninja/L_walk_3.png'),image.load('images/Ninja/L_walk_4.png'))
    ninL = (image.load('images/Ninja/L_idle_1.png'),image.load('images/Ninja/L_idle_2.png'))
    jumpL = (image.load('images/Ninja/L_jump.png'),image.load('images/Ninja/L_land.png'))
    #Attacking Left
    kAtckL = (image.load('images/Ninja/L_attack_1.png'),image.load('images/Ninja/L_attack_2.png'),image.load('images/Ninja/L_attack_4.png'),image.load('images/Ninja/L_attack_6.png'))
    iAtckL = (image.load('images/Ninja/L_attack_1.png'),image.load('images/Ninja/L_attack_2.png'),image.load('images/Ninja/L_attack_5.png'))
    lAtckL = (image.load('images/Ninja/L_attack_1.png'),image.load('images/Ninja/L_attack_2.png'),image.load('images/Ninja/L_attack_3.png'))
    
    def __init__(self, x, y, width, height):
        #co-ordinates of player
        self.x = x
        self.y = y
        #dimension of player
        self.width = width
        self.height = height
        self.atckUC = 0  
        self.jumpC = 7
        self.atckC = 0
        self.walkC = 0
        self.runC = 0 
        self.idle = 0     
        self.vel = 5 #velocity of player
        self.isDownR = False
        self.isDownL = False
        self.atckIsK = False
        self.atckIsI = False
        self.atckIsL = False
        self.isRunR = False
        self.isRunL = False
        self.isJump = False
        self.isUpR = False
        self.isUpL = False
        self.isIdle = True
        self.isL = False
        self.isR = True
         

    def draw(self, win):
        win.blit(bg, (0,0)) 

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

                    if self.isR or self.isRunR:
                        if self.atckIsK:
                            win.blit(self.kAtckR[self.atckC//2],(self.x,self.y))
                            self.atckC += 1
                            if self.atckC >=7:
                                self.atckC = 0
                        elif self.atckIsI:
                            win.blit(self.iAtckR[self.atckUC//2],(self.x,self.y))
                            self.atckUC += 1
                            if self.atckUC >=6:
                                self.atckUC = 0
                        elif self.atckIsL:
                            win.blit(self.lAtckR[self.atckUC//2],(self.x,self.y))
                            self.atckUC += 1
                            if self.atckUC >=6:
                                self.atckUC = 0
                    elif self.isL or self.isRunL:
                        if self.atckIsK:
                            win.blit(self.kAtckL[self.atckC//3],(self.x,self.y))
                            self.atckC += 1
                            if self.atckC >=12:
                                self.atckC = 0
                        elif self.atckIsI:
                            win.blit(self.iAtckL[self.atckUC//3],(self.x,self.y))
                            self.atckUC += 1
                            if self.atckUC >=8:
                                self.atckUC = 0
                        elif self.atckIsL:
                            win.blit(self.lAtckL[self.atckUC//3],(self.x,self.y))
                            self.atckUC += 1
                            if self.atckUC >=8:
                                self.atckUC = 0
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
    
ninja = Player(60, 160, 64, 64)   

while run:        
    time.delay(100) 
    #checks for input
    for e in event.get():
        if e.type == QUIT:
            run = False

    #array of keys *each key is assigned a number*        
    keys = key.get_pressed()

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
        ninja.atckC = 0
        ninja.atckUC = 0
    elif (keys[K_d] or keys[K_RIGHT]) and ninja.x < winWidth - ninja.width:
        ninja.x += ninja.vel
        ninja.isR = True
        ninja.isIdle = False
        ninja.isL = False
        ninja.isRunL = False
        ninja.isRunR = False
        ninja.isAtck = False
        ninja.atckC = 0
        ninja.atckUC = 0
    elif (keys[K_w] or keys[K_UP]) and ninja.x > ninja.vel:
        ninja.x -= ninja.vel * 2
        ninja.isRunL = True
        ninja.isIdle = False
        ninja.isRunR = False
        ninja.isR = False
        ninja.isL = False
        ninja.isAtck = False
        ninja.atckC = 0
        ninja.atckUC = 0
    elif (keys[K_s] or keys[K_DOWN]) and ninja.x < winWidth - ninja.width:
        ninja.x += ninja.vel * 2
        ninja.isRunR = True
        ninja.isIdle = False
        ninja.isRunL = False
        ninja.isR = False
        ninja.isL = False 
        ninja.isAtck = False
        ninja.atckC = 0
        ninja.atckUC = 0
    elif keys[K_k]:
        ninja.isAtck = True  
        ninja.atckIsK = True 
        ninja.atckIsL = False
        ninja.atckIsI = False
        ninja.isIdle = False 
    elif keys[K_i]:
        ninja.isAtck = True 
        ninja.atckIsI = True
        ninja.atckIsK = False  
        ninja.atckIsL = False 
        ninja.isIdle = False 
    elif keys[K_l]:
        ninja.isAtck = True 
        ninja.atckIsL = True 
        ninja.atckIsI = False
        ninja.atckIsK = False  
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
            ninja.atckC = 0
            ninja.atckUC = 0
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
            
    ninja.draw(win)
        
quit()
                