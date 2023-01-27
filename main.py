import pygame
from main_desc import *
from main_class import *
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()

pygame.display.set_caption('last one')

W, H = 1920, 1080
screen = pygame.display.set_mode((W, H),flags=pygame.NOFRAME)

clock = pygame.time.Clock()
FPS = 10
start_screan = pygame.image.load('image/game_screan.png').convert()
game_screan = pygame.image.load('image/yellow.png').convert()

start_sound = pygame.mixer.Sound('sound/background.mp3')
start_sound.play(loops=-1)

pygame.mixer.music.load('sound/Rip_Tear.mp3')
pygame.mixer.music.set_volume(0.2)
game_sound = pygame.mixer.Sound('sound/Rip_Tear.mp3')
game_sound.set_volume(0.2)

p_1 = "Blue"
p_1_left = pygame.K_a
p_1_right = pygame.K_d
p_1_shoot = pygame.K_v
p_1_jump = pygame.K_b
p_1_reload = pygame.K_n
p_1 = player_info(screen, p_1, 'a', 'd', 'v', 'b', 'n')

p_2 = 'Red'
p_2_left = pygame.K_LEFT
p_2_right = pygame.K_RIGHT
p_2_shoot = pygame.K_KP_1
p_2_jump = pygame.K_KP_2
p_2_reload = pygame.K_KP_3
p_2 = player_info(screen, p_2, 'left', 'right', 'num1', 'num2', 'num3')

gameplay = False
startscrean =True
runTime = True
while runTime:   
    pygame.display.update()

    keys = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    mouse_pres = pygame.mouse.get_pressed()  
    screen.blit(game_screan, (0, 0))
    
    if startscrean:
        screen.blit(game_screan, (0, 0))

        p_1.show_info(50, 50)
        p_2.show_info(W - 400, 50)

        if keys[pygame.K_SPACE]:
            startscrean = False
            gameplay = True
            start_sound.stop()
            #game_sound.play()
            pygame.mixer.music.play(-1)
    else:
        if gameplay:
            player_1.info(50, 50)
            player_2.info(W - 300, 50)

            player_1.control()
            player_2.control()

            if keys[p_1_reload] and player_1.down:
                player_1.reload = True
                player_1.sound_reload.play()
            if keys[p_1_jump] and player_1.down:
                player_1.up = True
            elif keys[p_1_left]:
                player_1.animation_l()
                if player_1.x > 50:
                    player_1.move_l()
            elif keys[p_1_right]:
                player_1.animation_r()   
                if player_1.x < W - 110:
                    player_1.move_r()
            else:
                player_1.animation_stay()

            if keys[p_2_reload] and player_2.down:
                player_2.reload = True
                player_2.sound_reload.play()
            if keys[p_2_jump] and player_2.down:
                player_2.up = True
            elif keys[p_2_left]:
                player_2.animation_l()
                if player_2.x > 50:
                    player_2.move_l()
            elif keys[p_2_right]:
                player_2.animation_r()       
                if player_2.x < W - 110:
                    player_2.animation_r()
                    player_2.move_r()
            else:
                player_2.animation_stay()

            player_1.bulet_screen(player_2)
            player_2.bulet_screen(player_1)

            if player_1.hp < 1 or player_2.hp < 1:
                gameplay = False
                start_sound.play()
                #game_sound.stop()
                pygame.mixer.music.stop()
        else:
            if keys[pygame.K_SPACE]:
                gameplay = True
                start_sound.stop()
                #game_sound.play()
                pygame.mixer.music.play(-1)
                player_1.reset(hp, ammo, x, y)
                player_2.reset(hp, ammo, W - x, y)

            if player_1.hp < 1:
                player_2.win_info()
                p_2.win_info(W / 2 - 100, H / 2 - 100)           
            elif player_2.hp < 1:
                player_1.win_info()
                p_1.win_info(W / 2 - 100, H / 2 - 100)          
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            runTime = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                runTime = False
        if event.type == pygame.KEYUP and event.key == p_1_shoot and not player_1.reload:
            player_1.bulets_append()
        if event.type == pygame.KEYUP and event.key == p_2_shoot and not player_2.reload:
            player_2.bulets_append()
            
clock.tick(FPS)