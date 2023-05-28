import pygame

# Initialize Pygame
pygame.init()

# Set screen dimensions
largeur = 1262
hauteur = 686
screen = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Mario")

#Niveau


Start= True
gameover= False
Levels= False
running= False
Level1= False
Level2= False
Level3= False

#Image Debut Game
StartS= pygame.image.load("startscreen.png").convert_alpha()
map = pygame.image.load("map.png").convert()
marioS= pygame.image.load("mariostand.png").convert_alpha()
level1= pygame.image.load("level1.png").convert_alpha()
level2= pygame.image.load("level2.png").convert_alpha()
level3= pygame.image.load("level3.png").convert_alpha()
lock= pygame.image.load("levellock.png").convert_alpha()
start= pygame.image.load("start.png").convert_alpha()

#Mario et Variables au Debut
mario_x = 0
mario_y = 0
point1= [160,250]
point2=[350,250]
point3=[600, 250]
point4=[900,250]
points = [point1,point2]
current_point_index = 0
levelAvailable = 4


# Load background image
background = pygame.image.load("bg_mario.png").convert()
sol = pygame.image.load("sol.png").convert_alpha()
solm= pygame.image.load("solm.png").convert_alpha()
marioj = pygame.image.load("marioj.png").convert_alpha()
mario1 = pygame.image.load("mario1.png").convert_alpha()
mario2 = pygame.image.load("mario2.png").convert_alpha()
mario3 = pygame.image.load("mario3.png").convert_alpha()
mario_images = [mario1, mario2, mario3, pygame.transform.flip(mario1, True, False), pygame.transform.flip(mario2, True, False), pygame.transform.flip(mario3, True, False)]
bloc = pygame.image.load("bloc.png").convert_alpha()
coin = pygame.image.load("coin1.png").convert_alpha()

gameover = pygame.image.load("gameover.png").convert_alpha()
heart = pygame.image.load("heartW.png")


# Variables
mario_image = mario1
mario_direction = 0
is_jumping = False
GRAVITY = 0.1
JUMP_POWER = 6
HITBOX_WIDTH = 40
HITBOX_HEIGHT = 40
nheart = 3

# Coordinates
mario_x = 95
mario_y = 572
mario_x_speed = 0
mario_y_speed = 0
heart_x = 20
heart_y = 20

# Create Rect objects
sol_rect = sol.get_rect()
sol_rect.x = 0
sol_rect.y = 627
solm_rect= solm.get_rect()
solm_rect.x= 818
solm_rect.y=627
mario_rect = mario_image.get_rect()
bloc_rect = bloc.get_rect()
bloc_rect.y = 500
coin_rect= coin.get_rect()
 # Assuming ncoin is the number of coins

collisions = [sol_rect, bloc_rect]
collected_coins = [] 



def draw_blocks(screen, bloc, x, y, nbloc):
    global mario_x, mario_y, mario_x_speed, mario_y_speed, is_jumping

    for i in range(nbloc):
        bloc_rect = bloc.get_rect(topleft=(x + i * bloc.get_width(), y))
        screen.blit(bloc, bloc_rect)

        if mario_rect.colliderect(bloc_rect):
           
            
            
                
            # Check for collision with top of block
            if mario_rect.top <= bloc_rect.bottom:
                mario_y_speed = 0
                is_jumping = True
                mario_y_speed = GRAVITY 
            
            
            if mario_x_speed > 0 and mario_rect.right <= bloc_rect.left + mario_x_speed:
                mario_x_speed = 0
                mario_x = bloc_rect.left - mario_rect.width
                mario_y_speed = GRAVITY  # Apply gravity to make Mario fall down
                is_jumping = True
                

            # Check for collision with left side of block
            elif mario_x_speed < 0 and mario_rect.left >= bloc_rect.right + mario_x_speed:
                mario_x_speed = 0
                mario_x = bloc_rect.right
                mario_y_speed = GRAVITY  # Apply gravity to make Mario fall down
                is_jumping = True
            else :
                
                mario_y_speed = -GRAVITY
                is_jumping = False
                mario_image = mario1
                
                
