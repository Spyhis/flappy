import pygame
import os

b = 0
numbers = []
deleted_numbers = []
class Score(pygame.sprite.Sprite):
    def __init__(self,score, *groups):
        global b
        global numbers
        global deleted_numbers
        self.score = score
        a = 0
        self.path =  os.path.join("images")
        self.numbers = numbers
        if b == 0:
            for i in os.listdir(self.path):
                
                numbers.append(i)
                if a == 10:
                    break
        
        if b >= 1:
            self.delete()
        
        self.score_ones = score % 10   
        self.image = pygame.image.load(os.path.join("images",self.numbers[self.score_ones]))
        self.rect = self.image.get_rect(topleft = (40,20))
        
        deleted_numbers.append(self.rect)
        b+= 1

                                                                                                                                      
        super().__init__(*groups)
    
    def delete(self):
        global deleted_numbers
        deleted_numbers[0].x = -600
        deleted_numbers.pop(0)



deleted_numbers_1 = []       
c = 0
numberss = []
class TensScore(pygame.sprite.Sprite):
    def __init__(self,score, *groups):
        global deleted_numbers_1
        global c
        a = 0
        self.path =  os.path.join("images")
        self.numbers = numberss
        if c == 0:
            for i in os.listdir(self.path):
                a += 1
                self.numbers.append(i)
                if a == 10:
                    break
        if c>= 1:
            self.delete()
        
        self.score_tens = score // 10   
        self.image = pygame.image.load(os.path.join("images",self.numbers[self.score_tens]))
        self.rect = self.image.get_rect(topleft = (20,20))

        deleted_numbers_1.append(self.rect)
        
        c += 1

        super().__init__(*groups)

    def delete(self):
        global deleted_numbers_1
        deleted_numbers_1[0].x = -600
        deleted_numbers_1.pop(0)