import pygame
import os
import time
import sys

pygame.init()
size = width, height = 1280, 720
screen = pygame.display.set_mode(size)
running = True
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
run1, run2, run3 = False, False, False
bounce = False
now_time = 0
now_time_bounce_left = 0
now_time_bounce_right = 0
now_time_bounce = 0
block_left_right = True
trampoline = 0
speed = 0
platforms = pygame.sprite.Group()
num_music = 0
num_sounds = 1
music_play = True
speed_right = 0
level_num = 1
num_click_level = 0


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def sounds():
    if num_sounds == 1:
        per_sound = pygame.mixer.Sound('data/per_menu.ogg')
        per_sound.play()


def music():
    global music_play
    if music_play:
        music_play = not music_play
        pygame.mixer.music.stop()
    else:
        music_play = not music_play
        pygame.mixer.music.play(-1)


def start_music():
    pygame.mixer.music.load('data/fon_music.mp3')
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)


def options_screen():
    global num_sounds, num_music
    menu = ['music.png', 'sounds.png']
    menu_num = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    sounds()
                    menu_num = (menu_num + 1) % len(menu)
                if event.key == pygame.K_UP:
                    sounds()
                    menu_num = (menu_num - 1) % len(menu)
                if event.key == pygame.K_RETURN:
                    sounds()
                    if abs(menu_num) == 0:
                        music()
                        num_music = (num_music + 1) % 2
                    if abs(menu_num) == 1:
                        num_sounds = (num_sounds + 1) % 2
                if event.key == pygame.K_ESCAPE:
                    sounds()
                    return
        screen.fill((0, 0, 0))
        fon1 = pygame.transform.scale(load_image(menu[menu_num], -1), (width, height))
        screen.blit(fon1, (0, 0))
        if num_music == 1:
            fon2 = pygame.transform.scale(load_image('galochka_music.png', -1),
                                          (width, height))
            screen.blit(fon2, (0, 0))
        if num_sounds == 1:
            fon3 = pygame.transform.scale(load_image('galochka_sounds.png', -1),
                                          (width, height))
            screen.blit(fon3, (0, 0))
        pygame.display.flip()
        clock.tick(60)


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    pygame.mouse.set_visible(False)

    menu = ['fon_menu1.png', 'fon_menu2.png', 'fon_menu3.png']
    # menu_anim = ['menu_anim/menu_anim' + str(i) + '.png' for i in range(1, 125, 3)]
    menu_num = 0
    menu_num2 = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    sounds()
                    menu_num = (menu_num + 1) % len(menu)
                if event.key == pygame.K_UP:
                    sounds()
                    menu_num = (menu_num - 1) % len(menu)
                if event.key == pygame.K_RETURN:
                    sounds()
                    if abs(menu_num) == 0:
                        level_fon()
                    elif abs(menu_num) == 1:
                        options_screen()
                    else:
                        terminate()
        menu_num2 += 1
        # menu_num2 %= len(menu_anim)
        screen.fill((0, 0, 0))
        fon1 = pygame.transform.scale(load_image(menu[menu_num], -1), (width, height))
        # fon2 = pygame.transform.scale(load_image(menu_anim[menu_num2], -1), (width, height))
        screen.blit(fon1, (0, 0))
        # screen.blit(fon2, (0, 0))
        pygame.display.flip()
        clock.tick(60)


def level_fon():
    global level_num, num_click_level
    level = ['level_fon1.png', 'level_fon2.png']
    menu_num = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    sounds()
                    menu_num = (menu_num + 1) % len(level)
                if event.key == pygame.K_UP:
                    sounds()
                    menu_num = (menu_num - 1) % len(level)
                if event.key == pygame.K_ESCAPE:
                    start_screen()
                if event.key == pygame.K_RETURN:
                    sounds()
                    if abs(menu_num) == 0:
                        num_click_level += 1
                        level_num = 1
                        textures()
                        game()
                    elif abs(menu_num) == 1:
                        num_click_level += 1
                        level_num = 2
                        textures()
                        game()
        screen.fill((0, 0, 0))
        fon1 = pygame.transform.scale(load_image(level[menu_num], -1), (width, height))
        screen.blit(fon1, (0, 0))
        pygame.display.flip()
        clock.tick(60)