def draw_coins(screen, coin, x, y, ncoin, spacing):
    global mario_rect, collected_coins

    coins_to_draw = []  # Create a new list to store the coins that need to be drawn

    for i in range(ncoin):
        coin_x = x - ((ncoin - 1) * spacing / 2) + (i * spacing)  # Calculate the X position of each coin
        coin_rect = coin.get_rect(topleft=(coin_x, y))

        if coin_rect.colliderect(mario_rect):
            # If Mario touches the coin, remove it from the list of coins to be drawn
            collected_coins.append(i)

        if i not in collected_coins:
            # If the coin has not been collected, add it to the list of coins to be drawn
            coins_to_draw.append((coin, coin_rect))

    # Draw the remaining coins
    for coin_image, coin_rect in coins_to_draw:
        screen.blit(coin_image, coin_rect)


        


    
while Start:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN  :
                Start= False
                Levels= True
    screen.blit(StartS, (0,0))
    pygame.display.flip()



while Levels:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if mario_x == point2[0] and event.key == pygame.K_RETURN  :
                Levels = False
                running= True
                Level1 = True
            elif mario_x == point3[0] and event.key == pygame.K_RETURN  :
                Levels = False
                running= True
                Level2 = True
            elif mario_x == point4[0] and event.key == pygame.K_RETURN  :
                levels = False
                running= True
                Level3 = True
            if event.key == pygame.K_RIGHT:
                if current_point_index < len(points) -1 and levelAvailable > current_point_index + 1:
                    current_point_index += 1
                    
            elif event.key == pygame.K_LEFT:
                if current_point_index > 0:
                    current_point_index -= 1
        


    # Set the new position of Mario based on the current point
    mario_x, mario_y = points[current_point_index]
    screen.blit(map, (0, 0))
    screen.blit(lock, (point3[0] + 2, point3[1] + 20))
    screen.blit(lock, (point4[0] + 2, point4[1] + 20))
    screen.blit(level1, (point2[0] + 2, point2[1] + 20))
    if levelAvailable >= 3:
        points.append(point3)
        screen.blit(level2, (point3[0] + 2, point3[1] + 20))
    if levelAvailable == 4:
        points.append(point4)
        screen.blit(level3, (point4[0] + 2, point4[1] + 20))
    screen.blit(marioS, (mario_x, mario_y))
    # Update the screen
    pygame.display.flip()

mario_x = 95
mario_y = 560


            
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not is_jumping :
                if mario_direction == 0:
                    mario_image = marioj
                else:
                    mario_image = pygame.transform.flip(marioj, False, False)
                mario_y_speed = -JUMP_POWER
                is_jumping = True
               
            if event.key == pygame.K_RIGHT:
                mario_x_speed = 2
                mario_direction = 0
            elif event.key == pygame.K_LEFT:
                mario_x_speed = -2
                mario_direction = 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                mario_x_speed = 0
            elif event.key == pygame.K_LEFT:
                mario_x_speed = 0
            
                

    # Apply Gravity
    mario_y_speed += GRAVITY

    #Update positions
    mario_x += mario_x_speed
    mario_y += mario_y_speed
    mario_rect.x = mario_x
    mario_rect.y = mario_y
    
    #Collisions
        
        #Sol
    if mario_rect.colliderect(sol_rect) or (mario_rect.bottom >= sol_rect.top and mario_rect.bottom <= sol_rect.bottom and mario_rect.right >= 1020):
        mario_y_speed = 0
        mario_y_speed -= GRAVITY
        is_jumping = False
        mario_image = mario1

