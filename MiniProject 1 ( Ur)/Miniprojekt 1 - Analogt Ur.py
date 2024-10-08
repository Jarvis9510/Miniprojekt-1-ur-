# Example file showing a basic pygame "game loop"
import pygame
import math
from datetime import datetime

# boiler-plate
pygame.init()
screen_size = (640,480)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Analogt Ur")
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 16)

#Global variables
radius = 200
start_pos = (screen_size[0]/2,screen_size[1]/2) #start position in the middle of the screen


# Main loop
running = True
while True:
    screen.fill("black")
    
    #!----Clock layout ------#   
    pygame.draw.circle(screen, (255, 255, 255), start_pos, radius, 1) # Background circle
    
    for i in range(12):
        angle = 360/12*i
        marker_length = 10 
        inner_x = (start_pos[0]+(radius-marker_length)*math.cos(math.radians(angle)))
        inner_y =  (start_pos[1]+(radius-marker_length)*math.sin(math.radians(angle)))
        outer_x = (start_pos[0]+radius*math.cos(math.radians(angle)))
        outer_y = (start_pos[1]+radius*math.sin(math.radians(angle)))
        pygame.draw.line(screen, (255,255,255), (inner_x, inner_y), (outer_x, outer_y), 1)
       
        #!------Numbers------#
        distance = radius*1.1
        number_pos = (start_pos[0]+distance*math.cos(math.radians(angle-60)), 
                      start_pos[1]+distance*math.sin(math.radians(angle-60)))
        number_text = font.render(str(i + 1), True, (255,255,255))
        text_rect = number_text.get_rect(center=(number_pos))
        screen.blit(number_text, text_rect)

    #!----Clock hand 1 (seconds)----------------#
    s = datetime.now().second 
    angle_1  = 360/60*s
    clock_hand_1 = radius * 0.8
    tik_tok_1 = [clock_hand_1*math.cos(math.radians(angle_1-90)), clock_hand_1*math.sin(math.radians(angle_1-90))]
    end_pos_1 = (start_pos[0]+tik_tok_1[0], start_pos[1]+tik_tok_1[1])
    pygame.draw.line(screen, (255, 255, 255), start_pos, end_pos_1, 1)
    
    #!----Clock hand 2 (minute) ----------------#
    m = datetime.now().minute
    angle_2 = 360/60*m+6*(s/60)
    clock_hand_2 = radius * 0.7
    tik_tok_2 = [clock_hand_2*math.cos(math.radians(angle_2-90)), clock_hand_2*math.sin(math.radians(angle_2-90))]
    end_pos_2 = (start_pos[0]+tik_tok_2[0], start_pos[1]+tik_tok_2[1])
    pygame.draw.line(screen, (255, 255, 255), start_pos, end_pos_2, 2)
    
    #!----Clock hand 3 (hour) ----------------#
    h = datetime.now().hour
    angle_3 = 360/12*h+30*(m/60)
    clock_hand_3 = radius*0.5
    tik_tok_3 = [clock_hand_3*math.cos(math.radians(angle_3-90)), clock_hand_3*math.sin(math.radians(angle_3-90))]
    end_pos_3 = (start_pos[0]+tik_tok_3[0], start_pos[1]+tik_tok_3[1])
    pygame.draw.line(screen, (255, 255, 255), start_pos, end_pos_3, 4)
    
    #!----Center circle ---------------#
    pygame.draw.circle(screen, (200, 20, 20), start_pos, 4.5) # Background circle
    
    #boiler-plate
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            exit()