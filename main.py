import pygame, random
pygame.init()
#initialise variables
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
bombdropping = False
listt = []
clock = pygame.time.Clock()
plane = pygame.Rect(x,y,width,height)
sprite = pygame.image.load("images/plane.png")
building = pygame.Rect(50,300,50,300)
bomb = pygame.Rect(x,y,width/2,height/2)
fontyes =  pygame.font.SysFont("None",30)
gameovertext = fontyes.render("Game Over",True,(0,0,0))
wintext = fontyes.render(("WIN"),True,(0,0,0))
#create buildings in list
for i in range(8):
  listt.append(pygame.Rect(building.x*i,random.randrange(150,375),building.width,building.height))
def gameover():
  global run
  while run:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
    screen.fill((177, 226, 252))
    #put text in the middle of the display
    screen.blit(gameovertext,(screenwidth/2 -gameovertext.get_rect().width/2,screenheight/2-gameovertext.get_rect().height/2))
    pygame.display.update()
while run:
  #stop game if x button pressed
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  keys = pygame.key.get_pressed()
  if keys[pygame.K_SPACE] and not bombdropping:
    bombdropping = True
    #places bomb under the middle of the plane
    bomb = pygame.Rect(plane.centerx-(width/2/2),plane.centery+(height/2),25,25)
  plane.left += vel
  if plane.left >= screenwidth:
    plane.left = -50
    plane.y += 25
  if bombdropping:
    bomb.y += 5
    for v in listt:
      if v.colliderect(bomb):
        bombdropping = False
        listt.remove(v)
        score+=100
        bomb = pygame.Rect(screenwidth,screenheight,25,25)
  #sky blue colour
  screen.fill((177, 226, 252))
  if bomb.y > 400:
    bombdropping = False
  if not bombdropping:
    #move bomb offscreen
    bomb = pygame.Rect(500,500,25,25)
  if plane.collidelist(listt) != -1:
    gameover()
  if score == 800:
    screen.blit(wintext,(screenwidth/2 -wintext.get_rect().width/2,screenheight/2-wintext.get_rect().height/2))
  #antialiased text
  scorefont = fontyes.render(("SCORE: "+str(score)),True,(0,0,0))
  screen.blit(scorefont,(0,0))
  screen.blit(sprite,(plane.x,plane.y))
  pygame.draw.ellipse(screen,"grey",bomb)
  for v in listt:
    pygame.draw.rect(screen,"black",v)
  pygame.display.update()
  clock.tick(30)