from main_class import *

W, H = 1920, 1080
screen = pygame.display.set_mode((W, H),flags=pygame.NOFRAME)

x = 200
y = H - 200
move = 2
jump = 300
bulet_spped = 5
bulet_range = 1000
hp = 10
ammo = 10

blue_image = [
            pygame.image.load('image/blue.png').convert_alpha(),
            [
            pygame.image.load('image/blue_l_1.png').convert_alpha(),
            pygame.image.load('image/blue_l_2.png').convert_alpha()
            ],
            [
            pygame.image.load('image/blue_r_1.png').convert_alpha(),
            pygame.image.load('image/blue_r_2.png').convert_alpha()
            ],
            pygame.image.load('image/blue_jump.png').convert_alpha(),
            [
            pygame.image.load('image/blue_jump_l_1.png').convert_alpha(),
            pygame.image.load('image/blue_jump_l_2.png').convert_alpha()
            ],
            [
            pygame.image.load('image/blue_jump_r_1.png').convert_alpha(),
            pygame.image.load('image/blue_Jump_r_2.png').convert_alpha()
            ],
            pygame.image.load('image/blue_bulet.png').convert_alpha()
            ]
red_image = [
            pygame.image.load('image/red.png').convert_alpha(),
            [
            pygame.image.load('image/red_l_1.png').convert_alpha(),
            pygame.image.load('image/red_l_2.png').convert_alpha()
            ],
            [
            pygame.image.load('image/red_r_1.png').convert_alpha(),
            pygame.image.load('image/red_r_2.png').convert_alpha()
            ],
            pygame.image.load('image/red_jump.png').convert_alpha(),
            [
            pygame.image.load('image/red_jump_l_1.png').convert_alpha(),
            pygame.image.load('image/red_jump_l_2.png').convert_alpha()
            ],
            [
            pygame.image.load('image/red_jump_r_1.png').convert_alpha(),
            pygame.image.load('image/red_Jump_r_2.png').convert_alpha()
            ],
            pygame.image.load('image/red_bulet.png').convert_alpha()
            ]

player_1 = charter(screen, blue_image, x, y, move, jump, bulet_spped, bulet_range, hp, ammo)
player_2 = charter(screen, red_image, W - x, y, move, jump, bulet_spped, bulet_range, hp, ammo)