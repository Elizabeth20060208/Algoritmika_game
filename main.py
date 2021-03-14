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

bg = pygame.transform.scale(pygame.image.load("images/bg.png"), (800, 600)) #Загрузка фона с компьютера

run = True
while run:
    window.blit(bg, (0, 0)) #Наложение фона
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Выход при нажатии на крестик
            run = False






    pygame.display.update()