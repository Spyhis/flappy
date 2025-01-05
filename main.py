
from time import sleep

import pygame
from objects.objects import *
from objects.start import Start
from objects.gameover import Gameover
from objects.score import Score, TensScore
import threading

pygame.init()

losing = False
running = True
starting = False
control = False
losingstart = True
surface = pygame.display.set_mode((width, height))

wing = pygame.mixer.Sound(os.path.join("musics", "wing.ogg"))
point = pygame.mixer.Sound(os.path.join("musics", "point.ogg"))
hit = pygame.mixer.Sound(os.path.join("musics", "hit.ogg"))

frame = pygame.time.Clock()

objects = pygame.sprite.LayeredUpdates()

Background(objects)
Background1(objects)
bird = Bird(objects)
start = Start(objects)
colonmake = pygame.USEREVENT +1
tensscore = pygame.USEREVENT +2
onesscore = pygame.USEREVENT +3

def colo():
    while True:
        if starting and not losing:
            sleep(1.3)
            pygame.event.post(pygame.event.Event(colonmake))
a = threading.Thread(target=colo, daemon=True)
a.start()

pygame.event.post(pygame.event.Event(onesscore))
score = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == colonmake:
            colon = Colon(objects)
            flipcolon = FlipColon(objects) 
        if event.type == tensscore:
            tens = TensScore(score, objects)
        if event.type == onesscore:
            ones = Score(score, objects)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and losingstart:
                starting = True
                losing = False
                wing.play()
                start.kill()
                bird.keyboard(event=event)
            if event.key == pygame.K_ESCAPE and losing:
                starting = False
                losing = False
                losingstart = True
                colon.colondel()
                flipcolon.flipcolondel() 
                gameover.kill()
                bird.kill()
                bird = Bird(objects)
                start = Start(objects)
                if score >= 10:
                    tens.kill()
                score = 0
                pygame.event.post(pygame.event.Event(onesscore))
                
    if starting and not losing:
        for object in objects:
            if type(object) == Colon and object.control():
                
                score+= 1
                pygame.event.post(pygame.event.Event(onesscore))
                if score>= 10:
                    pygame.event.post(pygame.event.Event(tensscore))
                point.play()

    if bird.check(objects) and not losing and starting:
        gameover = Gameover(objects)
        hit.play()
        losing= True
        starting = False
        losingstart = False
        pygame.time.set_timer(colonmake, 0)
    
    if losing == False and starting:
        objects.update()
        
    objects.draw(surface)
    pygame.display.flip()
    frame.tick(60)
pygame.quit()