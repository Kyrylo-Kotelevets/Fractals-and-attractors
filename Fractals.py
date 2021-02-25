#!/usr/bin/python
# -*-coding: utf-8-*-

from PIL import Image, ImageDraw
from math import pi, sin, cos, sqrt
from random import randint, choice
from point_2D import point
import numpy as np


def interpolate(from_color: tuple, to_color: tuple, interval: int):
    ''' Вычисляем последовательность цветов для перехода от from_color к to_color за interval шагов'''
    delta =[(t - f) / interval for f, t in zip(from_color, to_color)]  # разница значений (r, g, b) в соседних цветах
    return [tuple(round(f + det * i) for f, det in zip(from_color, delta)) for i in range(interval)]


def triangle(back_color: str=(0, 0, 0),  # Цвет фона
             from_color: str=(0, 255, 0),  # Начальный цвет градиента
             to_color:   str=(0, 255, 0),  # Конечный цвет градиента
             size: int=1920,  # Размер изображения
             points: int=200000,  # Количество рисуемых точек
             border: int=100,  # Отступы вершин от краёв изображения
             filename: str="Треугольник_Серпинского"  # Имя файла для сохранения
             ) -> None:

    ''' Построение треугольника Серпинского '''
    image = Image.new('RGB', (size, size), back_color)
    drawer = ImageDraw.Draw(image)

    # Длина стороны и высоты тругольника
    side = size - 2 * border
    height = sqrt(3) * (size // 2 - border)

    # Список вершин треугольника
    vertex = [point(size // 2, border),
              point(border, border + height),
              point(size - border, border + height)]

    # Интерполируем заданные цвета вдоль длины стороны
    gradient = interpolate(from_color, to_color, interval=int(side))

    # Выбираем случайную вершнину и стартуем
    curr = choice(vertex)
    for i in range(points):
        # На каждом шаге случайно выбираем одну из трех вершин и проходим половину расстояния к ней
        curr = (curr + choice(vertex)) // 2
        drawer.point(tuple(curr), fill=gradient[int(curr.x - border)])

    # Опционально сохраняем результат
    if filename:
        image.save(f"{filename}.png")

    # Показываем получившееся
    image.show()


def carpet(back_color: tuple=(0, 0, 0),  # Цвет фона
           from_color: tuple=(0, 255, 0),  # Начальный цвет градиента
           to_color:   tuple=(0, 255, 0),  # Конечный цвет градиента
           size: int=1920,   # Размер изображения
           points: int=500000,  # Количество рисуемых точек
           border: int=200,  # Отступы вершин от краёв изображения
           koef: float=2.0,  # Коефициент перемещения точки
           filename: str="Ковёр_Серпинского"  # Имя файла для сохранения
           ) -> None:

    ''' Построение ковра Серпинского '''
    image = Image.new('RGB', (size, size), back_color)
    drawer = ImageDraw.Draw(image)

    # Координаты вершин и центров сторон квадрата
    vertex = [point(border, border),           point(size - border, border),
              point(border, size - border),    point(size - border, size - border),
              point(size // 2, border),        point(border, size // 2),
              point(size - border, size // 2), point(size // 2, size - border)]

    # Длина стороны и количество главных диагоналей
    side = size - 2 * border
    diag = 2 * size - 1

    # Интерполируем заданные цвета вдоль количества побочных диагоналей
    gradient = interpolate(from_color, to_color, interval=int(diag))

    # Выбираем случайную точку и стартуем
    curr = choice(vertex)
    for i in range(points):
        # На каждои шаге проходим расстояние к случайной вершине по формуле
        curr = (curr + koef * choice(vertex)) / (koef + 1)
        drawer.point(tuple(curr), fill=gradient[int(curr.x + curr.y - 2 * border)])

    # Опционально сохраняем результат
    if filename:
        image.save(f"{filename}.png")

    # Показываем получившееся
    image.show()


def fern(back_color: tuple=(0, 0, 0),  # Цвет фона
         from_color: tuple=(0, 255, 0),  # Начальный цвет градиента
         to_color:   tuple=(0, 255, 0),  # Конечный цвет градиента
         size: int=1920,   # Размер изображения
         points: int=350000,  # Количество рисуемых точек
         filename: str="Папоротник_Барнсли"  # Имя файла для сохранения
         ) -> None:

    ''' Построение папоротника Барнсли '''
    image = Image.new('RGB', (size, size), back_color)
    drawer = ImageDraw.Draw(image)

    # Коефициенты масштабирования вдоль осей
    w_scale = size / 10
    h_scale = size / 11

    # Интерполируем заданные цвета вдоль длины стороны изображения
    gradient = interpolate(to_color, from_color, interval=int(size))

    # Вероятности преобразований
    probability = [0.02, 0.84, 0.07, 0.07]
    # Векторы к преобразованиям
    addition = [[0.00, 0.00],
                [0.00, 1.60],
                [0.00, 1.60],
                [0.00, 0.44]]

    # Сами матрицы преобразований
    transform = [[[ 0.00,  0.00],
                  [ 0.00,  0.16]],

                 [[ 0.85,  0.04],
                  [-0.04,  0.85]],

                 [[ 0.20, -0.26],
                  [ 0.23,  0.22]],

                 [[-0.15,  0.28],
                  [ 0.26,  0.24]]]

    # Начинаем из нулевой координаты
    curr = point(0, 0)
    for i in range(points):
        # Случайно выбираем номер трансформации
        move = np.random.choice(np.arange(4), p=probability)
        # Непосредственно применяем её
        curr = transform[move] * curr + addition[move]
        drawer.point((curr.x * w_scale + size // 2, curr.y * h_scale), fill=gradient[int(curr.y * h_scale)])

    # Опционально сохраняем результат
    if filename:
        image.save(f"{filename}.png")

    # Показываем получившееся
    image.show()


def tree(n: float,  # Обратный коефициент левого изгиба
         m: float,  # Обратный коефициент правого изгиба
         line_len: int=400,  # Начальная длина линии
         size: int=1920,  # Размер изображения
         back_color: tuple=(0, 0, 0),  # Цвет фона
         line_color: tuple=(0, 255, 0),  # Цвет линии
         line_width: int=1,  # Толщина линии
         decr_koef: float=0.7,  # Коефициент уменьшения длины линии (ОЧЕНЬ ЧУВСТВИТЕЛЬНЫЙ)
         start_angle: float=pi/2,  # Начальный угол
         border: int=400,  # Отступ начала линии от края изображения
         filename: str="Дерево_Пифагора"  # Имя файла для сохранения
         ) -> None:

    ''' Построение Пифагорова дерева '''
    image = Image.new('RGB', (size, size), back_color)
    drawer = ImageDraw.Draw(image)

    ''' Вспомогательная функция для рекурсивной отрисовки ветвей '''
    def draw(curr: point, L: int, angle: float):
        if (L > 1):  # Если длина линии еще не единичная
            nex = curr + point(L * cos(angle), -L * sin(angle))  # Вычисляем след. точку
            drawer.line([tuple(curr), tuple(nex)], fill=line_color, width=line_width)

            draw(nex, L * decr_koef, angle + pi / n)  # Рекурсивно рисуем правую ветвь
            draw(nex, L * decr_koef, angle - pi / m)  # Рекурсивно рисуем левую ветвь

    # Запускаем рекурсивную рисовку
    draw(point(size / 2, size - border), line_len, start_angle)

    # Опционально сохраняем результат
    if filename:
        image.save(f"{filename}.png")

    # Показываем получившееся
    image.show()

fern(from_color=(255, 0, 0), to_color=(255, 0, 255))