add_library("minim")
from player import *
from eagle import *
from Obstacle import *
from wofl import *
from Boss import *
import random


character_visible = True
lives = 3
obstacles = []
obstacle_images = []
tile_width = 115
tile_height = 20  # Adjust this to make the platforms thinner
max_platform_length = 2
is_jumping = False

platforms = []
platforms_phase4 = []
platforms_2 = []
idle_images_otter = [[], []]
moving_images_otter = [[], []]
eagle_images = [[], []]
active_buffs = []
wolf_images = []
buff_images = []
boss_images = []
sound_effects = []
sound_effect_running = False

x1_p2 = 0
x2_p2 = 1200
x1_p3 = 0
x2_p3 = 1200
wolves_defeated = 0
eagles = []
wolves = []

attack_images = []
held_keys = []
previous_phase = [None]
move_platform = None
change_state = False

buffs = {"damage buff": None, "double_jump": None, "speed_boost":None}
stage_2_counter = 0
orb = 0
game_state = "pre 0"
round_start = 0
warning_time = 0
otter = 0

# BOSS VARIABLES
asteroids = []
attack = 1
start_time = 0
dmg = 1

def setup():
    global otter, cloud, grass_tile, platform_y, game_state, bg_clouds, portal, eagle, lives_2, lives_1, gg, bg_2, otter, stone_tile, previous_otter_x, bg_3, fireball, orb, pre_p1, pre_p2, pre_p3, buff_images, pre_p0, pre_p4, arena, asteroid_img, lava_tile, boss, warning1, warning2, warning3, warning4, ball, winner
    global jump, speed, dmg_img, start_music
    size(1200, 800)
    orb = loadImage("orb.png")
    ball = loadImage("ball.png")
    otter = Otter(500, 530, idle_images_otter, moving_images_otter, orb, sound_effects)
    boss = Boss(width/2-80, height/2-20, boss_images, ball)
    previous_otter_x = otter.position.x
    # otter = Otter(0, height/2, idle_images_otter, moving_images_otter)
    cloud_1 = [random.randint(0, width,), random.randint(-50, 800)]
    cloud_2 = [random.randint(0, width,), random.randint(-50, 800)]
    cloud_3 = [random.randint(0, width,), random.randint(-50, 800)]
    bg_clouds = [cloud_1, cloud_2, cloud_3]
    generate_platforms_phase1()
    generate_eagles()
    
        # Spawn the otter at the left middle side of the screen
    reset_round_phase_1()
        
    platform_width = 115
    platform_height = 20 
    
    platforms_phase4.append([373, 661, platform_width, platform_height])
    platforms_phase4.append([775, 608, platform_width, platform_height])
    platforms_phase4.append([821, 500, platform_width, platform_height])
    platforms_phase4.append([758, 375, platform_width, platform_height])
    platforms_phase4.append([758, 228, platform_width, platform_height])
    platforms_phase4.append([179, 551, platform_width, platform_height])
    platforms_phase4.append([257, 393, platform_width, platform_height])
    platforms_phase4.append([392, 248, platform_width, platform_height])   
    
    idle_images_otter[0].append(loadImage("otter_idle_1.png"))
    idle_images_otter[0].append(loadImage("otter_idle_3.png"))
    idle_images_otter[0].append(loadImage("otter_idle_2.png"))
    idle_images_otter[1].append(loadImage("otter_idle_1_f.png"))
    idle_images_otter[1].append(loadImage("otter_idle_2_f.png"))
    idle_images_otter[1].append(loadImage("otter_idle_3_f.png"))
    moving_images_otter[0].append(loadImage("otter_run_1.png"))
    moving_images_otter[0].append(loadImage("otter_run_2.png"))
    moving_images_otter[0].append(loadImage("otter_run_3.png"))
    moving_images_otter[1].append(loadImage("otter_run_1_f.png"))
    moving_images_otter[1].append(loadImage("otter_run_2_f.png"))
    moving_images_otter[1].append(loadImage("otter_run_3_f.png"))
    grass_tile = loadImage("platform_grass.png")
    stone_tile = loadImage("platform_stone.png")
    eagle_images[0].append(loadImage("eagle_1.png"))
    eagle_images[0].append(loadImage("eagle_2.png"))
    eagle_images[0].append(loadImage("eagle_3.png"))
    eagle_images[1].append(loadImage("eagle_1_f.png"))
    eagle_images[1].append(loadImage("eagle_2_f.png"))
    eagle_images[1].append(loadImage("eagle_3_f.png"))
    obstacle_images.append(loadImage("trash_1.png"))
    obstacle_images.append(loadImage("trash_2.png"))
    obstacle_images.append(loadImage("trash_3.png"))
    wolf_images.append(loadImage("wolf_1.png"))
    wolf_images.append(loadImage("wolf_2.png"))
    wolf_images.append(loadImage("wolf_3.png"))
    wolf_images.append(loadImage("wolf_4.png"))
    wolf_images.append(loadImage("wolf_5.png"))
    buff_images.append(loadImage("dmgbuff.png"))
    buff_images.append(loadImage("jumpbuff.png"))
    buff_images.append(loadImage("speedbuff.png"))
    fireball = loadImage("fireball.png")
    pre_p1 = loadImage("The Climb.png")
    pre_p2 = loadImage("underturtle.png")
    pre_p3 = loadImage("corruptsouls.png")
    pre_p4 = loadImage("destroyerscreen.png")
    bg_2 = loadImage("bg2.png")
    bg_3 = loadImage("bg_3.png")
    lives_2 = loadImage("2_lives.png")
    lives_1 = loadImage("1_lives.png")
    pre_p0 = loadImage("lore.png")
    gg = loadImage("0_lives.png")
    arena = loadImage("hellarena.png")
    boss_images.append(loadImage("boss1.png"))
    boss_images.append(loadImage("boss2.png"))
    boss_images.append(loadImage("boss3.png"))
    boss_images.append(loadImage("boss4.png"))
    warning1 = loadImage("warning1.png")
    warning2 = loadImage("warning2.png")
    warning3 = loadImage("warning3.png")
    warning4 = loadImage("warning4.png")
    asteroid_img = loadImage("asteroid.png")
    lava_tile = loadImage("lava_tile.png")
    winner = loadImage("winner.png")
    jump = loadImage("jumpbuff_collected.png")
    dmg_img = loadImage("dmgbuff_collected.png")
    speed = loadImage("speedbuff_collected.png")
    minim = Minim(this)
    sound_effects.append(minim.loadSample("death.mp3"))
    sound_effects.append(minim.loadSample("gamewon.mp3"))
    sound_effects.append(minim.loadSample("jumpsound.mp3"))
    sound_effects.append(minim.loadSample("ottershot.mp3"))
    sound_effects.append(minim.loadSample("fireball.mp3"))
    sound_effects.append(minim.loadSample("buffcollected.mp3"))
    start_music = minim.loadFile("music.mp3")
    start_music.play()
    
    for set_imgs in eagle_images:
        for img in set_imgs:
            img.resize(130, 70)
    
    for imgs in wolf_images:
        imgs.resize(130, 90)
    
    
    asteroid_img.resize(179, 460)
    bg_3.resize(width+6, height+6)
    obstacle_images[0].resize(162, 66)
    portal = loadImage("portal.png")
    cloud = loadImage("cloud.png")
    if not asteroids:
        generate_asteroids()



