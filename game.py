import pygame

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Mario Game")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Load Mario image
mario = pygame.image.load("mario.png")  # Add a Mario sprite in the same directory
mario = pygame.transform.scale(mario, (50, 50))

# Player properties
player_x = 50
player_y = 300
player_width = 50
player_height = 50
velocity = 5
jumping = False
jump_count = 10

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(30)  # FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement controls
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= velocity
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += velocity
    if not jumping:
        if keys[pygame.K_SPACE]:
            jumping = True
    else:
        if jump_count >= -10:
            neg = 1 if jump_count > 0 else -1
            player_y -= (jump_count ** 2) * 0.3 * neg
            jump_count -= 1
        else:
            jump_count = 10
            jumping = False

    # Draw everything
    screen.fill(WHITE)
    screen.blit(mario, (player_x, player_y))
    pygame.draw.rect(screen, BLUE, (0, 350, WIDTH, 50))  # Ground

    pygame.display.update()

pygame.quit()
