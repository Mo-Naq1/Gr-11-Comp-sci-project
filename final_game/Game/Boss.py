import math
import random
class Boss:
    def __init__(self, x, y, images, img):
        self.x = x
        self.y = y
        self.images = images
        self.health = 14
        self.attack_phase = 0
        self.projectiles = []
        self.asteroids = []
        self.warning_time = 0
        self.current_image = 0
        self.frame_count = 0
        self.last_attack_time = 0
        self.img = img
    def display(self):
        image(self.images[self.current_image], self.x, self.y)
        
    def update(self):
        if self.frame_count % 10 == 0:
            self.current_image = (self.current_image + 1) % len(self.images)
        self.frame_count += 1

    def circular_attack(self):
        
        current_time = millis()
        if current_time - self.last_attack_time >= 2000:
            
            for _ in range(5):
                # Create 10 projectiles in a circular pattern
                num_of_projectiles = 4
                for i in range(num_of_projectiles):
                    angle = math.radians(i * (360 / num_of_projectiles))  # Divide the circle into 10 equal parts
                    speed = 5
                    dx = speed * math.cos(angle)  # Calculate the change in x
                    dy = speed * math.sin(angle)  # Calculate the change in y
        
                    # Create a new projectile with the calculated direction
                    projectile = BossProjectile(self.x+angle, self.y+angle, dx+angle*random.random(), dy+angle*random.random(), self.img)
    
                    # Add the projectile to the boss's list of projectiles
                    self.projectiles.append(projectile)
            self.last_attack_time = current_time

            
            
    def floor_attack(self):
            # Create a projectile at the left side of the floor
            projectile = BossProjectile(0, height - 50, 5, 0, self.img)  # Adjust the y-coordinate and speed as needed
            self.projectiles.append(projectile)
            
    
        
    def get_hitbox(self):
        return [self.x, self.y, self.x+300, self.y+198]
    
    def display_health_bar(self):
        # Set the dimensions of the health bar
        total_bar_width = 200
        bar_height = 20

        # Calculate the width of the health portion of the bar
        health_portion_width = int((self.health / 10.0) * total_bar_width)
        if self.health <= 0:
            health_portion_width = 0
        # Draw the background of the health bar
        fill(255, 0, 0)
        rect(self.x+10, self.y + 200, health_portion_width, bar_height)

        # Draw the health portion of the health bar

class Asteroid:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.start_time = millis()  # Record the creation time
        self.speed = 0

    def display(self):
        image(self.img, self.x, self.y)

    def update(self):
        # If 4 seconds have passed, start moving down
        self.y += self.speed

    def get_hitbox(self):
        return self.x, self.y+330, self.x + self.img.width-15, self.y + self.img.height-15
    
    def is_off_screen(self):
        return self.y > 800


class BossProjectile:
    def __init__(self, x, y, dx, dy, img):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.size = 30 
        self.img = img

    def update(self):
        # Move the projectile
        self.x += self.dx
        self.y += self.dy 

    def display(self):
        # Draw the projectile as a square
        image(self.img, self.x, self.y)

    def get_hitbox(self):
        # Return the hitbox of the projectile
        return [self.x, self.y, self.x + self.size, self.y + self.size]
    
    def is_off_screen(self):
        if self.x > width or self.x + self.size < 0 or self.y > height or self.y + self.size < 0:
            return True
        return False