def draw():
    global held_keys, cloud, platforms, game_state, respawn_time,otter, otter, previous_phase, platforms_2, lives, active_buffs, stage_2_counter, start_time
    bg_2.resize(width, height)
    collision = False
    gravity = PVector(0, 0.5)


    if game_state == "pre 0":
        image(pre_p0, 0, 0)

            
    if game_state == "pre 1":
        start_music.pause()
        image(pre_p1, 0, 0)
        reset_round_phase_1()
        if change_state == True:
            lives = 3
            game_state = "phase 1"
            
    if game_state == "pre 2":
        image(pre_p2, 0, 0)
        reset_round_phase_2()
        if change_state == True:
            transition_to_phase_2()
        
    if game_state == "pre 3":
        image(pre_p3, 0, 0)
        reset_round_phase_3()
        if change_state == True:
            transition_to_phase_3()
            
    if game_state == "pre 4":
        image(pre_p4, 0, 0)
        reset_round_phase_4()
        if mousePressed:
            transition_to_phase_4()
            
            
            
    if game_state == "phase 1":
        otter.apply_force(gravity)
        previous_phase[0] = "phase 1"
        frameRate(60)
        phase_1()
        otter.game_mode = "phase 1"
        collision = True
        otter.display()
        otter.update()
        for eagle in eagles:
            eagle.display()
            eagle.update()
        if move_platform == True and last_platform[1] < 300:
            move_platforms()
            
    if game_state == "phase 2":
        previous_phase[0] = "phase 2"
        otter.game_mode = "phase 2"
        phase_2()
        otter.display()
        otter.update()
        
        
    if game_state == "phase 3":
        otter.apply_force(gravity)
        phase_3()
        otter.game_mode = "phase 3"
        otter.display()
        otter.update()
        for projectile in otter.projectiles:
            projectile.update()
            projectile.display()
                    
    if game_state == "phase 4":
        previous_phase[0] = "phase 4"
        otter.game_mode = "phase 4"
        otter.apply_force(gravity)
        phase_4()
        otter.display()
        otter.update()
        boss.display()
        boss.update()
        for projectile in otter.projectiles:
            projectile.update()
            projectile.display()
            
    if game_state == "win":
        image(winner, 0, 0)
    if game_state == "life lost":
        life_lost()
        otter.velocity.y = 0
        
    if game_state == "game over":
        game_over()
        
    if collision == True:
        collide()
    

    movement(held_keys)
    # Apply gravity to the otter
    
    
    
