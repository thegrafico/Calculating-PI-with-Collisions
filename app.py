"""
Animation in python for calculating number Pi using collipcions
"""

import pygame

class AnimationPi():
    def __init__(self):
        """
        Setup of the animation
        """
        pygame.init()
        
        #size of the windows to play the game
        self.windows_size = 500
        self.run = True
        self.win = pygame.display.set_mode((self.windows_size,self.windows_size))

        
    def start(self):
        position_x, position_y = self.windows_size // 2, self.windows_size // 2
        rect_width, rect_height = 20, 20
        square = pygame.Rect(position_x, position_y, rect_width, rect_height)
        pygame.draw.rect(self.win, (255,0,0), square)
        
        while self.run:
            
            #Look for event every 100 miliseconds 
            for event in pygame.event.get():

                #Exit from the game
                if event.type == pygame.QUIT:
                    self.run = False
                    self.exit()
            pygame.display.update()
            
    def exit(self):
        pygame.quit()
#==

animation = AnimationPi()
animation.start()