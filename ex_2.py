import pygame
from pygame.draw import *

pygame.init()

FPS = 30
display = pygame.display.set_mode((500, 800))

Black = (0, 0, 0)
White = (255, 255, 255)
Red = (255, 0, 0)
Red2 = (255, 100, 100)


def sky():
    """
    sky - background
    """
    rect(display, (138, 43, 226, 255), (0, 0, 500, 80))
    rect(display, (0, 0, 139, 255), (0, 80, 500, 80))
    rect(display, (238, 154, 0, 255), (0, 160, 500, 80))
    rect(display, (255, 181, 197, 255), (0, 240, 500, 80))
    rect(display, (142, 229, 238, 255), (0, 320, 500, 480))


def bird(x_step, y_step, scale_x, scale_y, width_of_line):
    """
    bird in sky - background
    """
    arc(display, White, [100 + x_step, 40 + y_step, scale_x, scale_y],
        0, 3.14, width_of_line)
    arc(display, White, [100 + scale_x + x_step, 40 + y_step, scale_x, scale_y],
        0, 3.14, width_of_line)


def all_birds():
    """
    composition of birds in sky - background
    """
    bird(0, 0, 70, 50, 3)
    bird(150, 80, 70, 50, 3)
    bird(90, 210, 70, 50, 3)
    bird(200, 50, 30, 25, 1)
    bird(220, 30, 30, 25, 1)
    bird(180, 10, 30, 25, 1)
    bird(160, 125, 30, 25, 1)
    bird(210, 145, 30, 25, 1)
    bird(180, 165, 30, 25, 1)
    bird(230, 185, 30, 25, 1)
    bird(90, 140, 30, 25, 1)
    bird(70, 170, 30, 25, 1)
    bird(110, 187, 30, 25, 1)
    bird(285, 145, 35, 30, 2)
    bird(320, 170, 33, 30, 2)
    bird(295, 200, 33, 30, 2)


def gull_body(surface, x, y, scale, color, width_of_line):
    """
    draws body of gull
    x, y - coordinates of the upper left corner of whole picture
    scale - size of gull
    width_of_line - width of outline
    """
    polygon(surface, color, [(x + 2 * scale, y), (x + 4 * scale, y + scale),
                             (x + 8 * scale, y + 2 * scale),
                             (x + 9 * scale, y + 6 * scale),
                             (x + 11 * scale, y + 7 * scale),
                             (x + 13 * scale, y + 7 * scale),
                             (x + 13 * scale, y + 8 * scale),
                             (x + 12 * scale, y + 9 * scale),
                             (x + 6 * scale, y + 9 * scale),
                             (x + 3 * scale, y + 10 * scale),
                             (x + 2 * scale, y + 7 * scale),
                             (x + 3 * scale, y + 6 * scale),
                             (x + 6 * scale, y + 7 * scale),
                             (x + 5 * scale, y + 6 * scale),
                             (x + 5 * scale, y + 5 * scale),
                             (x + 2 * scale, y + 4 * scale),
                             (x, y + 2 * scale), (x + 2 * scale, y + 3 * scale),
                             (x + 6 * scale, y + 3 * scale),
                             (x + 8 * scale, y + 6 * scale),
                             (x + 6 * scale, y + 3 * scale),
                             (x + 4 * scale, y + 2 * scale)], width_of_line)


def gull_head(surface, x, y, scale, width_of_line):
    """
    draw gull's head
    x, y - coordinates of the upper left corner of whole picture
    scale - size of gull
    width_of_line - width of outline
    """
    ellipse(surface, White,
            (12 * scale + x, 6 * scale + y, 4 * scale, 2 * scale))
    arc(surface, Black, (12 * scale + x, 6 * scale + y, 4 * scale, 2 * scale),
        -2.1, 3.14, width_of_line)


def gull_feet(surface, x, y, scale, color, width_of_line):
    """
    draw gull's feet
    x, y - coordinates of the upper left corner of whole picture
    scale - size of gull
    width_of_line - width of outline
    """
    polygon(surface, color, [(12 * scale + x, 12 * scale + y),
                             (11 * scale + x, 13 * scale + y),
                             (12 * scale + x, 12.5 * scale + y),
                             (13 * scale + x, 13 * scale + y),
                             (12.5 * scale + x, 12.3 * scale + y),
                             (13.5 * scale + x, 13 * scale + y),
                             (13 * scale + x, 12.3 * scale + y),
                             (14 * scale + x, 12 * scale + y)], width_of_line)
    polygon(surface, color, [(11 * scale + x, 13 * scale + y),
                             (10 * scale + x, 14 * scale + y),
                             (11 * scale + x, 13.5 * scale + y),
                             (12 * scale + x, 14 * scale + y),
                             (11.5 * scale + x, 13.3 * scale + y),
                             (12.5 * scale + x, 14 * scale + y),
                             (12 * scale + x, 13.3 * scale + y),
                             (13 * scale + x, 13 * scale + y)], width_of_line)