def finish_screen():
    menu = ['finish_menu1.png', 'finish_menu2.png', 'finish_menu3.png']
    menu_num = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    sounds()
                    menu_num = (menu_num + 1) % len(menu)
                if event.key == pygame.K_LEFT:
                    sounds()
                    menu_num = (menu_num - 1) % len(menu)
                if event.key == pygame.K_RETURN:
                    sounds()
                    if abs(menu_num) == 0:
                        lan.rect.x = 300
                        lan.rect.y = -500
                        start_screen()
                    elif abs(menu_num) == 1:
                        print('Переход на слейдущий уровень')
                    else:
                        lan.rect.x = 300
                        lan.rect.y = -500
                        game()
        screen.fill((0, 0, 0))
        fon1 = pygame.transform.scale(load_image(menu[menu_num], -1), (width, height))
        screen.blit(fon1, (0, 0))
        pygame.display.flip()
        clock.tick(60)


class Mountain0(pygame.sprite.Sprite):
    global level_num

    def __init__(self):
        super().__init__(all_sprites)
        self.image = load_image(f"l{level_num}_0.png", (0, 0, 0))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)


class Mountain(pygame.sprite.Sprite):
    global level_num

    def __init__(self):
        super().__init__(all_sprites)
        self.image = load_image(f"l{level_num}_1.png", (0, 0, 0))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)


class Mountain2(pygame.sprite.Sprite):
    global level_num

    def __init__(self):
        super().__init__(all_sprites)
        self.image = load_image(f"l{level_num}_2.png", (0, 0, 0))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)


class Mountain3(pygame.sprite.Sprite):
    global level_num

    def __init__(self):
        super().__init__(all_sprites)
        self.image = load_image(f"l{level_num}_3.png", (0, 0, 0))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)


class Mountain4(pygame.sprite.Sprite):
    global level_num

    def __init__(self):
        super().__init__(all_sprites)
        self.image = load_image(f"l{level_num}_4.png", (0, 0, 0))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)


class Mountain5(pygame.sprite.Sprite):
    global level_num

    def __init__(self):
        super().__init__(all_sprites)
        self.image = load_image(f"l{level_num}_5.png", (0, 0, 0))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)


class Mountain6(pygame.sprite.Sprite):
    global level_num

    def __init__(self):
        super().__init__(all_sprites)
        self.image = load_image(f"l{level_num}_6.png", (0, 0, 0))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)


class Mountain7(pygame.sprite.Sprite):
    global level_num

    def __init__(self):
        super().__init__(all_sprites)
        self.image = load_image(f"l{level_num}_7.png", (0, 0, 0))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)


class Mountain8(pygame.sprite.Sprite):
    global level_num

    def __init__(self):
        super().__init__(all_sprites)
        self.image = load_image(f"l{level_num}_8.png", (0, 0, 0))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)


