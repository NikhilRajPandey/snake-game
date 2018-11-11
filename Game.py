import pygame
import random
# main game

pygame.init()
screen_width = 900
screen_height = 500
game =  pygame.display.set_mode((screen_width,screen_height))
ex = False
gameover = False
# colors
white = (255,255,255)
bl = (25,50,100)
red = (255,0,0)
# Spesfic variables
x = 45
y = 55
h = 30
f_x = random.randint(20,885)
f_y = random.randint(20,485)
velocity_x = 0
velocity_y = 0
fps = 30
clock = pygame.time.Clock()
snk_l = []
snk_le = 1
font = pygame.font.SysFont(None,55)
# stoping from exiting
def plot():
    for v_x,v_y in snk_l:
        pygame.draw.rect(game, bl, [v_x, v_y, h, h])
# def sloop(text,x_axis,y_axis):
#     font = pygame.font.SysFont(None,55)
#     s_t  = font.render(text,True,red)
#     game.blit(s_t,[x_axis,y_axis])

# def world():
    #     game.fill(white)
    #     txt = font.render("Press Enter to play", True, bl)
    #     game.blit(txt, [50, 60])
    #     pygame.display.update()
while not ex:
    score = len(snk_l) * 5
    # sloop("Enter to play",200,500)
    # events to respond
    game.fill(white)
    txt = font.render("Score:"+str(score), True, bl)
    game.blit(txt, [5, 5])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ex = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = 10
                velocity_y = 0
            if event.key == pygame.K_LEFT:
                velocity_x = -10
                velocity_y = 0
            if event.key == pygame.K_DOWN:
                velocity_y = 10
                velocity_x = 0
            if event.key == pygame.K_UP:
                velocity_y = -10
                velocity_x = 0
    if abs(x - f_x)<8 and abs(y - f_y)<8:
        snk_le = snk_le + 5
        f_x = random.randint(20, screen_width / 2)
        f_y = random.randint(20, screen_height / 2)
    if x<0 or y<0 or x>screen_width or y>screen_height:
        ex = True
        pygame.mixer.music.stop()
    head = []
    head.append(x)
    head.append(y)
    snk_l.append(head)
    if head in snk_l[:-2]:
        ex = True
        pygame.mixer.music.stop()
    plot()
    # snk = pygame.draw.rect(game, bl, [x, y, h, h])
    food = pygame.draw.rect(game, red, [f_x, f_y, h, h])
    x = x + velocity_x
    y = y + velocity_y
    if len(snk_l)>snk_le:
        del snk_l[0]
    clock.tick(fps)
    pygame.display.update()
pygame.quit()
quit()