def gull_beak(surface, x, y, scale, width_of_line):
    """
    draw gull's beak
    x, y - coordinates of the upper left corner of whole picture
    scale - size of gull
    width_of_line - width of outline
    """
    polygon(surface, (255, 100, 100), [(16 * scale + x, 6.9 * scale + y),
                                       (18 * scale + x, 6.3 * scale + y),
                                       (18.5 * scale + x, 7 * scale + y),
                                       (18 * scale + x, 7.7 * scale + y),
                                       (16 * scale + x, 7.1 * scale + y)])
    polygon(surface, (255, 0, 0), [(16 * scale + x, 6.9 * scale + y),
                                   (18 * scale + x, 6.3 * scale + y),
                                   (18.5 * scale + x, 7 * scale + y),
                                   (18 * scale + x, 7.7 * scale + y),
                                   (16 * scale + x, 7.1 * scale + y)],
            width_of_line)
    line(surface, (255, 0, 0), (16 * scale + x, 7 * scale + y),
         (18.5 * scale + x, 7 * scale + y))


def gull_stomach(surface, x, y, scale, color, width_of_line):
    """
    draw gull's stomach
    x, y - coordinates of the upper left corner of whole picture
    scale - size of gull
    width_of_line - width of outline
    """
    ellipse(surface, color,
            (6 * scale + x, 8 * scale + y, 6 * scale, 2 * scale))
    arc(surface, Black, (6 * scale + x, 8 * scale + y, 6 * scale, 2 * scale),
        3.14, 6.28, width_of_line)


def gull_legs(surface, x, y, scale, color, width_of_line):
    """
    draw gull's legs
    x, y - coordinates of the upper left corner of whole picture
    scale - size of gull
    width_of_line - width of outline
    """
    polygon(surface, color, [(8 * scale + x, 10 * scale + y),
                             (8 * scale + x, 11 * scale + y),
                             (9 * scale + x, 13 * scale + y),
                             (12 * scale + x, 13 * scale + y),
                             (9 * scale + x, 12 * scale + y),
                             (9 * scale + x, 11 * scale + y),
                             (11 * scale + x, 12 * scale + y),
                             (13 * scale + x, 12 * scale + y),
                             (10 * scale + x, 11 * scale + y),
                             (10 * scale + x, 10 * scale + y)], width_of_line)


def gull_eye(surface, x, y, scale, color, eye_radius):
    """
    draw gull's eye
    x, y - coordinates of the upper left corner of whole picture
    scale - size of gull
    width_of_line - width of outline
    eye_radius - size of eyes
    """
    circle(surface, color, (15 * scale + x, 7 * scale + y), eye_radius)


def gull_anotherpart(surface, x, y, scale):
    """
    draw another part of gull
    x, y - coordinates of the upper left corner of whole picture
    scale - size of gull
    """
    polygon(surface, White, [(8 * scale + x, 10.2 * scale + y),
                             (10 * scale + x, 10.2 * scale + y),
                             (10 * scale + x, 9.9 * scale + y),
                             (8 * scale + x, 9.9 * scale + y),
                             (9 * scale + x, 9.9 * scale + y)])


def gull(x, y, scale, width_of_line, eye_radius, mirror):
    """
    x, y - coordinates of the upper left corner of whole picture
    scale - size of gull
    width_of_line - width of outline
    eye_radius - size of eyes
    mirror - reverse parameter (1 - reversed gull)
    """
    if mirror == 1:
        surface = pygame.Surface((x + 19 * scale, y + 14 * scale),
                                 pygame.SRCALPHA)
    else:
        surface = display

    gull_feet(surface, x, y, scale, Red, 0)
    gull_feet(surface, x, y, scale, Red2, width_of_line)

    gull_body(surface, x, y, scale, White, 0)
    gull_body(surface, x, y, scale, Black, width_of_line)

    gull_stomach(surface, x, y, scale, White, width_of_line)

    gull_beak(surface, x, y, scale, width_of_line)

    gull_head(surface, x, y, scale, width_of_line)

    gull_legs(surface, x, y, scale, White, 0)
    gull_legs(surface, x, y, scale, Black, width_of_line)

    gull_anotherpart(surface, x, y, scale)

    gull_eye(surface, x, y, scale, Black, eye_radius)

    if mirror == 1:
        surface = pygame.transform.flip(surface, True, False)
        display.blit(surface, (x, y))


