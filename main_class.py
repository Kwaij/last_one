import pygame
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()

class charter:
    def __init__(self, screen, image, x, y, move, jump, bulet_speed, bulet_range, hp, ammo):
        self.screen = screen
        self.image = image
        self.anim = 0  
        self.up = False
        self.down = True
        self.l = False
        self.r = False
        self.x = x
        self.y = y
        self.move = move
        self.jump = jump
        self.jump_speed = jump / 100
        self.jump_speed_down = jump / 200
        self.jump_up = y - jump
        self.jump_down = y
        self.bulet = None
        self.bulet_speed = bulet_speed
        self.bulet_range = bulet_range
        self.bulets_l = []
        self.bulets_r = []
        self.hp = hp
        self.ammo = ammo
        self.reload = False
        self.reload_time = 0
        self.sound_step = pygame.mixer.Sound('sound/step.mp3')
        self.sound_jump = pygame.mixer.Sound('sound/jump.mp3')
        self.sound_shoot = pygame.mixer.Sound('sound/shoot.mp3')
        self.sound_reload = pygame.mixer.Sound('sound/reload.mp3')
        self.sound_got_you = pygame.mixer.Sound('sound/got_you.mp3')
        self.sound_bulet = pygame.mixer.Sound('sound/bulet_on_bulet.mp3')
    
    def control(self):
        if self.y != self.jump_down:
            self.down = False
        else:
            self.down = True
  
        if self.up and self.y > self.jump_up:
            self.y -= self.jump_speed
            if self.y < self.jump_up:
                self.up = False   
        else:
            if self.y < self.jump_down:
                self.y += self.jump_speed_down  

        if self.reload and self.down:
            self.sound_step.stop()
            self.reload_time += 1    
            if self.reload_time == 200:
                self.ammo = 10
                self.reload = False
                self.reload_time = 0
        else:
            self.reload = False
            self.reload_time = 0
            
    def move_l(self):
        self.x -= self.move
        self.l = True
        self.r = False

    def move_r(self):
        self.x += self.move
        self.l = False
        self.r = True

    def animation_count(self):
        if self.anim == 1:
            self.anim = 0
        else:
            self.anim += 1 
    
    def animation_stay(self):
        self.rect = self.image[0].get_rect(topleft=(self.x,self.y))  
        if not self.down:
            self.screen.blit(self.image[3],(self.x,self.y))
        else:
            self.screen.blit(self.image[0],(self.x,self.y))  
 
    def animation_l(self):
        self.animation_count()
        if not self.down:
            self.screen.blit(self.image[4][self.anim],(self.x,self.y))
        else: 
            self.screen.blit(self.image[1][self.anim],(self.x,self.y))

    def animation_r(self):
        self.animation_count()
        if not self.down:
            self.screen.blit(self.image[5][self.anim],(self.x,self.y))
        else:
            self.screen.blit(self.image[2][self.anim],(self.x,self.y)) 

    def bulets_append(self):
        if self.l and self.ammo > 0:
            self.bulets_l.append(self.image[6].get_rect(topleft=(self.x,self.y + 10)))
            self.ammo -= 1
            self.sound_shoot.play()
        elif self.r and self.ammo > 0:
            self.bulets_r.append(self.image[6].get_rect(topleft=(self.x,self.y + 10)))
            self.ammo -= 1
            self.sound_shoot.play()

    def bulet_screen(self, player):
        if self.bulets_l:
            for (i, el) in enumerate(self.bulets_l):
                self.screen.blit(self.image[6],(el.x, el.y))
                el.x -= self.bulet_speed
                if el.x < self.x - self.bulet_range:
                    self.bulets_l.pop(i)
                if player.rect.colliderect(el):
                    self.bulets_l.pop(i)
                    player.hp -= 1
                    player.sound_got_you.play()
                if player.bulets_l:
                    for (player_i, player_el) in enumerate(player.bulets_l):
                        if el.colliderect(player_el):
                            player.bulets_l.pop(player_i)
                            self.bulets_l.pop(i)
                            self.sound_shoot.stop()
                            self.sound_bulet.play()
                if player.bulets_r:
                    for (player_i, player_el) in enumerate(player.bulets_r):
                        if el.colliderect(player_el):
                            player.bulets_r.pop(player_i)
                            self.bulets_l.pop(i)
                            self.sound_shoot.stop()
                            self.sound_bulet.play()

        if self.bulets_r:
            for (i, el) in enumerate(self.bulets_r):
                self.screen.blit(self.image[6],(el.x, el.y))
                el.x += self.bulet_speed
                if el.x > self.x + self.bulet_range:
                    self.bulets_r.pop(i)
                if player.rect.colliderect(el):
                    self.bulets_r.pop(i)
                    player.hp -= 1
                    player.sound_got_you.play()
                if player.bulets_l:
                    for (player_i, player_el) in enumerate(player.bulets_l):
                        if el.colliderect(player_el):
                            player.bulets_l.pop(player_i)
                            self.bulets_r.pop(i)
                if player.bulets_r:
                    for (player_i, player_el) in enumerate(player.bulets_r):
                        if el.colliderect(player_el):
                            player.bulets_r.pop(player_i)
                            self.bulets_r.pop(i)
        
    def start_info(self,x,y):
        info_text = pygame.font.Font('fonts/Roboto-Black.ttf', 40)
        text_move_left = info_text.render('Blue control: ', False, (0, 0, 0))
        text_move_right = info_text.render('MOVE: A and D', False, (0, 0, 0))
        text_jump = info_text.render('AMMO: ', False, (0, 0, 0))
        text_reload = info_text.render('AMMO: ', False, (0, 0, 0))
        self.screen.blit(text_move_left, (x, y))
        self.screen.blit(text_move_right, (x, y + 50))
        self.screen.blit(text_jump, (x, y + 100))
        self.screen.blit(text_reload, (x, y + 150))
    
    def info(self,x,y):
        game_text = pygame.font.Font('fonts/Roboto-Black.ttf', 40)
        player_hp = game_text.render('HP: ' + str(self.hp), False, (0, 0, 0))
        player_ammo = game_text.render('AMMO: ' + str(self.ammo), False, (0, 0, 0))
        player_reload = game_text.render('reload', False, (0, 0, 0))
        self.screen.blit(player_hp, (x, y))
        self.screen.blit(player_ammo, (x, y + 50))
        if self.reload:
            self.screen.blit(player_reload, (x, y + 100))

    def win_info(self):
        None
    
    def reset(self, hp, ammo, x, y):
        self.hp = hp
        self.ammo = ammo
        self.x = x
        self.y = y
        self.bulets_l.clear()
        self.bulets_r.clear()

