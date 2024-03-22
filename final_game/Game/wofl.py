import random
from math import sin
class Wolf:
    def __init__(self, x, y, images, target, proj_img, buff_img_lst, pspeed):
        self.x = x
        self.y = y
        self.images = images
        self.shooting_wolves = 0
        self.current_image = 0
        self.frame_count = 0
        self.last_shot_time = 0
        self.projectiles = [] 
        self.target = target
        self.proj_img = proj_img
        self.can_shoot = False
        self.buff_img_lst = buff_img_lst
        self.pspeed = pspeed
        self.buffs = {"damage buff": None, "double_jump": None, "speed_boost": None}
    def display(self):
        image(self.images[self.current_image], self.x, self.y)
        
    def update(self):
        if self.frame_count % 10 == 0:
            self.current_image = (self.current_image + 1) % len(self.images)
        self.frame_count += 1
        
        # Automatically shoot a projectile every 1.5 seconds
        if (millis() - self.last_shot_time >= 1000) and self.can_shoot:
            self.shoot()
            self.last_shot_time = millis()

        # Update the projectiles
        for projectile in self.projectiles:
            projectile.update(self.pspeed)

    def shoot(self):
        # Create a new projectile and add it to the list

        if self.can_shoot:
            # Get the otter's previous position with a small random offset
            prev_x = self.target.position.x + random.randint(-10, 10)
            prev_y = self.target.position.y + random.randint(-10, 10)
            # Create a new projectile aimed at the previous position of the otter
            new_projectile = Projectile(self.x, self.y, [prev_x, prev_y], self.proj_img, self.pspeed)
            self.projectiles.append(new_projectile)
            self.last_shot_time = millis()
    
    def get_hitbox(self):
        # Calculate the coordinates of the hitbox.

        hitbox_x1 = self.x
        hitbox_y1 = self.y
        hitbox_x2 = self.x + self.images[0].width
        hitbox_y2 = self.y + self.images[0].height

        return [hitbox_x1, hitbox_y1, hitbox_x2, hitbox_y2]
    def drop_buff(self):
        # Define the possible buffs
        
        buff_keys = list(self.buffs.keys())
        for _ in range(9):
            buff_keys.append(None)
        
        # Randomly select a buff
        buff = random.choice(buff_keys)
        
        if buff is not None:
            # Create a new Buff object and return it
            return Buff(self.x + 50, self.y + 30, buff, self.buff_img_lst)
        else:
            return None

        

class Projectile:
    def __init__(self, x, y, target, img, pspeed):
        self.x = x
        self.y = y
        self.width = 20  # Set the width to 20px
        self.height = 20  # Set the height to 20px
        self.speed = 4
        self.img = img
        self.pspeed = pspeed
        dx = target[0] - self.x
        dy = target[1] - self.y
        dist = sqrt(dx*dx + dy*dy)
        self.direction = PVector(dx / dist, dy / dist)  # Save the direction of movement

    def update(self, speed):
        # Continue moving in the direction of the target, regardless of distance
        self.x += self.speed * self.direction.x - speed
        self.y += self.speed * self.direction.y

    def display(self):
        image(self.img, self.x, self.y)

    def is_off_screen(self):
        return self.x < 0 or self.x > width or self.y < 0 or self.y > height

    def get_hitbox(self):
        # Calculate the coordinates of the hitbox.
        hitbox_x1 = self.x
        hitbox_y1 = self.y
        hitbox_x2 = self.x + self.width
        hitbox_y2 = self.y + self.height

        return hitbox_x1, hitbox_y1, hitbox_x2, hitbox_y2
    
    
class Buff:
    def __init__(self, x, y, buff_type, imgs):
        self.x = x
        self.y = y
        self.buff_type = buff_type
        self.imgs = imgs
        self.frame_count = 0
        self.original_y = y  # Save the original y position

    def display(self):
        if self.buff_type == "damage buff":
            img = self.imgs[0]
        elif self.buff_type == "double_jump":
            img = self.imgs[1]
        elif self.buff_type == "speed_boost":
            img = self.imgs[2]
        
        # Calculate the new y position
        self.y = self.original_y + 10 * sin(self.frame_count / 10.0)
        
        image(img, self.x, self.y)
        self.frame_count += 1
    

            
    def get_hitbox(self):
        return [self.x, self.y, self.x + 50, self.y + 50]
    
