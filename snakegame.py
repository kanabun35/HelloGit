import pygame
import sys
import random
import time
from pygame.locals import * 
def run_game():
    pygame.init()
    screen = pygame.display.set_mode((600,600))
    font = pygame.font.SysFont(None, 80)
    instance = snake(20,1)
    interval = 0
    level = 4
    score = 0
    head = []
    setFeed()
    check = []
    while True:
        screen.fill((0, 0, 0))
        for i in head:
            pygame.draw.rect(screen,(255,255,255),i)
        pygame.draw.circle(screen, (255,255,255), (feedx,feedy), 8)
        if len(check) != len(set(check)):
            gameover = font.render("GAME OVER", True, (255,255,255))
            scoretext = font.render("SCORE:" + str(score), True, (255,255,255))
            screen.blit(gameover,(130,100))
            screen.blit(scoretext,(150,300))
            pygame.display.update()
            sys.exit()
        pygame.display.update()
        if interval == level:
            instance.go()
            head.insert(0,pygame.Rect(instance.x,instance.y,16,16))
            check.insert(0,str(instance.x)+str(instance.y))
            if len(head) > instance.length:
                head.pop(-1)
                check.pop(-1)
            interval = 0
        else:
            interval += 1
        if instance.x == feedx - 8 and instance.y == feedy - 8:
            instance.length += 1
            score += 100
            setFeed()
        if instance.length > 14:
            level = 1
        elif instance.length > 9:
            level = 2
        elif instance.length > 4:
            level = 3
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    instance.direction = 1
                if event.key == K_UP:
                    instance.direction = 2
                if event.key == K_LEFT:
                    instance.direction = 3
                if event.key == K_DOWN:
                    instance.direction = 4
def setFeed():
    global feedx
    global feedy
    feedx = random.randint(0,29)*20 + 8
    feedy = random.randint(0,29)*20 + 8
class snake():
    def __init__(self, speed,length):
        self.speed = speed
        self.length = length
        self.direction = 1
        self.x = 0
        self.y = 0
    def go(self):
        if self.direction == 1:
            self.x += self.speed
        elif self.direction == 2:
            self.y -= self.speed
        elif self.direction == 3:
            self.x -= self.speed
        else:
            self.y += self.speed
        if self.x > 580:
            self.x = 0
        if self.y > 580:
            self.y = 0
        if self.x < 0:
            self.x = 580
        if self.y < 0:
            self.y = 580
        return(self.x,self.y)
run_game()