class player_info:
    def __init__(self, screen, name, left, right, shoot, jump, reload):
        self.screen = screen
        self.name = name
        self.left = left
        self.right = right
        self.shoot = shoot
        self.jump = jump
        self.reload = reload
    
    def show_info(self, x, y):
        text_show = pygame.font.Font('fonts/Roboto-Black.ttf', 40)
        show_player = text_show.render('' + str(self.name) + ' control:', False, (0, 0, 0))
        show_left = text_show.render('move left: ' + str(self.left), False, (0, 0, 0))
        show_right = text_show.render('move right: ' + str(self.right), False, (0, 0, 0))
        show_shoot = text_show.render('shoot: ' + str(self.shoot), False, (0, 0, 0))
        show_jump = text_show.render('jump: ' + str(self.jump), False, (0, 0, 0))
        show_reload = text_show.render('reload: ' + str(self.reload), False, (0, 0, 0))
        self.screen.blit(show_player, (x, y))
        self.screen.blit(show_left, (x, y + 50))
        self.screen.blit(show_right, (x, y + 100))
        self.screen.blit(show_shoot, (x, y + 150))
        self.screen.blit(show_jump, (x, y + 200))
        self.screen.blit(show_reload, (x, y + 250))

    def win_info(self, x, y):
        text_show = pygame.font.Font('fonts/Roboto-Black.ttf', 40)
        win_player = text_show.render('' + str(self.name) + ' WIN', False, (0, 0, 0))
        next_game = text_show.render('press SPACE to play again', False, (0, 0, 0))
        self.screen.blit(win_player, (x, y))
        self.screen.blit(next_game, (x - 150, y + 50))