# Solm
    if mario_rect.colliderect(solm_rect) :
        mario_y_speed = 0
        mario_y_speed -= GRAVITY
        is_jumping = False
        mario_image = mario1
    
        

        
        #Bas du screen
    if mario_y >= hauteur+ 100 - mario_image.get_height():
        mario_x = 95
        mario_y = 560
        mario_x_speed = 0
        mario_y_speed = 0
        is_jumping = False
        mario_image = mario1
        mario_direction = 0
        mario_rect.x = mario_x
        mario_rect.y = mario_y
        nheart -= 1
        
        if nheart ==0:
            screen.blit(gameover, (0, 0))
            pygame.display.flip()
            pygame.time.wait(3000)
            running = False
            Levels= True
   

    
        # les Cotes
    if mario_x < 0:
        mario_x = 0
    if mario_x > largeur - HITBOX_WIDTH:
        mario_x = largeur - HITBOX_WIDTH
    if mario_y < 0:
        mario_y = 0
        
    #Affichage
    screen.blit(background, (0, 0))
    screen.blit(sol, sol_rect)
    
    
    for i in range(nheart):
        screen.blit(heart, (heart_x + i * 40, heart_y))
        
    if not is_jumping and mario_x_speed ==0 and mario_direction==0: screen.blit(mario1, (mario_x, mario_y))
    elif not is_jumping and mario_x_speed ==0 and mario_direction==1 :screen.blit(pygame.transform.flip(mario1, True, False), (mario_x, mario_y))
    elif is_jumping and mario_direction==0: screen.blit(marioj, (mario_x, mario_y))
    elif is_jumping and mario_direction==1: screen.blit(pygame.transform.flip(marioj, True, False), (mario_x, mario_y))
    else: screen.blit(mario_images[mario_direction*3+(mario_x//30)%3], (mario_x, mario_y))
    if not is_jumping: mario_image = mario1

 
    
    if Level1 == True :
        screen.blit(sol, (sol_rect.x + 1020,sol_rect.y))
        screen.blit(solm, (solm_rect))
        
        draw_blocks(screen, bloc, 430, 500, 5)
        draw_coins(screen,coin, 500, 470, 5,30)
        
        draw_blocks(screen, bloc, 0, 360, 1)
        draw_blocks(screen, bloc, 216, 360, 1)
        draw_blocks(screen, bloc, 0, 380, 7)
        draw_coins(screen,coin, 50, 350, 6,30,)
        
        draw_blocks(screen, bloc, 330, 230, 2)
        
        draw_blocks(screen, bloc, 530, 160, 1)
        draw_blocks(screen, bloc, 817, 160, 1)
        draw_blocks(screen, bloc, 530, 180, 9)
        
        by= 627
        for loop in range(6):
            draw_blocks(screen, bloc, 820, by- 30, 1)
            by -= 30
            
        draw_blocks(screen, bloc, 970, 370, 8)
        
        
        pygame.display.flip()
    
    elif Level2 == True :
    
        screen.blit(sol, (sol_rect.x + 1020,sol_rect.y))
        screen.blit(solm, (solm_rect))
        
        draw_blocks(screen, bloc, 430, 500, 5)
        draw_coins(screen,coin, 500, 470, 5,30)
        
        draw_blocks(screen, bloc, 0, 360, 1)
        draw_blocks(screen, bloc, 216, 360, 1)
        draw_blocks(screen, bloc, 0, 380, 7)
        draw_coins(screen,coin, 50, 350, 6,30)
        
        draw_blocks(screen, bloc, 330, 230, 2)
        
        draw_blocks(screen, bloc, 530, 160, 1)
        draw_blocks(screen, bloc, 817, 160, 1)
        draw_blocks(screen, bloc, 530, 180, 9)
        
        by= 627
        for loop in range(6):
            draw_blocks(screen, bloc, 820, by- 30, 1)
            by -= 30
            
        draw_blocks(screen, bloc, 970, 370, 8)
        
        pygame.display.flip()
     
    elif Level3 == True :
    
        draw_blocks(screen, bloc, 460, 500, 3)
        draw_blocks(screen, bloc, 400, 360, 1)
        draw_blocks(screen, bloc, 0, 380, 7)
        pygame.display.flip()
  
    
    if nheart<=0 :
        running= False
        Levels= True
