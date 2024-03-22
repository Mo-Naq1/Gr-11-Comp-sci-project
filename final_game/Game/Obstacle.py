from math import sin, cos
class Obstacle:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img  
        self.speed = 0  # Define a speed for the obstacle's movement
        self.current_image = 0  # Current image index
        self.angle = 0  # Initialize angle for circular motion
        self.radius = 2  # Define the radius for the circular motion

    def update(self):
        # Move the obstacle
        self.x -= self.speed
        # Update the angle
        self.angle += 0.1
        # Make the obstacle move in a subtle circle
        self.x += self.radius * cos(self.angle)*2  # Adjust the multiplier as needed
        self.y += self.radius * sin(self.angle)  # Adjust the multiplier as needed

    def display(self):
    
        image(self.img, self.x, self.y)

    def get_hitbox(self):
        # Default hitbox, can be overridden by child classes
        return self.x, self.y, self.x + self.img.width, self.y + self.img.height

class Pizza(Obstacle):
    def get_hitbox(self):
        # Custom hitbox for Pizza
        return self.x + 10, self.y + 10, self.x + self.img.width - 10, self.y + self.img.height - 10

class Cup(Obstacle):
    def get_hitbox(self):
        # Custom hitbox for Cup
        return self.x + 20, self.y + 20, self.x + self.img.width - 20, self.y + self.img.height - 20

class Soda(Obstacle):
    def get_hitbox(self):
        # Custom hitbox for Soda
        return self.x + 15, self.y + 15, self.x + self.img.width - 15, self.y + self.img.height - 15
