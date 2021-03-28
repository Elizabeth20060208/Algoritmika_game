import pygame
window = pygame.display.set_mode((1280, 720)) #Размер игрового окна
pygame.display.set_caption("Алгоритмика") #Название программы

class Object(pygame.sprite.Sprite):       #Класс объектов игры
    def __init__(self, img, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()  #Форма: прямоугольник
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

#Точка спауна игрока
start_x = 100
start_y = 120

#Импорт изображений
bg = pygame.transform.scale(pygame.image.load("images/bg.png"), (1280, 720)) #Загрузка фона с компьютера
player_img = pygame.transform.scale(pygame.image.load("images/player.png"), (60, 65)) #Загрузка игрока с компьютера
wall = pygame.transform.scale(pygame.image.load("images/wall.png"), (120, 100)) #Загрузка стенок с компьютера(дерева)

all_sprites = pygame.sprite.Group() #Создание группы объектов
walls = pygame.sprite.Group() #Создание группы стенок

player = Object(player_img, start_x, start_y, 4) #Создание объекта "игрок"
all_sprites.add(player) #Добавление объекта "игрок" в группу всех спрайтов

#Стенки

wall1 = Object(wall, 0, 0, 0)
all_sprites.add(wall1)
walls.add(wall1)
wall2 = Object(wall, 90, 0, 0)
all_sprites.add(wall2)
walls.add(wall2)
wall3 = Object(wall, 180, 0, 0)
all_sprites.add(wall3)
walls.add(wall3)
wall4 = Object(wall, 270, 0, 0)
all_sprites.add(wall4)
walls.add(wall4)
wall5 = Object(wall, 360, 0, 0)
all_sprites.add(wall5)
walls.add(wall5)
wall6 = Object(wall, 450, 0, 0)
all_sprites.add(wall6)
walls.add(wall6)
wall7 = Object(wall, 540, 0, 0)
all_sprites.add(wall7)
walls.add(wall7)
wall8 = Object(wall, 630, 0, 0)
all_sprites.add(wall8)
walls.add(wall8)
wall9 = Object(wall, 720, 0, 0)
all_sprites.add(wall9)
walls.add(wall9)
wall10 = Object(wall, 810, 0, 0)
all_sprites.add(wall10)
walls.add(wall10)

wall11 = Object(wall, 540, 90, 0)
all_sprites.add(wall11)
walls.add(wall11)
wall12 = Object(wall, 540, 180, 0)
all_sprites.add(wall12)
walls.add(wall12)
wall13 = Object(wall, 540, 270, 0)
all_sprites.add(wall13)
walls.add(wall13)
wall14 = Object(wall, 540, 360, 0)
all_sprites.add(wall14)
walls.add(wall14)

wall15 = Object(wall, 450, 360, 0)
all_sprites.add(wall15)
walls.add(wall15)
wall16 = Object(wall, 360, 360, 0)
all_sprites.add(wall16)
walls.add(wall16)
wall17 = Object(wall, 270, 360, 0)
all_sprites.add(wall17)
walls.add(wall17)

wall18 = Object(wall, 270, 270, 0)
all_sprites.add(wall18)
walls.add(wall18)
wall19 = Object(wall, 270, 180, 0)
all_sprites.add(wall19)
walls.add(wall19)

wall20 = Object(wall, 180, 180, 0)
all_sprites.add(wall20)
walls.add(wall20)
wall21 = Object(wall, 90, 180, 0)
all_sprites.add(wall21)
walls.add(wall21)

wall22 = Object(wall, 90, 270, 0)
all_sprites.add(wall22)
walls.add(wall22)
wall23 = Object(wall, 90, 360, 0)
all_sprites.add(wall23)
walls.add(wall23)

wall24 = Object(wall, 890, 0, 0)
all_sprites.add(wall24)
walls.add(wall24)
wall25 = Object(wall, 980, 0, 0)
all_sprites.add(wall25)
walls.add(wall25)
wall26 = Object(wall, 1160, 0, 0)
all_sprites.add(wall26)
walls.add(wall26)
wall27 = Object(wall, 1250, 0, 0)
all_sprites.add(wall27)
walls.add(wall27)

wall28 = Object(wall, 630, 180, 0)
all_sprites.add(wall28)
walls.add(wall28)
wall29 = Object(wall, 720, 180, 0)
all_sprites.add(wall29)
walls.add(wall29)

wall30 = Object(wall, 270, 450, 0)
all_sprites.add(wall30)
walls.add(wall30)
wall31 = Object(wall, 270, 540, 0)
all_sprites.add(wall31)
walls.add(wall31)

wall32 = Object(wall, 360, 540, 0)
all_sprites.add(wall32)
walls.add(wall32)
wall33 = Object(wall, 450, 540, 0)
all_sprites.add(wall33)
walls.add(wall33)
wall34 = Object(wall, 540, 540, 0)
all_sprites.add(wall34)
walls.add(wall34)

wall35 = Object(wall, 1250, 90, 0)
all_sprites.add(wall35)
walls.add(wall35)
wall36 = Object(wall, 1250, 180, 0)
all_sprites.add(wall36)
walls.add(wall36)
wall37 = Object(wall, 1250, 270, 0)
all_sprites.add(wall37)
walls.add(wall37)
wall38 = Object(wall, 1250, 360, 0)
all_sprites.add(wall38)
walls.add(wall38)
wall39 = Object(wall, 1250, 450, 0)
all_sprites.add(wall39)
walls.add(wall39)

#Стенки


run = True
while run:
    window.blit(bg, (0, 0)) #Наложение фона
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Выход при нажатии на крестик
            run = False

    keys = pygame.key.get_pressed() #Нажатие на клавиатуру
    #Передвижение игрока
    if event.type == pygame.KEYDOWN:
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            player.rect.y -= player.speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            player.rect.y += player.speed
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            player.image = player_img
            player.rect.x -= player.speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            player.image = pygame.transform.flip(player_img, True, False)
            player.rect.x += player.speed


    all_sprites.draw(window) #Отображение спрайтов в окне
    all_sprites.update() #Обновление спрайтов
    pygame.display.update() #Обновление экрана