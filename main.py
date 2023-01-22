import pygame
import random
import sys


pygame.init()
screen = pygame.display.set_mode((500, 500))
name_of_game = pygame.display.set_caption('Dodge the Bomb!')
clock = pygame.time.Clock()
font_type = pygame.font.Font("fonts/ARCADECLASSIC.TTF", 50)

score = 0
bomb_speed = 1

map_surface = pygame.image.load("graphics/fixed_map.png").convert()

player_image_surface = pygame.image.load("graphics/character/character_new.png")
player_rect = player_image_surface.get_rect(center=(230, 340))
player_x_pos = 230
bomb_image_surface = pygame.image.load("graphics/small_bomb1.png")
bomb_rect = bomb_image_surface.get_rect(bottomleft=(30, 30))

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	keys = pygame.key.get_pressed()

	if keys[pygame.K_RIGHT]:
		player_image_surface = pygame.image.load("graphics/character/character_right.png")
		player_rect.x += 2

	if keys[pygame.K_LEFT]:
		player_image_surface = pygame.image.load("graphics/character/character_new.png")
		player_rect.x -= 2

	if player_rect.x < -15:
		player_rect.x = 500

	if player_rect.x > 500:
		player_rect.x = 0

	bomb_rect.y += bomb_speed

	if bomb_rect.y == 500:
		score = score + 1
		bomb_rect.y = 30
		bomb_rect.x = random.randint(50, 400)

	if score >= 5:
		bomb_speed += 2

	if score == 0:
		bomb_speed = 1

	text_surface = font_type.render(str(score), False, "White")
	if player_rect.colliderect(bomb_rect) == 1:
		score = 0

	screen.blit(map_surface, (0, 0))
	screen.blit(text_surface, (230, 0))
	screen.blit(player_image_surface, player_rect)
	screen.blit(bomb_image_surface, bomb_rect)

	pygame.display.update()
	clock.tick(60)