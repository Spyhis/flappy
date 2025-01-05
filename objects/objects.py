
import os
import pygame
import random


width = 464
height = 665

#Background Class
class Background(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self.image = pygame.image.load(os.path.join("images","background.png"))
        self.rect = self.image.get_rect(topleft= (0, 0))

        super().__init__(*groups)
    def update(self):
        self.rect.x -= 2
        
        
        if self.rect.right <= 0 :
            self.rect.x = width
    
class Background1(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self.image = pygame.image.load(os.path.join("images","background.png"))
        self.rect = self.image.get_rect(topleft= (width, 0))

        super().__init__(*groups)
    def update(self):
        self.rect.x -= 2
        
        
        if self.rect.right <= 0 :
            self.rect.x = width

#Colon Class
y_ = 0
y_flip= 0
rects = []
deleted_rects= []
class Colon(pygame.sprite.Sprite):
    def __init__(self, *groups):
        global y_flip
        n = 0
        self.rando = random.uniform(530, 330)
        y_ = self.rando
        y_flip = self.rando - 400
        self.y_ = y_
        self.y_flip = y_flip

        self.image = pygame.image.load(os.path.join("images","colon.png"))
        self.rect = self.image.get_rect(topleft=(width,self.y_))
        self.mask = pygame.mask.from_surface(self.image)
        rects.append(self.rect)
        n +=1
        super().__init__(*groups)
    def update(self):
        self.rect.x -= 2
        if self.rect.x<-50:
            self.kill()

    def control(self):
        global deleted_rects
        global rects
        try:
            if rects[0].x <= 150:
                deleted_rects.append(rects[0])
                
                rects.pop(0)
                
                return True
        except:
            lambda:None        
        return False
    def colondel(self):
        global rects
        self.rects_number =len(rects)
        for i in deleted_rects:
            self.i =i
            
            self.i.x = -500
        for s in rects:

            self.s = s
            self.s.y = -500
            self.s.x =600
        for d in range(0,self.rects_number):
            self.d = d
            rects.pop(0)
        
f = []
deleted_flip_rect = []
class FlipColon(pygame.sprite.Sprite):
    def __init__(self, *groups):
        global f
        self.image = pygame.image.load(os.path.join("images","flippedcolon.png"))
        self.rect = self.image.get_rect(topleft=(width, y_flip ))
        self.mask = pygame.mask.from_surface(self.image)
        f.append(self.rect)
        super().__init__(*groups)

    def update(self):
        self.rect.x -= 2
        if self.rect.x<-50:
            self.kill()
    def control(self):
        global f
        global deleted_flip_rect
        if f[0].x <= 150:
            deleted_flip_rect.append(f[0])
            f.pop(0)
            
            
    def flipcolondel(self):
        for i in deleted_flip_rect:
            self.i = i
            self.i.y = -500
            self.i.x = 800
        for c in f:
            self.c = c
            self.c.y = -500
            self.c.x = 800
            
        self.kill()
 

#Bird Class
class Bird(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self.image = pygame.image.load(os.path.join("images","bird.png"))
        self.rect = self.image.get_rect(topleft= (-50, 200))
        self.down = 0
        self.mask = pygame.mask.from_surface(self.image)
        super().__init__(*groups)
    
    def update(self):
        self.down += 0.3
        self.rect.y += self.down
        if self.rect.x <= 150:
            self.rect.x+= 2
        if self.rect.y >= 530:
            self.down= 0
            self.down+= 0

    def keyboard(self,event):
        if event.key == pygame.K_SPACE : 
            self.down= 0
            self.down-= 5

    def check(self, objects):
        for object in objects:
            
            if ((type(object) == Colon) and object.mask.overlap(self.mask, (self.rect.x - object.rect.x, self.rect.y - object.rect.y)) or self.rect.y >=530)  :
                return True 
            if (type(object) == FlipColon) and object.mask.overlap(self.mask, (self.rect.x - object.rect.x, self.rect.y - (object.rect.y))):
                return  True
            if (type(object) == FlipColon) and object.mask.overlap(self.mask, (self.rect.x - object.rect.x, self.rect.y - (-300 +object.rect.y))):
                return  True
            if (type(object) == FlipColon) and object.mask.overlap(self.mask, (self.rect.x - object.rect.x, self.rect.y - (-600 +object.rect.y))):
                return  True
        return False
