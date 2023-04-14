import pygame as pg
import sys

# экран
pg.init()  # инициализация всех модулей пайгейма
SCREEN_WIDTH = 800  # ширина экрана
SCREEN_HEIGHT = 600  # высота экрана
SCREEN_COLOR = (0, 0, 0)  # задаём цвет экрана
screen = pg.display.set_mode(
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)  # задали размер экрана

# игрок
player_width = 50  # ширина игрока
player_height = 50  # высота игрока
player_x = SCREEN_WIDTH // 2 - player_width // 2  # x игрока
player_y = SCREEN_HEIGHT // 2 - player_height // 2  # y игрока
player = pg.Rect(
    player_x, player_y, player_width, player_height
)  # прямоугольник-игрок, координаты x и y, ширина и высота
PLAYER_COLOR = (70, 130, 180)  # задаём цвет игрока

while True:  # главный цикл программы

    # работа с событиями
    for event in pg.event.get():  # идём по всем событиям
        if event.type == pg.QUIT:  # ловим событие выхода
            pg.quit()  # выгружает модули из памяти
            sys.exit()  # закрывает окно

        if event.type == pg.KEYDOWN:  # ловим нажатия клавиш
            if event.key == pg.K_ESCAPE:  # нажат Esc
                pg.quit()
                sys.exit()

        if event.type == pg.KEYDOWN:  # ловим нажатия клавиш
            if event.key == pg.K_RIGHT:  # проверяем нажата ли нужная кнопка
                player.x += 50  # игрок идёт в право

        if event.type == pg.KEYDOWN:  # ловим нажатия клавиш
            if event.key == pg.K_LEFT:  # проверяем нажата ли нужная кнопка
                player.x -= 50  # игрок идёт в лево

        if event.type == pg.KEYDOWN:  # ловим нажатия клавиш
            if event.key == pg.K_DOWN:  # проверяем нажата ли нужная кнопка
                player.y += 50  # игрок идёт в вниз

        if event.type == pg.KEYDOWN:  # ловим нажатия клавиш
            if event.key == pg.K_UP:  # проверяем нажата ли нужная кнопка
                player.y -= 50  # игрок идёт в вверх

    # отрисовка(reder)
    screen.fill(SCREEN_COLOR)  # заливаем весь экран
    pg.draw.rect(screen, PLAYER_COLOR, player)  # рисуем игрока
    pg.display.flip()  # обновляем экран