class Person1(pygame.sprite.Sprite):
    image = load_image("cube.png")

    def __init__(self, pos):
        super().__init__(all_sprites)
        self.image = Person1.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        global run1, run2, run3, now_time, bounce, now_time_bounce_left, now_time_bounce_right
        global now_time_bounce, block_left_right, trampoline, speed, speed_right, x, y
        if pygame.sprite.collide_mask(self, mountain3):
            print(pygame.sprite.collide_mask(self, mountain),
                  pygame.sprite.collide_mask(self, mountain3), 'red')
        if pygame.sprite.collide_mask(self, mountain2):
            print(pygame.sprite.collide_mask(self, mountain),
                  pygame.sprite.collide_mask(self, mountain2), 'blue')
        if pygame.sprite.collide_mask(self, mountain5):
            # Шип от которого ты умираешь и телепортируешься к последней точки
            per_sound = pygame.mixer.Sound('data/pad.ogg')
            per_sound.play()
            self.rect.x = -x + 30
            self.rect.y = -y + 1100
            # self.rect.x = -300
            # self.rect.y = -300
        if pygame.sprite.collide_mask(self, mountain7):
            speed = time.clock()
        if time.clock() - speed < 0.2:
            speed_right = 12

        if pygame.sprite.collide_mask(self, mountain6):  # Батут
            per_sound = pygame.mixer.Sound('data/jump.ogg')
            per_sound.play()
            trampoline = time.clock()
        if time.clock() - trampoline < 0.2 and trampoline != 0:
            self.rect.y -= 45  # Прыжок батута

        # Прыжок от левой стены ниже
        now_time_bounce_global = time.clock()
        block_left_right = True
        if (pygame.sprite.collide_mask(self, mountain2) and run1 and pygame.sprite.collide_mask(self,
                                                                                                mountain) and
            pygame.sprite.collide_mask(self, mountain)[0] != 0) or \
                (pygame.sprite.collide_mask(self,
                                            mountain2) and run1 and not pygame.sprite.collide_mask(
                    self, mountain)):
            now_time_bounce_left = time.clock()
            run1 = False
        if now_time_bounce_global - now_time_bounce_left < 0.1 and now_time_bounce_left != 0:
            lan.rect.x -= 34
            lan.rect.top -= 53
            block_left_right = False
        # прыжок от правой стены ниже
        if (pygame.sprite.collide_mask(self, mountain3) and run1 and pygame.sprite.collide_mask(self,
                                                                                                mountain) and
            pygame.sprite.collide_mask(self, mountain)[1] != 47) or \
                (pygame.sprite.collide_mask(self,
                                            mountain3) and run1 and not pygame.sprite.collide_mask(
                    self, mountain)):
            now_time_bounce_right = time.clock()
            run1 = False
        if now_time_bounce_global - now_time_bounce_right < 0.1 and now_time_bounce_right != 0:
            lan.rect.x += 34
            lan.rect.top -= 53
            block_left_right = False

        if pygame.sprite.collide_mask(self, mountain) and \
                pygame.sprite.collide_mask(self, mountain3) and \
                pygame.sprite.collide_mask(self, mountain)[1] != 47 and \
                pygame.sprite.collide_mask(self, mountain3)[1] != 0:
            self.rect = self.rect.move(0, 1)  # Скорость падения у правой боковой стены
            # Падает если стоит в правой бокой границе и соприкосается с верхним пикселем текстуры

        if pygame.sprite.collide_mask(self, mountain) and \
                pygame.sprite.collide_mask(self, mountain2) and \
                pygame.sprite.collide_mask(self, mountain)[1] != 47 and \
                pygame.sprite.collide_mask(self, mountain2)[1] != 0:
            self.rect = self.rect.move(0, 1)  # Скорость падения у левой боковой стены
            # Падает если стоит в левой бокой  границе и соприкосается с верхним пикселем текстуры
        if pygame.sprite.collide_mask(self, mountain) and not pygame.sprite.collide_mask(self,
                                                                                         mountain2) and not pygame.sprite.collide_mask(
            self, mountain3):
            # Если персонаж упал ниже текстурки то он становится на нее
            lan.rect.top = lan.rect.top - (47 - pygame.sprite.collide_mask(self, mountain)[1])
        if pygame.sprite.collide_mask(self, mountain) and not \
                pygame.sprite.collide_mask(self, mountain2) and \
                pygame.sprite.collide_mask(self, mountain3):
            # Если персонаж упал ниже текстурки то он становится на нее
            lan.rect.top = lan.rect.top - (47 - pygame.sprite.collide_mask(self, mountain)[1])

        if pygame.sprite.collide_mask(self, mountain) and not pygame.sprite.collide_mask(self,
                                                                                         mountain3) and pygame.sprite.collide_mask(
            self, mountain2):
            # Если персонаж упал ниже текстурки то он становится на нее
            lan.rect.top = lan.rect.top - (47 - pygame.sprite.collide_mask(self, mountain)[1])

        if pygame.sprite.collide_mask(self, mountain3) and \
                pygame.sprite.collide_mask(self, mountain3)[
                    0] != 0 and not pygame.sprite.collide_mask(self, mountain4):
            lan.rect.x = lan.rect.x + pygame.sprite.collide_mask(self, mountain3)[0]
            # Если персонаж заехал за правую боковую сторону то он возращается к границе блока

        if pygame.sprite.collide_mask(self, mountain2) and \
                pygame.sprite.collide_mask(self, mountain2)[
                    0] != 47 and not pygame.sprite.collide_mask(self, mountain4):
            lan.rect.x = lan.rect.x - (47 - pygame.sprite.collide_mask(self, mountain2)[0])
            # Если персонаж заехал за левую боковую сторону то он возращается к границе блока

        if not pygame.sprite.collide_mask(self, mountain):
            self.rect = self.rect.move(0, 11)  # Падает если нет препятствий, со скоростью 1
        if pygame.sprite.collide_mask(self, mountain4) and \
                pygame.sprite.collide_mask(self, mountain4)[1] >= 0:
            lan.rect.y = lan.rect.y + pygame.sprite.collide_mask(self, mountain4)[1] + 2
            # Нельзя прыгнуть выше нижнего блока
        if ((pygame.sprite.collide_mask(self, mountain) and
             pygame.sprite.collide_mask(self, mountain)[
                 1] == 47)) or pygame.sprite.spritecollideany(self,
                                                              platforms):  # Прыжок может быть только на вверху платформы
            bounce = True
        else:
            bounce = False

        if run1 and bounce:
            now_time_bounce = time.clock()

            run1 = False
        if time.clock() - now_time_bounce < 0.1 and now_time_bounce != 0:
            lan.rect.top -= 39  # Скорость прыжка
        if run2 and not pygame.sprite.collide_mask(self, mountain2) and block_left_right:
            self.rect.x += 24 + speed_right  # Скорость вправо
        if run3 and not pygame.sprite.collide_mask(self, mountain3) and block_left_right:
            self.rect.x -= 24  # Скорость влево
        speed_right = 0
        run1 = False
        if pygame.sprite.spritecollideany(self, platforms):
            self.rect.top -= 11
            print(123)
        if pygame.sprite.collide_mask(self, mountain8):
            finish_screen()


