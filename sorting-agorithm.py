import pygame
import random

pygame.init()

class ColorInformation:
    BLACK = 0, 0, 0
    SOFTWHITE = 250, 250, 250
    BLUE = 0, 0, 255
    GREEN = 0, 255, 0
    LIGHTGREY = 192, 192, 192
    GREY = 110, 110, 110
    PADDINGPIX = 200
    FONT = pygame.font.SysFont('dejavusansmono', 20)

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
    keycontrols = color_info.FONT.render("Hit the SPACEBAR to start sorting | R - Reset", 1, color_info.BLACK)
    color_info.window.blit(keycontrols, (5, 5))
    draw_list(color_info)
    pygame.display.update()

def draw_list(color_info, color_position=dict(), clear_plot=False):
    lst = color_info.unsorted_list

    if clear_plot:
        pygame.draw.rect(color_info.window, color_info.SOFTWHITE, (0, color_info.PADDINGPIX, color_info.height * 2, color_info.width * 2))

    for i, val in enumerate(lst):
        x_point = color_info.start_cor_x + i * color_info.bar_width
        y_point = color_info.height - (val - color_info.min) * color_info.bar_height

        color = color_info.GREY
        if i % 2 == 1:
            color = color_info.LIGHTGREY

        if i in color_position:
            color = color_position[i]

        pygame.draw.rect(color_info.window, color, (x_point, y_point, color_info.bar_width, color_info.height))

    if clear_plot:
        pygame.display.update()



def main():
    run = True
    clock = pygame.time.Clock()

    n = 30
    min_val = 0
    max_val = 100

    unsorted_list = generate_random_list(n, min_val, max_val)
    color_info = ColorInformation(800, 600, unsorted_list)

    currently_sorting = False

    current_algorithm = bubble_sort
    current_algorithm_name = "bubble sort"
    current_generator = None

    while run:
        clock.tick(60)

        if currently_sorting:
            try:
                    next(current_generator)
            except StopIteration:
                    sorting = False

        else:
            draw(color_info)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_SPACE:
                currently_sorting = True
                current_generator = current_algorithm(color_info)

            if event.key == pygame.K_r:
                unsorted_list = generate_random_list(n, min_val, max_val)
                color_info.set_list(unsorted_list)
                currently_sorting = False

    pygame.quit()

def bubble_sort(color_info):
    unsorted_list = color_info.unsorted_list
    print("im called bitch")

    for i in range(len(unsorted_list) - 1):
        for j in range(len(unsorted_list) - i - 1):
            val1 = unsorted_list[j]
            val2 = unsorted_list[j + 1]

            if val1 > val2:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
                draw_list(color_info, {j: color_info.BLUE, j + 1: color_info.GREEN}, True)
                yield True

    return unsorted_list




if __name__ == "__main__":
    main()
