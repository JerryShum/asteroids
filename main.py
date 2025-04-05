import pygame
from constants import *
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    
    # Creating groups to add objects to (player, asteroids, etc.)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    # Adding all player objects to the updatable and drawable groups
    Player.containers = (updatable, drawable)
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(x = SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    dt = 0
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Updating all objects in the updatable group
        updatable.update(dt)
            
        screen.fill("black")
        
        # Drawing all objects in the drawable group
        for obj in drawable:
            obj.draw(screen)
           
           
        pygame.display.flip()
            
        
        # FPS = 60
        dt = clock.tick(60) / 1000
        
        
        
        
    
    
    
    
    
    
    
if __name__ == "__main__":
    main()