import random
from circleshape import *
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 0), self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
        
        random_angle = random.uniform(20, 50)
        asteroid_1_vector = self.velocity.rotate(random_angle)
        asteroid_2_vector = self.velocity.rotate(-random_angle)
        new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        asteroid_1.velocity = asteroid_1_vector * 1.2
        asteroid_2.velocity = asteroid_2_vector * 1.2
        

        self.kill()