class Platform(pygame.sprite.Sprite):

    def __init__(self, pos, size, sdvig_px, num, time_stop):
        super().__init__(all_sprites)
        self.add(platforms)
        self.image = pygame.Surface(size)
        self.image.fill(pygame.Color('orange'))
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.sdvig = sdvig_px
        self.now_time_platform = time.clock()
        self.num1 = num
        self.num2 = -1
        self.time_stop = time_stop

    def update(self):
        if time.clock() - self.now_time_platform > self.time_stop:
            self.num2 += 1
            if self.num2 % self.num1 == 0:
                self.sdvig = -self.sdvig
            self.rect.x += self.sdvig
            self.now_time_platform = time.clock()


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.dy = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        global x, y
        self.dx = -(target.rect.x + target.rect.w // 2 - width // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - height // 2)
        x -= self.dx
        y -= self.dy


def game():
    global run1, run2, run3, running
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            keys = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run1 = True
                if event.key == pygame.K_ESCAPE:
                    start_screen()
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                run2 = True
            else:
                run2 = False
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                run3 = True
            else:
                run3 = False

        all_sprites.draw(screen)
        all_sprites.update()
        camera.update(lan)
        for sprite in all_sprites:
            camera.apply(sprite)
        pygame.display.flip()
        clock.tick(60)
        screen.fill((0, 0, 0))

    pygame.quit()


x, y = 0, 0
mountain0 = 0
mountain = 0
mountain2 = 0
mountain3 = 0
mountain4 = 0
mountain5 = 0
mountain6 = 0
mountain7 = 0
mountain8 = 0


def textures():
    global mountain0, mountain, mountain2, mountain3, mountain4, mountain5, mountain6, mountain7, mountain8
    mountain0 = Mountain0()
    mountain = Mountain()
    mountain2 = Mountain2()
    mountain3 = Mountain3()
    mountain4 = Mountain4()
    mountain5 = Mountain5()
    mountain6 = Mountain6()
    mountain7 = Mountain7()
    mountain8 = Mountain8()


camera = Camera()
Platform((1700, 2020), (120, 15), 500, 1, 2)
Platform((6000, 1350), (150, 15), 15, 102, 0.1)
#lan = Person1((30, 1100))
lan = Person1((6057, 1300))
start_music()
start_screen()
