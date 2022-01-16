import pygame
import random

pygame.init()

class ColorInformation:
    BLACK = 0, 0, 0
    SOFTWHITE = 250, 250, 250
    RED = 255, 0, 0
    GREEN = 0, 255, 0
    LIGHTGREY = 192, 192, 192
    GREY = 110, 110, 110
    PADDINGPIX = 200

    def __init__(self, width, height, unsorted_list):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("SORTING ALGORITHM VISUALISER")
        self.set_list(unsorted_list)

    def set_list(self, unsorted_list):
        self.unsorted_list = unsorted_list
        self.max = max(unsorted_list)
        self.min = min(unsorted_list)

        self.bar_width = round((self.width - self.PADDINGPIX) / len(unsorted_list))
        self.bar_height = round((self.height - self.PADDINGPIX) / (self.max - self.min))
        self.start_cor_x = self.PADDINGPIX // 2

def generate_random_list(len, min_val, max_val):
    lst = []
    for _ in range(len):
        lst.append(random.randint(min_val, max_val))

    return lst

def draw(color_info):
    color_info.window.fill(color_info.SOFTWHITE)
    drawList(color_info)
    pygame.display.update()

def drawList(color_info):
    lst = color_info.unsorted_list
    for i, val in enumerate(lst):
        x_point = color_info.start_cor_x + i * color_info.bar_width
        y_point = color_info.height - (val - color_info.min) * color_info.bar_height

        color = color_info.GREY
        if i % 2 == 1:
            color = color_info.LIGHTGREY

        pygame.draw.rect(color_info.window, color, (x_point, y_point, color_info.bar_width, color_info.height))



def main():
    run = 1
    clock = pygame.time.Clock()

    n = 30
    min_val = 0
    max_val = 100

    unsorted_list = generate_random_list(n, min_val, max_val)
    color_info = ColorInformation(800, 600, unsorted_list)

    while run:
        clock.tick(60)

        draw(color_info)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = 0

    pygame.quit()

if __name__ == "__main__":
    main()
