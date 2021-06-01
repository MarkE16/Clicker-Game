import pygame
import pygame.freetype
from stuff import icon_location, coin_location

pygame.init()
displayx = 500
displayy = 500
points = 0
main = True
display = pygame.display.set_mode([displayx, displayy])
icon = pygame.image.load(icon_location)
coin = pygame.image.load(coin_location)
pygame.display.set_caption("Clicker Game | In development")
pygame.display.set_icon(icon)
coincollison = coin.get_rect()
text = pygame.freetype.SysFont(pygame.freetype.get_default_font(), 12)

def stats(score):
  text.render_to(display, (10, 470), f"Points: {score}", (0, 0, 0), None, size=20)

while main:
  pos = pygame.mouse.get_pos()
  display.fill((255, 255, 255))
  c = display.blit(coin, (230, 200))
  mousepressed = pygame.mouse.get_pressed()
  #
  #
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      main = False
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
      if c.collidepoint(pos):
        points += 1
  
  stats(points)
  pygame.display.update()