from pygame.math import Vector2
from imagesound import load_sprite, wrap_position,get_random_velocity
from pygame.transform import rotozoom

UP = Vector2(0, -1)

class GameObject:
    def __init__(self, position, sprite, velocity):
        self.position = Vector2(position)
        self.sprite = sprite
        self.radius = sprite.get_width() / 2
        self.velocity = Vector2(velocity)

    def draw(self, surface):
        blit_position = self.position - Vector2(self.radius)
        surface.blit(self.sprite, blit_position)

    def move(self, surface):
        self.position = wrap_position(self.position + self.velocity, surface)

    def collides_with(self, other_obj):
        distance = self.position.distance_to(other_obj.position)
        return distance < self.radius + other_obj.radius

class Player(GameObject):
    TURN=3
    ACCE=0.02
    HIT = 3
    def __init__(self, position):
      
        
        self.direction = Vector2(UP)
        super().__init__( position, load_sprite(f"model/player"), Vector2(0))
    
    def accelerate(self):
        self.velocity += self.direction * self.ACCE

    def decelerate(self):
        self.velocity -= self.direction * self.ACCE

    def goright(self):
        self.position = self.position + (10,0)

    def goleft(self):
        self.position = self.position - (10,0)

    def goup(self):
        self.position = self.position + (0,10)

    def godown(self):
        self.position = self.position - (0,10)

    

class animal(GameObject):
    def __init__(self, position):
        super().__init__(position, load_sprite(f"model/m1"), get_random_velocity(1, 3))

class animalSmall(GameObject):
    def __init__(self, position):
        super().__init__(position, load_sprite(f"model/m2"), get_random_velocity(2, 4))
        
class bird(GameObject):
    def __init__(self, position):
        super().__init__(position, load_sprite(f"model/b1"), get_random_velocity(1, 3))

class birdSmall(GameObject):
    def __init__(self, position):
        super().__init__(position, load_sprite(f"model/b2"), get_random_velocity(2, 4))


