import pygame
import pygame.freetype
import pygame_gui
from stuff import icon_location, coin_location

pygame.init()

# ---[ Variables ]---
clicktotal = 1
cost1 = 50
clock = pygame.time.Clock()
displayx = 500
displayy = 500
points = 0
main = True
window = pygame.display.set_mode([displayx, displayy])
icon = pygame.image.load(icon_location)
coinimg = pygame.image.load(coin_location)
coincollision = coinimg.get_rect()
text = pygame.freetype.SysFont(pygame.freetype.get_default_font(), 12)
manager = pygame_gui.UIManager([displayx, displayy])
purchase_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 100), (100, 20)), text="Purchase", manager=manager)

# ---[ Functions ]---
def stats(score):
  text.render_to(window, (10, 470), f"Points: {score}", (0, 0, 0), None, size=20)

# Changes the icon and window caption.
pygame.display.set_caption("Clicker Game | In development")
pygame.display.set_icon(icon)

while main:

  time_delta = clock.tick(60) / 1000
  pos = pygame.mouse.get_pos()
  window.fill((255, 255, 255))
  c = window.blit(coinimg, (230, 200))
  pygame.draw.rect(window, (0, 0, 0), (8, 490, 485, 3))
  pygame.draw.rect(window, (0, 0, 0), (8, 5, 485, 3))
  text.render_to(window, (10, 80), f"Cost: {cost1}", (0, 0, 0), None, size=15)

  #
  #
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      main = False

    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
      if c.collidepoint(pos):
        points += clicktotal

    if event.type == pygame.USEREVENT:
      if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
        if event.ui_element == purchase_button:
          if points < cost1:
            print("Insufficient points to make purchase.")
          else:
            points -= cost1
            clicktotal = clicktotal * 2
            cost1 = cost1 * clicktotal
            print("Purchase made.")
    manager.process_events(event)
  
  manager.update(time_delta)
  manager.draw_ui(window)
  stats(points)
  pygame.display.update()