########################################################################################################################################################################################################################################################################################
########################################################################################################################################################################################################################################################################################
################################### TRANSITIONAL FUNCTIONS ##################


def transition_to_phase_2():
    global game_state, otter, platforms, obstacles, stage_2_counter, lives
    frameRate(10)
    otter.velocity.y = 0
    frameRate(60)
    frameRate(10)
    platforms = []
    obstacles = []
    lives = 3
    # Change the game state to phase 2
    game_state = "pre 2"
    
def transition_to_phase_3():
    global game_state, previous_phase, lives
    lives = 3
    frameRate(10)
    game_state = "phase 3"
    previous_phase[0] = "phase 3"
    otter.position = PVector(width/2, height-120)
    
    
def transition_to_phase_4():
    global game_state, previous_phase, lives, asteroids, start_time
    start_time = millis()
    lives = 3
    asteroids = []
    generate_asteroids()
    frameRate(10)
    boss.projectiles = []
    game_state = "phase 4"
    previous_phase[0] = "phase 4"
    otter.position = PVector(width/2, height-120)
    
########################################################################################################################################################################################################################################################################################
########################################################################################################################################################################################################################################################################################
################################### PHASE 1 #####################################################################################################################################################################################################################################################
# GAME PHASE 1 - CLIMBING
def phase_1():
    global previous_phase, platforms, move_platform, eagles, last_platform
    on_ground = False
    previous_phase[0] = "phase 1"
    background("#87CEEB")
    # CODE FOR GRADIENT BACKGROUND
    for i in range(height):
        # Calculate a color based on the current row
        inter = map(i, 0, height, 0, 1)
        c = lerpColor(color(0, 0, 130), color(130, 206, 235), inter)
        # Set the stroke color
        stroke(c)
        # Draw a line across the screen at this height
        line(0, i, width, i)
    # Check if the otter collides with the portal
    portal_hitbox = [last_platform[0], last_platform[1], last_platform[0] + tile_width+20, last_platform[1] + tile_height+200]
    if is_colliding(otter.get_hitbox(), portal_hitbox):
        frameRate(10)
        clear()
        transition_to_phase_2()
    draw_platforms()


def reset_round_phase_1():
    global platforms, move_platform, eagles
    platforms = []  # Clear the existing platforms
    generate_platforms_phase1()  # Generate the platforms again
    move_platform = False  # Stop the platforms from moving
    
    eagles = []
    generate_eagles()
    otter.velocity.y = 0     
    
def generate_eagles():
    global eagles
    for i in range(15):
        eagle = Eagle(random.randint(100, width-100), -4500+(300*(i+1)), eagle_images)
        eagles.append(eagle)


# FUNCTION FOR CREATING PLATFORMS
def generate_platforms_phase1():
    global last_platform
    l_border_x = 400
    r_border_x = 900
    for j in range(38):
        platform_length = random.randint(1, max_platform_length)
        ground_platform = [530, 730, tile_width, tile_height]
        last_platform = [450, -5500]
        portal_platform = [540, -5150, tile_width, tile_height]
        platforms.append(portal_platform)
        initial_platform = [random.randint(l_border_x, r_border_x-tile_width), -5150+(150*(j+1)), tile_width, tile_height]
        platforms.append(ground_platform)
        platforms.append(initial_platform)  
        
        last_x_coord = initial_platform[0]
        for i in range(platform_length-1):
            if last_x_coord + tile_width <= r_border_x:
                additional_platform = [initial_platform[0] + tile_width*(i+1), initial_platform[1], tile_width, tile_height]
                last_x_coord = additional_platform[0]
                platforms.append(additional_platform)
            else:
                break
        
    

