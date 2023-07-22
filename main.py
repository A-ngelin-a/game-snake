import pygame
import random

# Инициализация Pygame
pygame.init()

# Размер окна игры
window_width = 800
window_height = 600

# Цвета
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Размеры змейки и яблока
snake_size = 20
apple_size = 20

# Скорость змейки
initial_snake_speed = 5

# Создание окна игры
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Змейка')

clock = pygame.time.Clock()


# Отрисовка змейки
def draw_snake(snake_list):
    for segment in snake_list:
        pygame.draw.rect(window, black, [segment[0], segment[1], snake_size, snake_size])


# Основной цикл игры
def game_loop():
    game_over = False
    game_exit = False

    # Начальные координаты змейки
    x = window_width / 2
    y = window_height / 2

    # Начальные значения изменений координат
    x_change = 0
    y_change = 0

    # Создание яблока
    apple_x = round(random.randrange(0, window_width - apple_size) / 20.0) * 20.0
    apple_y = round(random.randrange(0, window_height - apple_size) / 20.0) * 20.0

    # Список сегментов змейки
    snake_list = []
    snake_length = 1

    # Скорость змейки
    snake_speed = initial_snake_speed
    while not game_exit:
        while game_over:
            window.fill(white)
            font_style = pygame.font.SysFont(None, 50)
            message = font_style.render("Game Over! Press Q-Quit or C-Play Again", True, red)
            window.blit(message, [window_width / 2 - 300, window_height / 2 - 50])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_size
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_size
                    x_change = 0

        # Проверка столкновений змейки с границами окна
        if x >= window_width or x < 0 or y >= window_height or y < 0:
            game_over = True

        # Изменение координат змейки
        x += x_change
        y += y_change

        # Очистка окна игры
        window.fill(white)

        # Отрисовка яблока
        pygame.draw.rect(window, red, [apple_x, apple_y, apple_size, apple_size])

        # Создание и отрисовка змейки
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_over = True

        draw_snake(snake_list)

        pygame.display.update()

        # Проверка столкновения змейки с яблоком
        if x == apple_x and y == apple_y:
            apple_x = round(random.randrange(0, window_width - apple_size) / 20.0) * 20.0
            apple_y = round(random.randrange(0, window_height - apple_size) / 20.0) * 20.0
            snake_length += 1
            snake_speed += 1

        # Ограничение скорости змейки
        clock.tick(snake_speed)

    pygame.quit()
    quit()


# Запуск игры
game_loop()