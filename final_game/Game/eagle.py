class Eagle:
    def __init__(self, x, y, images):
        self.x = x
        self.y = y
        self.images = images  
        self.frame_count = 0
        self.flipped = False
        self.speed = 7  # Define a speed for the eagle's movement
        self.hitbox = (150, 50)  # Define the hitbox size
        self.current_image = 0  # Current image index

    def update(self):
        # Change image every 10 frames to create the idle animation

        if self.frame_count % 10 == 0:
            self.current_image = (self.current_image + 1) % len(self.images[0])
        self.frame_count += 1

        # Move the eagle
        self.x += self.speed

        # If the eagle hits the edge of the screen, flip the direction
        if self.x + self.hitbox[0] > width: 
            self.speed = -self.speed
            self.flipped = True
        elif self.x < 0:
            self.speed = -self.speed
            self.flipped = False

    def display(self):
        # Display the current image
        if self.flipped:
            image(self.images[1][self.current_image], self.x, self.y)
        else:
            image(self.images[0][self.current_image], self.x, self.y)
