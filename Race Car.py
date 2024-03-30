# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 10:31:04 2024

@author: bluet
"""
import pygame, simpleGE, random
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("background-1.png")
        
        self.sndCrash = simpleGE.Sound("Car Crash.flac")
        
        self.racer = Racer(self)
        self.obstacles = []
        self.sprites = [self.racer, self.obstacles]
        
        for obstacle in range(3):
            self.obstacles.append(Obstacles(self))
        
    def process(self):
        for obstacle in self.obstacles:
            if obstacle.collidesWith(self.racer):
                self.sndCrash.play()
                obstacle.reset()
        if self.racer.x <= 115:
            self.racer.x = 125
        if self.racer.x >= 535:
            self.racer.x = 525
class Racer(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("AssetPack/TopDownCar.png")
        self.setSize(80,40)
        self.moveSpeed = 10
        self.position = (200,400)
        self.imageAngle = 90
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed
class Obstacles(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("AssetPack/TopDownCar.png")
        self.setSize(80,40)
        self.minSpeed = 6
        self.maxSpeed = 12
        self.imageAngle = -90
        self.reset()
        self.dy = random.randint(self.minSpeed, self.maxSpeed)
    def reset(self):
        self.y = 10
        self.x = random.randint(125,525)
        self.dy - random.randint(self.minSpeed, self.maxSpeed)
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()
