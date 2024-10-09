import pygame , time

pygame.init()

screenWidth = 1200

screenHeight = 800

screen = pygame.display.set_mode((screenWidth, screenHeight))

run = True

prev_time = time.time()

dt = 0

start = False

target_fps = 550

#this is the game loop

player_pos = pygame.Vector2(10, 360)

rect = pygame.Rect(player_pos, (15 , 100))

while run:

  screen.fill((0, 0, 0))
  
  key = pygame.key.get_pressed()
  
  #in this if is the game after the start screen
  
  while start:
    now = time.time()

    dt = prev_time * -1 - now * -1

    prev_time = now

    key2 = pygame.key.get_pressed()
    
    screen.fill((0, 0, 0))
    
    pygame.draw.rect(screen, (0, 80, 255), rect)

    if key2[pygame.K_w]:

      player_pos.y -= 1 * dt * target_fps
      
    if key2[pygame.K_s]:

      player_pos.y += 1 * dt * target_fps
    
    if player_pos.y <= 0:
     
     player_pos.y = 0 
    
    if player_pos.y >= screenHeight - rect.height:

      player_pos.y = screenHeight - rect.height
      
    rect.topleft = player_pos

    for event in pygame.event.get():
    
      if event.type == pygame.QUIT:
        
        start = False
        
        run = False
        
      if key2[pygame.K_SPACE]:
      
        start = False
        
    pygame.display.update()
    
  #this is the event handler
  
  for event in pygame.event.get():
    
    if key[pygame.K_BACKSPACE]:
      
      start = True
    
    if event.type == pygame.QUIT:
    
      run = False
    
  pygame.display.update()
  
pygame.quit()      