def fish(scale, step_x, step_y, width_of_line, eye_radius, pupil_radius):
    """
    fish - background
    scale, step_x, step_y - size
    width_of_line - width of outline
    eye_radius - size of eyes
    pupil_radius - size of pupil
    """
    ellipse(display, (0, 240, 100),
            (3 * scale + step_x, 28 * scale + step_y, 4 * scale, 2 * scale))
    ellipse(display, (0, 100, 0),
            (3 * scale + step_x, 28 * scale + step_y, 4 * scale, 2 * scale),
            width_of_line)
    polygon(display, (100, 0, 100),
            [(1 * scale + step_x, 28 * scale + step_y),
             (1.5 * scale + step_x, 29 * scale + step_y),
             (1 * scale + step_x, 30 * scale + step_y),
             (3 * scale + step_x, 29 * scale + step_y)])
    polygon(display, (100, 0, 0),
            [(1 * scale + step_x, 28 * scale + step_y),
             (1.5 * scale + step_x, 29 * scale + step_y),
             (1 * scale + step_x, 30 * scale + step_y),
             (3 * scale + step_x, 29 * scale + step_y)], width_of_line)
    polygon(display, (100, 0, 100),
            ((5 * scale + step_x, 28 * scale + step_y),
             (5 * scale + step_x, 27 * scale + step_y),
             (3 * scale + step_x, 27 * scale + step_y),
             (4 * scale + step_x, 28 * scale + step_y)))
    polygon(display, (100, 0, 0),
            ((5 * scale + step_x, 28 * scale + step_y),
             (5 * scale + step_x, 27 * scale + step_y),
             (3 * scale + step_x, 27 * scale + step_y),
             (4 * scale + step_x, 28 * scale + step_y)), width_of_line)
    ellipse(display, (100, 0, 100),
            (4.5 * scale + step_x, 27 * scale + step_y, 1 * scale, 1 * scale))
    arc(display, (100, 0, 0),
        (4.5 * scale + step_x, 27 * scale + step_y, 1 * scale, 1 * scale),
        -1.57, 1.57, width_of_line)
    polygon(display, (100, 0, 100),
            [(5 * scale + step_x, 30 * scale + step_y),
             (6 * scale + step_x, 30 * scale + step_y),
             (6 * scale + step_x, 31 * scale + step_y)])
    polygon(display, (100, 0, 0), [(5 * scale + step_x, 30 * scale + step_y),
                                   (6 * scale + step_x, 30 * scale + step_y),
                                   (6 * scale + step_x, 31 * scale + step_y)],
            width_of_line)
    polygon(display, (100, 0, 100),
            [(3 * scale + step_x, 30 * scale + step_y),
             (4 * scale + step_x, 29.8 * scale + step_y),
             (3.8 * scale + step_x, 30.6 * scale + step_y),
             (3 * scale + step_x, 31 * scale + step_y)])
    polygon(display, (100, 0, 0),
            [(3 * scale + step_x, 30 * scale + step_y),
             (4 * scale + step_x, 29.8 * scale + step_y),
             (3.8 * scale + step_x, 30.6 * scale + step_y),
             (3 * scale + step_x, 31 * scale + step_y)], width_of_line)
    circle(display, (0, 0, 240),
           (6 * scale + step_x, 29 * scale + step_y), eye_radius)
    circle(display, (0, 0, 0),
           (6 * scale + step_x, 29 * scale + step_y), pupil_radius)
    ellipse(display, (255, 255, 255),
            (5.7 * scale + step_x, 28.7 * scale + step_y,
             pupil_radius * 0.7, pupil_radius * 0.5))


sky()
all_birds()
fish(25, 0, 0, 2, 10, 6)
fish(20, 350, 90, 2, 10, 6)
fish(10, 270, 230, 2, 4, 2)
gull(0, 320, 17, 1, 3, 0)
gull(150, 270, 5, 1, 1, 0)
gull(280, 120, 12, 1, 2, 1)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