def draw_platforms():
    for cloud_coord in bg_clouds:
        cloud.resize(300, 100)
        image(cloud, cloud_coord[0], cloud_coord[1])
        
    for platform in platforms:
        image(grass_tile, platform[0], platform[1])
    
    portal.resize(300, 400)
    image(portal, last_platform[0], last_platform[1])


def move_platforms():
    for platform in platforms:
        platform[1] += 2 # CONSTANT LOWERING OF PLATFORMS
        if is_jumping:
            if otter.velocity.y < 0:
                platform[1] -= otter.velocity.y/1.2
    for cloud in bg_clouds:
        cloud[1] += 2
        if is_jumping:
            if otter.velocity.y < 0:
                cloud[1] -= otter.velocity.y/1.2
    if cloud[1] > 850:
        cloud[1] = -100
        cloud[0] = random.randint(0, width)
    
    for eagle in eagles:
        eagle.y += 2
        if is_jumping:
            if otter.velocity.y < 0:
                eagle.y -= otter.velocity.y/1.2
    last_platform[1] += 2
    if is_jumping:
        if otter.velocity.y < 0:
            last_platform[1] -= otter.velocity.y/1.2
            

########################################################################################################################################################################################################################################################################################
########################################################################################################################################################################################################################################################################################
################################### PHASE 2 #####################################################################################################################################################################################################################################################
def phase_2():
    global otter, obstacles, lives, game_state, respawn_time, previous_phase, stage_2_counter, x1_p2, x2_p2
    otter.position.x = 0
    
    previous_phase[0] = "phase 2"
    frameRate(60)
    speed = 2 
    
    x1_p2 -= speed
    x2_p2 -= speed
    
    # If the first image has moved off the screen, reset it to the right
    if x1_p2 < -width:
        x1_p2 = width
    
    # If the second image has moved off the screen, reset it to the right
    if x2_p2 < -width:
        x2_p2 = width

    image(bg_2, x1_p2, 0)
    image(bg_2, x2_p2, 0)
    # Move the otter to the right

    # Generate obstacles
    if frameCount % 40 == 0:  # Every 60 frames
        generate_obstacle()

    # Display and update obstacles
    for obstacle in obstacles:
        obstacle.display()
        obstacle.update()

    # Check for collisions
    for obstacle in obstacles:
        if is_colliding(otter.get_hitbox(), obstacle.get_hitbox()):
            lives -= 1
            sound_effects[0].trigger()
            frameRate(10)
            otter.velocity.y = 0
            if lives > 0:
                game_state = "life lost"
                respawn_time = millis()  # Record the current time
            else:
                game_state = "game over"
    
    if otter.position.y <= -80:
        otter.position.y = -80
    
    time_remaining = 15 - int((millis() - stage_2_counter)/1000)
    if (millis() - stage_2_counter < 15000):  # If 15 seconds have not passed
        textSize(32)
        text("Time Remaining {} (seconds)".format(time_remaining), 350, 100)
    else:
        clear()
        game_state = "pre 3"

        
def generate_obstacle():
    global obstacles, obstacle_images, random_obstacle_class, game_state, held_keys
    if game_state == "phase 2":
        obstacle_classes = [Pizza, Cup, Soda]
        img = random.choice(obstacle_images)
        random_obstacle_class = random.choice(obstacle_classes)
        obstacle = random_obstacle_class(width+100, random.randint(0, height), img)
        obstacle.speed = 5
        # Choose a random image for the obstacle
   
        # Create the obstacle off the right side of the screen, at a random y-coordinate

        # Add the obstacle to the list
        obstacles.append(obstacle)
    
def reset_round_phase_2():
    global obstacles,stage_2_counter
    obstacles = []  # Clear the existing obstacles
    generate_obstacle()  # Generate the obstacles again
    otter.position = PVector(0, height/2)
    stage_2_counter = millis()

########################################################################################################################################################################################################################################################################################
########################################################################################################################################################################################################################################################################################
################################### PHASE 3 #########################################################################################################################################################################################

