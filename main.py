import pygame
from stuff import icon_location

pygame.init()
displayx = 500
displayy = 500
main = True
# Replace "RESIZABLE" with "FULLSCREEN" to make the window fullscreen.
display = pygame.display.set_mode([displayx, displayy], pygame.RESIZABLE)
icon = pygame.image.load(icon_location)
pygame.display.set_caption("Clicker Game")
pygame.display.set_icon(icon)

while main:
  display.fill((255, 255, 255))
  #
  #
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      main = False
    # If the pygame window is set to resizeable, then this will make the window not bug out when the window is being resized.
    if event.type == pygame.VIDEORESIZE:
      display = pygame.display.set_mode([event.w, event.h], pygame.RESIZABLE)
  
  pygame.display.update()