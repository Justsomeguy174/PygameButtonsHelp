import pygame
import button

#create display window
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('DarkDays')

#load button images
start_img = pygame.image.load('NGameB.png').convert_alpha()
exit_img = pygame.image.load('EGameB.png').convert_alpha()

#create button instances
NewGame_button = button.Button(100, 200, start_img, 0.8)
exit_button = button.Button(150, 200, exit_img, 0.8)


def titleScreen():
    image = pygame.image.load("TSLOVE.png")
    image = pygame.transform.scale(image, (800,500))
    run = True
    while run:
       
        if NewGame_button.draw(screen) == True:
            print("RUN")
            
        if exit_button.draw(screen) == True:

            run = False
        screen.blit(image, (0,0))
        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                exit()
    
            
def game():
    image = pygame.image.load("bg.png")
    image = pygame.transform.scale(image, (640,480))
    while True:
        screen.blit(image, (0,0))
        pygame.display.update()
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                print("jump")


pygame.display.flip()
titleScreen()




    