def phase_3():
    global platforms_2, wolves, previous_otter_x, x1_p3, x2_p3, bg_3, lives, game_state, respawn_time, active_buffs, wolves_defeated, round_start, buffs
    frameRate(60)
    speed = (otter.position.x - previous_otter_x) *2
    x1_p3 -= speed
    x2_p3 -= speed
    # If the first image has moved off the screen, reset it to the right
    if x1_p3 < -width:
        x1_p3 = width
    # If the first image has moved off the screen to the right, reset it to the left
    elif x1_p3 > width:
        x1_p3 = -width

    # If the second image has moved off the screen, reset it to the right
    if x2_p3 < -width:
        x2_p3 = width
    # If the second image has moved off the screen to the right, reset it to the left
    elif x2_p3 > width:
        x2_p3 = -width

    image(bg_3, x1_p3, 0)
    image(bg_3, x2_p3, 0)

    previous_phase[0] = "phase 3"
    # Generate platforms and wolves if not already generated
    if not platforms_2:
        generate_platforms2()
    if not wolves:
        generate_wolves()

    # Display and update platforms and wolves
    for platform in platforms_2:
        image(stone_tile, platform[0], platform[1])
        platform[0] -= speed
    for wolf in wolves:
        wolf.x -= speed
    for buff in active_buffs:
        buff.x -= speed
    previous_otter_x = otter.position.x
    
    
    if otter.position.x >= 1065:
        otter.position.x = 1065
    if otter.position.x <= 0:
        otter.position.x = 0
        
    

    for wolf in wolves:
        wolf.display()    
        wolf.update()
        if (millis() - round_start > 3000):
            wolf.can_shoot = True
            for projectile in wolf.projectiles:
                projectile.display()
                projectile.update(speed)
                if projectile.is_off_screen():
                    wolf.projectiles.remove(projectile)
                elif is_colliding(otter.get_hitbox(), projectile.get_hitbox()):
                    # Handle collision
                    lives -= 1
                    sound_effects[0].trigger()
                    wolf.projectiles.remove(projectile)
                    if lives > 0:
                        game_state = "life lost"
                        speed = 0
                        x1_p3 = 0
                        x2_p3 = 1200
                        respawn_time = millis()  # Record the current time
                    else:
                        game_state = "game over"
        else:
            wolf.can_shoot = False
            

    for wolf in wolves:
        for projectile in otter.projectiles:
            if is_colliding(wolf.get_hitbox(), projectile.get_hitbox()):
                # Remove the wolf and the projectile
                wolves.remove(wolf)
                wolves_defeated += 1
                otter.projectiles.remove(projectile)
  
                # Drop a buff and add it to the list of active buffs
                buff = wolf.drop_buff()
                if buff is not None:
                    active_buffs.append(buff)
    for buff in active_buffs:
        buff.display()


        if is_colliding(otter.get_hitbox(), buff.get_hitbox()):
            # The otter has collected the buff
            active_buffs.remove(buff)
            buffs[buff.buff_type] = True  # Set the corresponding key in the dictionary to True
            sound_effects[5].trigger()
    
    if wolves_defeated == 10:

        game_state = "pre 4"
        
    draw_buffs()
def generate_platforms2():
    global platforms_2
    l_border_x = -800

    for j in range(10):
        y_coord = random.randint(150, 500 - tile_height)
        x_coord = random.gauss(600, 700)
        # Add all y-coordinates within the height of the platform to the set
        while x_coord < -800 or x_coord > 2000:
            x_coord = random.gauss(600, 700)
        platforms_2.append([x_coord*1.2, y_coord*1.2, tile_width, tile_height])

def generate_wolves():
    global wolves, platforms_2
    speed = (otter.position.x - previous_otter_x) *2
    for platform in platforms_2:
        wolf = Wolf(platform[0], platform[1] - 75, wolf_images, otter, fireball, buff_images, speed)
        wolves.append(wolf)
        
