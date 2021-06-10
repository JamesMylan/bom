import pygame, random
pygame.init()
screenheight = 400
screenwidth = 400
screen = pygame.display.set_mode((screenheight,screenwidth))
x=50
y=50
width=50
height=25
vel=5
run = True
bomdropping = False
listt = []
clock = pygame.time.Clock()
plane = pygame.Rect(x,y,width,height)
sprite = pygame.image.load("awd.png")
building = pygame.Rect(50,300,50,200)
bom = pygame.Rect(x,y,width/2,height/2)
bomacdropping = False
for i in range(8):
  listt.append(pygame.Rect(building.x*i,random.randrange(200,390),building.width,building.height))
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  keys = pygame.key.get_pressed()
  if keys[pygame.K_SPACE] and not bomdropping:
    bomdropping = True
    bomacdropping = True
  plane.left += vel
  if plane.left >= screenwidth:
    plane.left = -50
  if bomdropping:
    bom.y += 5
    for i in range(len(listt)):
      if bomacdropping:
        if listt[i].colliderect(bom):
          bomacdropping = False
          listt.pop(i)
  screen.fill((177, 226, 252))
  for i in range(len(listt)):
    pygame.draw.rect(screen,"black",listt[i])
  if bom.y > 400:
    bomdropping = False
    bomacdropping = False
  if not bomdropping:
    bom = pygame.Rect(plane.centerx-(width/2/2),plane.centery+(height/2),25,25)
  screen.blit(sprite,(plane.x,plane.y))
  pygame.draw.ellipse(screen,"grey",bom)
  pygame.display.update()
  clock.tick(30)