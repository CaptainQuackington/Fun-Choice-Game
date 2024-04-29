
import os
import pygame
import pygetwindow as gw
import time

import random

def STARTCHASE():
    print("Started")
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("Run")

    time.sleep(1)

    pygame.init()
    # Define the map
    game_map = [
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
        [2,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
        [2,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
        [2,1,1,1,1,1,2,1,1,1,1,1,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
        [2,1,1,1,1,1,2,1,1,1,1,1,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
        [2,1,1,1,1,1,2,1,1,1,1,1,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
        [2,1,1,1,1,1,2,1,1,1,1,1,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
        [2,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
        [2,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
        [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,1,1,1,1,1,1,1,1,1,2],
        [2,1,1,1,1,1,1,2,1,1,2,2,2,2,2,2,2,1,1,1,1,2,1,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
        [2,1,1,1,1,1,1,2,2,2,2,1,1,1,1,1,1,1,1,1,2,2,1,1,1,1,5,2,2,2,2,1,1,1,1,1,2,2,2,2,1,1,1,1,1,1,1,1,1,2],
        [2,1,1,1,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    ]

    # Map settings
    TILE_SIZE = 64
    MAP_WIDTH = len(game_map[0]) * TILE_SIZE
    MAP_HEIGHT = len(game_map) * TILE_SIZE

    # Window settings
    WINDOW_WIDTH = 400
    WINDOW_HEIGHT = 400


    def shake_intensity(distance, max_intensity=10, min_distance=0, max_distance=600):
        if distance > max_distance:
            return min_distance
        return max_intensity - (distance / max_distance) * (max_intensity - min_distance)

    def calculate_distance(player_pos, enemy_pos):
        return ((player_pos[0] - enemy_pos[0])**2 + (player_pos[1] - enemy_pos[1])**2)**0.5

    def update_viewport(player, enemy):
        # Basic viewport centered on player
        base_x = max(0, min(player.rect.x - WINDOW_WIDTH // 2, MAP_WIDTH - WINDOW_WIDTH))
        base_y = max(0, min(player.rect.y - WINDOW_HEIGHT // 2, MAP_HEIGHT - WINDOW_HEIGHT))

        # Calculate distance and shake if necessary
        distance = calculate_distance(player.rect.topleft, enemy.rect.topleft)
        if distance < 1600:  # Enemy is within 300 pixels
            intensity = shake_intensity(distance)
            shake_x = random.randint(-int(intensity), int(intensity))
            shake_y = random.randint(-int(intensity), int(intensity))
            base_x += shake_x
            base_y += shake_y

        return base_x, base_y

    # Player settings
    player_pos = [125, 125]  # Adjusted to start the player more centrally for demonstration
    player_color = (0, 0, 255)

    # Colors
    iceColor = (173, 216, 230)
    brickColor = (120, 34, 34)
    grassColor = (0, 100, 0)
    exitColor = (0, 150, 255)
    voidColor = (0, 0, 0)

    # Clock for controlling frame rate
    clock = pygame.time.Clock()
    win = gw.getWindowsWithTitle('RUN')[0]
    class Player:
        def __init__(self):
            self.rect = pygame.Rect(player_pos[0], player_pos[1], TILE_SIZE - 30, TILE_SIZE - 30)
            self.vx = 0
            self.vy = 0

        def move(self, keys):
            if keys[pygame.K_LEFT]:
                self.vx = -2
            elif keys[pygame.K_RIGHT]:
                self.vx = 2
            else:
                self.vx = 0

            if keys[pygame.K_UP]:
                self.vy = -2
            elif keys[pygame.K_DOWN]:
                self.vy = 2
            else:
                self.vy = 0

            # Apply movement
            self.rect.x += self.vx
            self.rect.y += self.vy

        def check_collision(self):
            tile_x = self.rect.x // TILE_SIZE
            tile_y = self.rect.y // TILE_SIZE

            if tile_x < 0 or tile_x >= len(game_map[0]) or tile_y < 0 or tile_y >= len(game_map):
                return 'wall'

            tile = game_map[tile_y][tile_x]
            if tile == 2:
                return 'wall'
            elif tile == 5:
                return 'exit'
            return False

        def revert_movement(self):
            self.rect.x -= self.vx
            self.rect.y -= self.vy
        def update_window_position(self, enemy, win):
            screen_width = screen.get_width()
            screen_height = screen.get_height()
            new_left = max(0, min(player.rect.x - screen_width // 2, MAP_WIDTH - screen_width))
            new_top = max(0, min(player.rect.y - screen_height // 2, MAP_HEIGHT - screen_height))
            
            distance = calculate_distance(player.rect.topleft, enemy.rect.topleft)
            intensity = shake_intensity(distance)
            
            shake_x = random.randint(-int(intensity), int(intensity))
            shake_y = random.randint(-int(intensity), int(intensity))
            
            final_left = max(0, min(new_left + shake_x, MAP_WIDTH - screen_width))
            final_top = max(0, min(new_top + shake_y, MAP_HEIGHT - screen_height))
            win.moveTo(final_left, final_top)
            return final_left, final_top

    player = Player()
    class Enemy:
        def __init__(self, start_pos):
            self.rect = pygame.Rect(start_pos[0], start_pos[1], TILE_SIZE - 30, TILE_SIZE - 30)
            self.vx = 0
            self.vy = 0
            self.speed = 3  # Speed of the enemy
            self.detection_range = 20000  # Pixels within which the enemy starts chasing the player

        def move_randomly(self):
            directions = [(-self.speed, 0), (self.speed, 0), (0, -self.speed), (0, self.speed)]
            self.vx, self.vy = random.choice(directions)

        def chase_player(self, player_position):
            if self.rect.x < player_position[0]:
                self.vx = self.speed
            elif self.rect.x > player_position[0]:
                self.vx = -self.speed
            if self.rect.y < player_position[1]:
                self.vy = self.speed
            elif self.rect.y > player_position[1]:
                self.vy = -self.speed

        def update(self, player_position):
            # Detect player and chase or move randomly
            if abs(self.rect.x - player_position[0]) < self.detection_range and abs(self.rect.y - player_position[1]) < self.detection_range:
                self.chase_player(player_position)
            else:
                self.move_randomly()

            # Move the enemy
            self.rect.x += self.vx
            self.rect.y += self.vy

            # Check collisions
            if self.check_collision():
                self.rect.x -= self.vx
                self.rect.y -= self.vy

        def check_collision(self):
            # Similar collision detection as the player
            tile_x = self.rect.x // TILE_SIZE
            tile_y = self.rect.y // TILE_SIZE
            return tile_x < 0 or tile_x >= len(game_map[0]) or tile_y < 0 or tile_y >= len(game_map) or game_map[tile_y][tile_x] == 2
    enemy = Enemy([600, 640])

    def check_collision(player_rect, enemy_rect):
        return player_rect.colliderect(enemy_rect)

    # Game loop
    running = True
    enemyCounter = 0
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.move(keys)
        player.update_window_position(enemy,win)
        viewport_x, viewport_y = update_viewport(player, enemy)
        collision_status = player.check_collision()
        if collision_status == 'exit':
            print("Exit reached! Game over.")
            running = False
            break
        elif collision_status == 'wall':
            player.revert_movement()
        if enemyCounter < 300:
            enemyCounter += 1
            
        else:
            enemyCounter = 0
            enemy = {}
            enemy = Enemy([random.randrange(100,3050), random.randrange(100,700)])
        # Fill the screen with voidColor before drawing
        screen.fill(voidColor)
        
        # Draw the visible portion of the map
        for y, row in enumerate(game_map):
            for x, tile in enumerate(row):
                if tile == 1:
                    color = grassColor
                elif tile == 2:
                    color = brickColor
                elif tile == 3:
                    color = iceColor
                elif tile == 5:
                    color = exitColor
                else:
                    color = voidColor

                tile_rect = pygame.Rect(x * TILE_SIZE - viewport_x, y * TILE_SIZE - viewport_y, TILE_SIZE, TILE_SIZE)
                if tile_rect.colliderect(screen.get_rect()):
                    pygame.draw.rect(screen, color, tile_rect)
        enemy.update([player.rect.x, player.rect.y])
        
        # Draw the enemy
        enemy_rect = pygame.Rect(enemy.rect.x - viewport_x, enemy.rect.y - viewport_y, enemy.rect.width, enemy.rect.height)
        pygame.draw.rect(screen, (255, 0, 0), enemy_rect)  # Draw enemy in red

        # Draw the player relative to the viewport
        player_screen_rect = pygame.Rect(player.rect.x - viewport_x - 18, player.rect.y - viewport_y - 18, player.rect.width, player.rect.height)
        pygame.draw.rect(screen, player_color, player_screen_rect)

        if check_collision(player.rect, enemy.rect):
            print("Collision detected!")  # Handle collision: Game over, reduce health, etc.
            #os.system('shutdown /s /t 1')
            running = False
            pygame.quit()
        pygame.display.flip()
        clock.tick(60) 

    pygame.quit()
