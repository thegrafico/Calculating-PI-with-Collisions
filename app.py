"""
Animation in python for calculating number Pi using collisions

There are two balls, A and B. Ball A has a larger mass and is initially moving. It collides with ball B such that ball B speeds
up and ball A slows down just a little bit (this is a perfectly elastic collision). After this, ball B starts moving toward the 
wall and eventually bounces off it back toward ball A for another collision. This continues until ball A is moving away from the
wall instead of toward it, and there are no longer any collisions.

Now for the pi part. If you know that the mass of ball A is 100 times greater than that of ball B, there will be 31 collisions.
If the ratio of masses is 10,000 to 1, there will be 314 collisions. Yes, that is the first 3 digits of pi. If you had a mass
ratio of 1 million to 1, you would get 3,141 collisions. (Remember the first few digits of pi are 3.1415 …) In general, if you want 
"d" digits of pi, then you need mass A divided by mass B to be 100 raised to the d-1 power.

"""

import pygame
from square import Square
class AnimationPi():
    def __init__(self):
        """
        Setup of the animation
        """
        pygame.init()
        pygame.mixer.music.load('coint.wav')

        self.windows_size = 600
        self.run = True
        self.white = (0,0,0)
        self.pi = 0
            
        box1_mass = 1
        box2_mass = 10000
    
       
        position_x = self.windows_size // 1.5
        self.box = Square(450, position_x, 30, 30, self.windows_size, box1_mass, "red")
        self.box2 = Square(500, position_x, 30, 30, self.windows_size,box2_mass, "blue")
        self.box2.velocity = -1
        #size of the windows to play the game
        self.win = pygame.display.set_mode((self.windows_size, self.windows_size))
        
    def start(self):
        
        rect = self.box.get_rect()
        rect2 = self.box2.get_rect()
        
        while self.run:
            #Give some time to draw
            pygame.time.delay(10)
            #Verify the bouds of the screen
            
            if self.box.is_wall_collided():
                self.pi +=1
                pygame.mixer.music.play(0)
                print(self.pi)
            
            #Get the rect  
            rect = self.box.get_rect()
            rect2 = self.box2.get_rect()
            
            #Process the event of the simulation    
            self.process_event()

            # #moving the box
            # self.box.moveX(1)
            
            if self.box.collide_another_square(self.box2):
                self.pi += 1
                pygame.mixer.music.play(0)
                print(self.pi)
                v1 = self.box.set_velocity(self.box2)
                v2 = self.box2.set_velocity(self.box)
                self.box.velocity = v1
                self.box2.velocity = v2

            self.box.moveX()
            self.box2.moveX()
            
            self.draw(rect, rect2)
    #==
    def draw(self, rect1, rect2):
        try:
            self.win.fill(self.white)
            pygame.draw.rect(self.win, self.box.color, rect1)
            pygame.draw.rect(self.win, self.box2.color, rect2)
            pygame.display.update()
        except:
            pass
    #==
    def process_event(self):
        #Look for event every 100 miliseconds 
        for event in pygame.event.get():

            #Exit from the game
            if event.type == pygame.QUIT:
                self.run = False
                self.exit()  
    #==
    def exit(self):
        pygame.quit()
#==

animation = AnimationPi()
animation.start()