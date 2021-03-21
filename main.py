import pygame
window = pygame.display.set_mode((800, 600)) #Размер игрового окна
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

bg = pygame.transform.scale(pygame.image.load("images/bg.png"), (800, 600)) #Загрузка фона с компьютера
player_img = pygame.transform.scale(pygame.image.load("images/player.png"), (60, 65)) #Загрузка игрока с компьютера

all_sprites = pygame.sprite.Group() #Создание группы объектов

player = Object(player_img, start_x, start_y, 3) #Создание объекта "игрок"
all_sprites.add(player) #Добавление объекта "игрок" в группу всех спрайтов


run = True
while run:
    window.blit(bg, (0, 0)) #Наложение фона
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Выход при нажатии на крестик
            run = False

    keys = pygame.key.get_pressed() #Нажатие на клавиатуру
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