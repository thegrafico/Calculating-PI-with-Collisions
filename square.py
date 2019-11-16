import pygame
class Square():
        
    def __init__(self,x: int, y:int, width:int, height:int, windows_size:int, mass:int = 1,color:str = "red"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.reverse = False
        self.windows_size = windows_size
        self.color = self.get_color(color) or (255,0,0)
        self.mass = mass
        self.velocity = 0

    def get_rect(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height) 
        return self.rect
    
    
    def moveX(self):
        self.x += self.velocity
            
    def get_color(self, color:str)->tuple:
        colors = {"red": (255,0,0), "green": (0,255,0), "blue":(0,0,255)}
        self.color = colors[color] or colors["red"] 
        return self.color
    
    def is_wall_collided(self)-> bool:
        """
        verify is the object touch the bounds
        """
        # print('{} >= {} or {} <= 0'.format(self.x + self.width, self.windows_size))
        if self.x <= 0:
            self.velocity = -self.velocity
            return True
        return False
        
    
    def collide_another_square(self, other)-> bool:
        if (self.x + self.width) >= other.x or (other.x + other.width) < self.x:
            # print("Boom!", self.color)
            return True
        return False
    
    def set_velocity(self, other):
        sums = self.mass + other.mass
        
        newV = (self.mass - other.mass) / sums * self.velocity
        newV += (2* other.mass / sums) * other.velocity
        return newV