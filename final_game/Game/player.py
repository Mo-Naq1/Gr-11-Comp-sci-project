from wofl import *
class Otter:
    def __init__(self, x, y, idle_images, moving_images, proj_img, sounds):
        self.position = PVector(x, y)
        self.velocity = PVector(0, 0)
        self.grav = PVector(0, 0)
        self.jumping = False
        self.idle_images = idle_images
        self.moving_images = moving_images
        self.idle_current_image = 0
        self.idle_frame_count = 0
        self.visible = True
        self.moving = False
        self.idle = True
        self.flipped = False
        self.frame_count = 0   
        self.moving_current_image = 0
        self.game_mode = ""
        self.projectiles = []
        self.last_attack_time = 0
        self.proj_img = proj_img
        self.jump_count = 0
        self.double_jump = False
        self.speed = 7
        self.sounds = sounds
        
    def apply_force(self, force):
        if self.game_mode != "phase 2":
            self.grav.add(force)
        else:
            self.grav = PVector(0, 0.1)

        
    def update(self):
        # Change image every 10 frames to create the idle animation
        if self.idle_frame_count % 10 == 0:
            self.idle_current_image = (self.idle_current_image + 1) % 3
        self.idle_frame_count += 1
        self.velocity.add(self.grav)
        self.position.add(self.velocity)


        # Prevent the otter from falling off the canvas
        if (self.position.y + 160 - self.grav[1]) >= height:
            self.jumping = False
            self.position.y = height - 160
            self.velocity.y = 0
            
        self.grav.mult(0)  # Clear acceleration

    def jump(self):
        if not self.jumping:
            self.sounds[2].trigger()
            if self.game_mode == "phase 3":
                self.velocity.y = -25
            else:
                self.velocity.y = -13
            self.jumping = True
            
            if self.double_jump:
                self.velocity.y = -13
                self.jump_count += 1
                self.jumping = True if self.jump_count % 2 == 0 else False
    


    def display(self):
        # Display the current image
        if self.visible:
            if self.game_mode == "phase 1" or self.game_mode == "phase 3" or self.game_mode == "phase 4":
                if self.idle:
                    if self.flipped:
                        image(self.idle_images[1][self.idle_current_image], self.position.x, self.position.y)
                    else:
                        image(self.idle_images[0][self.idle_current_image], self.position.x, self.position.y)
                if self.moving:
                    if self.flipped:
                        image(self.moving_images[1][self.idle_current_image], self.position.x, self.position.y)
                    else:
                        image(self.moving_images[0][self.idle_current_image], self.position.x, self.position.y)

            if self.game_mode == "phase 2":
                image(self.moving_images[0][self.idle_current_image], self.position.x, self.position.y)
            
    def move(self, dx, dy):
        if self.game_mode != "phase 2":  # Only allow horizontal movement if not in phase 2
            if dx < 0:  # Moving left
                self.velocity.x = -self.speed
                self.flipped = True
            elif dx > 0:  # Moving right
                self.velocity.x = self.speed
                self.flipped = False
        if dy < 0:  # Moving up
            self.velocity.y = -self.speed
        elif dy > 0:  # Moving down
            self.velocity.y = self.speed
        self.moving = True
        self.idle = False

            
    def hide(self):
        self.visible = False
        
    def show(self):
        self.visible = True
        
    def stop(self): 
        self.velocity.x = 0
        
        self.idle = True
        self.moving = False

        
    def shoot(self):
        # Check if at least 1 second (1000 milliseconds) has passed since the last attack
        if millis() - self.last_attack_time >= 1000:
            # Create a new projectile and add it to the list of projectiles
            new_projectile = OtterProjectile(self.position.x, self.position.y, self.flipped, self.proj_img)
            self.projectiles.append(new_projectile)
            # Record the current time as the time of the last attack
            self.last_attack_time = millis()
        
    def fast_fall(self):
        self.velocity.y += 20

        
    def get_hitbox(self):
        # Calculate the coordinates of the hitbox. Adding values since img is 200x200, and i only need the otter
        hitbox_x1 = self.position.x + 45
        hitbox_y1 = self.position.y + 75
        hitbox_x2 = self.position.x + 130
        hitbox_y2 = self.position.y + 180

        return hitbox_x1, hitbox_y1, hitbox_x2, hitbox_y2
    

class OtterProjectile:
    def __init__(self, x, y, direction, img):
        self.x = x + 90
        self.y = y + 80
        self.direction = direction  # Save the direction of movement
        self.speed = 15  # Set a speed for the projectile's movement
        self.img = img
        
    def update(self):
        # Move the projectile in the direction the otter is facing
        if self.direction:
            self.x -= self.speed
        else:
            self.x += self.speed

    def display(self):
        # Display the projectile as a square
        image(self.img, self.x, self.y)
        
    def is_off_screen(self):
        return self.x < 0 or self.x > width or self.y < 0 or self.y > height

    def get_hitbox(self):
        # Calculate the coordinates of the hitbox.
        hitbox_x1 = self.x
        hitbox_y1 = self.y
        hitbox_x2 = self.x + 20
        hitbox_y2 = self.y + 20

        return hitbox_x1, hitbox_y1, hitbox_x2, hitbox_y2
