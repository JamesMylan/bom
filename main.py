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
score=0
run = True
bomdropping = False
listt = []
index = 1
clock = pygame.time.Clock()
plane = pygame.Rect(x,y,width,height)
sprite = pygame.image.load("images/plane.png")
building = pygame.Rect(50,300,50,200)
bom = pygame.Rect(x,y,width/2,height/2)
bomacdropping = False
fontyes =  pygame.font.SysFont("None",30)
textsurface = fontyes.render("Game Over",True,(0,0,0))
framelist = [pygame.image.load("images/explosion/output001.png"),pygame.image.load("images/explosion/output002.png"),pygame.image.load("images/explosion/output003.png"),pygame.image.load("images/explosion/output004.png"),pygame.image.load("images/explosion/output005.png"),pygame.image.load("images/explosion/output006.png")]
for i in range(8):
  listt.append(pygame.Rect(building.x*i,random.randrange(200,390),building.width,building.height))
def gameover():
  global run
  while run:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
    screen.fill((177, 226, 252))
    screen.blit(textsurface,(screenwidth/2 -textsurface.get_rect().width/2,screenheight/2-textsurface.get_rect().height/2))
    pygame.display.update()
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  keys = pygame.key.get_pressed()
  if keys[pygame.K_SPACE] and not bomdropping:
    bomdropping = True
    bomacdropping = True
    bom = pygame.Rect(plane.centerx-(width/2/2),plane.centery+(height/2),25,25)
  plane.left += vel
  if plane.left >= screenwidth:
    plane.left = -50
    plane.y += 25
  if bomdropping:
    bom.y += 5
    for i in range(len(listt)):
      if bomacdropping:
        if listt[i].colliderect(bom):
          bomacdropping = False
          bombdropping = False
          listt.pop(i)
          score+=100
          bom = pygame.Rect(500,500,25,25)
  screen.fill((177, 226, 252))
  if bom.y > 400:
    bomdropping = False
    bomacdropping = False
  if not bomdropping:
    bom = pygame.Rect(500,500,25,25)
  if plane.collidelist(listt) != -1:
    gameover()
  index += 1
  if index >= 6:
    index = 1
  scorefont = fontyes.render(("SCORE: "+str(score)),True,(0,0,0))
  screen.blit(scorefont,(0,0))
  screen.blit(sprite,(plane.x,plane.y))
  pygame.draw.ellipse(screen,"grey",bom)
  for i in range(len(listt)):
    pygame.draw.rect(screen,"black",listt[i])
  pygame.display.update()
  clock.tick(30)