def reset_round_phase_3():
    global platforms_2, wolves, otter, previous_otter_x, x1_p3, x2_p3, active_buffs, round_start
    # Clear the existing buffs
    active_buffs = []

    # Reset the otter's position if necessary
    otter.position.x = previous_otter_x
    # Reset the background's x-coordinates
    x1_p3 = (x1_p3 // width) * width  # Ensure x1_p3 is a multiple of width
    x2_p3 = x1_p3 + width  # Ensure x2_p3 is exactly one image width away from x1_p3
    for wolf in wolves:
        wolf.can_shoot = False
        for key in wolf.buffs:
            wolf.buffs[key] = None
    round_start = millis()
    

########################################################################################################################################################################################################################################################################################
########################################################################################################################################################################################################################################################################################
################################### PHASE 4 #########################################################################################################################################################################################
def phase_4():
    global asteroids, platforms_phase4, otter, game_state, lives, respawn_time, attack, start_time, dmg
    print(buffs)
    frameRate(60)
    background(255)
    
    otter.speed = 7
    image(arena, 0, 0)
    if attack != 3:
        for platform in platforms_phase4:
            image(lava_tile, platform[0], platform[1])
        for platform in platforms_phase4:
            platform_hitbox = [platform[0], platform[1], platform[0] + tile_width, platform[1] + tile_height]
            if is_colliding(otter.get_hitbox(), platform_hitbox):
                # Check if the otter's feet are above the platform and the otter is moving downwards
                otter_bottom = otter.position.y + 160  # 85 is the height of the otter
                if otter_bottom <= platform[1] and otter.velocity.y > 0:  # platform[1] is the y-coordinate of the platform
                    otter.jumping = False
                    # Reset the otter's vertical velocity
                    otter.velocity.y = 0
                    # Adjust the otter's y position to be on top of the platform
                    otter.position.y = platform[1] - 160.6
    previous_attack = attack

    if attack == 1:
        if delay_before_attack(attack, start_time):
            if len(asteroids) > 0:
                for asteroid in asteroids:
                    asteroid.update()
                    asteroid.display()
                    if asteroid.is_off_screen():
                        asteroids.remove(asteroid)
                asteroid_hit()
            else:
                previous_attack = attack
                attack = 2
                start_time = millis()
                asteroids = []

                

    if attack == 2:
        if delay_before_attack(attack, start_time, 3000):
            if millis() - start_time <= 12000:   
                boss.circular_attack()
                for projectile in boss.projectiles:  # Iterate over a copy of the list
                    projectile.update()
                    projectile.display()
            
                    # Check for collisions with the otter
                    if is_colliding(otter.get_hitbox(), projectile.get_hitbox()):
                        print("Otter collided with a projectile!")
                        lives -= 1
                        sound_effects[0].trigger()
                        if lives > 1:
                            respawn_time = millis()
                            game_state = "life lost"
                        else:
                            game_state = "game over"
                       
                    # Remove the projectile if it's off the screen
                    if projectile.is_off_screen():
                        boss.projectiles.remove(projectile)
            else:
                previous_attack = attack
                boss.projectiles = []
                attack = 3
                start_time = millis()
    

                
    if attack == 3:
        if delay_before_attack(attack, start_time, 3000):
            if millis() - start_time <= 18000:
                if frameCount % 60 == 0:  # Every 1 second
                    boss.floor_attack()
                for projectile in boss.projectiles:
                    projectile.update()
                    projectile.display()
        
                    # Check for collisions with the otter
                    if is_colliding(otter.get_hitbox(), projectile.get_hitbox()):
                        print("Otter collided with a projectile!")
                        frameRate(10)
                        lives -= 1
                        sound_effects[0].trigger()
                        if lives > 1:
                            respawn_time = millis()
                            game_state = "life lost"
                        else:
                            game_state = "game over"
                       
                        
        
                    # Remove the projectile if it's off the screen
                    if projectile.is_off_screen():
                        boss.projectiles.remove(projectile)
            else:
                previous_attack = attack
                start_time = millis()
                attack = 0
                
    

    if attack == 0: 
        boss.display_health_bar()
        if millis() - start_time <= 8000:  # Lasts for 8 seconds
            if delay_before_attack(attack, start_time, 3000):  # 3-second delay before otter's attack
                for projectile in otter.projectiles:
                    # Check for collisions with the boss
                    if is_colliding(boss.get_hitbox(), projectile.get_hitbox()):
                        frameRate(10)
                        print("Boss collided with a projectile!")
                        boss.health -= dmg  # Decrease the boss's health
                        if boss.health <= 0:
                            sound_effects[1].trigger()
                            game_state = "win"
                            break
                        print(boss.health)
                        boss.display_health_bar()
                        otter.projectiles.remove(projectile)
                    # Remove the projectile if it's off the screen
                    if projectile.is_off_screen():
                        otter.projectiles.remove(projectile)
        else:
            previous_attack = attack
            boss.projectiles = []
            attack = 1
            start_time = millis()  # Reset start_time when attack changes to 1
            if not asteroids:
                generate_asteroids()
         
        
    if otter.position.x >= 1065:
        otter.position.x = 1065
    if otter.position.x <= 0:
        otter.position.x = 0
    
    
    draw_buffs()
    buff_effect()

def generate_asteroids():
    global asteroids, warning_time
    frameRate(60)
    for i in range(25):
        asteroid_obj = Asteroid((random.randint(0, 970)), (-11150 + (400*(i+1))), (asteroid_img))
        asteroid_obj.speed = 13
        asteroids.append(asteroid_obj)


def asteroid_hit():
    global game_state, lives, respawn_time
    for asteroid in asteroids:
        if is_colliding(otter.get_hitbox(), asteroid.get_hitbox()):
            print("Otter collided with an asteroid!")
            frameRate(10)
            lives -= 1
            sound_effects[0].trigger()
            if lives > 1:
                respawn_time = millis()
                game_state = "life lost"
            else:
                game_state = "game over"
                       

def delay_before_attack(attack, start_time, delay=5000):

    if millis() - start_time >= delay:
        return True
    else:
        # Display an image depending on the attack
        if attack == 1:
            image(warning1, width/2-warning1.width/2, 0) 
        elif attack == 2:
            image(warning2, width/2-warning2.width/2, 0) 
        elif attack == 3:
            image(warning3, width/2-warning3.width/2, 0) 
        elif attack == 0:
            image(warning4, width/2-warning4.width/2, 0)
        return False

def reset_round_phase_4():
    global asteroids, attack_2_time, start_time
    asteroids = []
    generate_asteroids()
    boss.projectiles = []
    start_time = millis()
    
def draw_buffs():
    global buffs
    if buffs["double_jump"] == True:
        image(jump, 1120, 80)
    if buffs["speed_boost"] == True:
        image(speed, 1120, 160)
    if buffs["damage buff"] == True:
        image(dmg_img, 1120, 20)
        
def buff_effect():
    global buffs, dmg
    if buffs["double_jump"] == True:
        otter.double_jump = True
    if buffs["speed_boost"] == True:
        otter.speed = 15
    if buffs["damage buff"] == True:
        dmg = 2
#################################################################################### LIVES / RESTART ##########################################################################################

def life_lost():
    global game_state, respawn_time, is_jumping, previous_phase, stage_2_counter, sound_effects
    frameRate(10) # needs time to process
    background(0)
    textSize(32)
    
    time_remaining = 3 - int((millis() - respawn_time)/1000)
    if millis() - respawn_time < 3000:  # If 3 seconds have not passed
        if lives == 2:
            image(lives_2, 230, 130)
        elif lives == 1:
            image(lives_1, 230, 130)
        text("Life lost! Respawning in {} seconds...".format(time_remaining), 330, 580)
        text("{} Lives Remaining!".format(lives), 450,300)
        
    else:
        if lives > 0:
            if previous_phase[0] == "phase 1":
                reset_round_phase_1()
                otter.position = PVector(500, 560)
            elif previous_phase[0] == "phase 2":
                reset_round_phase_2()
                otter.position = PVector(0, height/2)
            elif previous_phase[0] == "phase 3":
                frameRate(10)
                otter.velocity = PVector(0, 0)
                otter.position = PVector(width/2, height-120)
                reset_round_phase_3()
            elif previous_phase[0] == "phase 4":
                reset_round_phase_4()
            game_state = previous_phase[0] # Or whatever phase the otter should respawn at
        else:
            game_state = "game_over"
        
    
def game_over():
    global game_state, lives, change_state, previous_phase, reound_start, wolves, platforms_2, wolves_defeated, asteroids, start_time, attack, buffs
    textSize(32)
    background(0)
    text("Press 'r' to restart", 500, 200) 
    image(gg, 230, 130)
    if key == "r":
        if previous_phase[0] == "phase 1":
            otter.position = PVector(500, 560)
            if otter.position.y <= 600:
                otter.velocity.y = 0
            change_state = False
            game_state = "pre 0"
            lives = 3
        elif previous_phase[0]== "phase 2":
            otter.velocity.y = 0
            change_state = False
            game_state = "pre 2"
            lives = 3
        elif previous_phase[0] == "phase 3":
            reset_round_phase_3()
            buffs["double_jump"] = None
            buffs["speed_buff"] = None
            buffs["damage buff"] = None
            wolves = []
            platforms = []
            active_buffs = []
            otter.velocity.y = 0
            change_state = False
            game_state = "pre 3" 
            lives = 3   
            wolves_defeated = 0    
            round_start = millis()
        elif previous_phase[0] == "phase 4":
            boss.health = 10
            asteroids = []
            if not asteroids:
                generate_asteroids()
        
            lives = 3
            game_state = "pre 4"
            attack = 1
            change_state = False
            boss.projectiles = []
 
########################################### MOVEMENT HANDLING ######################################################
def movement(pressed):
    if len(pressed) == 1:
            
        if pressed[0] == "a":
            otter.move(-5, 0)


        if pressed[0] == "d":
            otter.move(5, 0)        


def keyPressed():
    global held_keys, is_jumping, move_platform,game_state, stage_2_counter, attack
    if key == 'w':
        if "w" not in held_keys:
            held_keys.append("w")

    elif key == 'a':
        if "a" not in held_keys:
            held_keys.append("a")

    elif key == 's':
        if "s" not in held_keys:
            held_keys.append("s")

    elif key == 'd':
        if "d" not in held_keys:
            held_keys.append("d")
    elif key == " ":
        is_jumping = True
        move_platform = True
        otter.jump()
        
    elif key == "f" and (game_state == "phase 3" or (game_state == "phase 4" and attack == 0)):
        otter.shoot()
        sound_effects[4].trigger()
        
    if game_state == "phase 2":
        if key == 'w':
            otter.move(0, -5)
        elif key == 's':
            otter.move(0, 5)
    if game_state == "phase 3":
        if key == 's':
            otter.fast_fall()



def keyReleased():
    global held_keys
    if key == 'w':
        held_keys.remove("w")
    if key == 'a':
        held_keys.remove("a")
    if key == 's':
        held_keys.remove("s")
    if key == 'd':
        held_keys.remove("d")
    if key == " ":
        is_jumping = False
        move_platform = True
    otter.stop()
    
def mouseClicked():
    global game_state, change_state
    if game_state == "pre 0":
        
        game_state = "pre 1"
    elif game_state == "pre 1":
        change_state = True
        game_state = "phase 1"
        change_state = False
    elif game_state == "pre 2":
        change_state = True
        game_state = "phase 2"
        change_state = False
    elif game_state == "pre 3":
        change_state = True
        game_state = "phase 3"
        change_state = False
    elif game_state == "pre 4":
        change_state = True
        game_state = "phase 4"
    print("Mouse clicked at: ", mouseX, mouseY)
    

    
    
################################################ COLLISION MANAGER ######################################################33

def is_colliding(rect1, rect2):
    # Check if rect1 is to the right of rect2 or rect2 is to the right of rect1
    if rect1[0] >= rect2[2] or rect2[0] >= rect1[2]:
        return False

    # Check if rect1 is below rect2 or rect2 is below rect1
    if rect1[1] >= rect2[3] or rect2[1] >= rect1[3]:
        return False

    # If neither of the above conditions is true, the rectangles are colliding
    return True


def collide():
    global game_state, lives, respawn_time
    if game_state == "phase 1":
        for platform in platforms:
            # Get the hitbox of the platform
            platform_hitbox = [platform[0], platform[1], platform[0] + tile_width, platform[1] + tile_height]
            if is_colliding(otter.get_hitbox(), platform_hitbox):
                # Check if the otter's feet are above the platform and the otter is moving downwards
                otter_bottom = otter.position.y + 160  # 85 is the height of the otter
                if otter_bottom <= platform[1] and otter.velocity.y > 0:  # platform[1] is the y-coordinate of the platform
                    otter.jumping = False
                    # Reset the otter's vertical velocity
                    otter.velocity.y = 0
                    # Adjust the otter's y position to be on top of the platform
                    otter.position.y = platform[1] - 160.6
                    

        
        
        for eagle in eagles:
            # Get the hitbox of the eagle
            eagle_hitbox = [eagle.x - 20, eagle.y, eagle.x + eagle.hitbox[0], eagle.y + eagle.hitbox[1]]
            if is_colliding(otter.get_hitbox(), eagle_hitbox):
            
                lives -= 1
                sound_effects[0].trigger()
                if lives > 0:
                    game_state = "life lost"
                    otter.velocity.y = 0
                    respawn_time = millis()  # Record the current time
                else:
                    game_state = "game over"
                    
        if otter.position.y > 639.5:
            lives -= 1
            sound_effects[0].trigger()
            otter.velocity.y = 0
            if lives > 0:
                game_state = "life lost"
                respawn_time = millis()  # Record the current time
            else:
                game_state = "game over"
