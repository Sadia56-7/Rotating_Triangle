import pygame
import math


pygame.init()
Width= 700
Height = 700
NUM_TRIS = 90
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((Height,Width))
pygame.display.set_caption("Rotating Triangles")


# Function to map a value from one range to another
def map_value(value, start1, stop1, start2, stop2):
    return start2 + (stop2 - start2) * ((value - start1) / (stop1 - start1))


# Function to draw a triangle
def draw_triangle(surface, color, vertices):
    pygame.draw.polygon(surface, color, vertices, 1)  # 1 for no fill, just the outline


# Main loop
running = True
clock = pygame.time.Clock()
t = 0  # Time


def setup():
    global screen
    screen.fill(BLACK)


def draw():
    global t
    screen.fill(BLACK)

    center_x, center_y = Width / 2, Height / 2
    mouse_x, mouse_y = pygame.mouse.get_pos()
    num_tris = int(map_value(mouse_x, 0, Width, 3, 120))

    for i in range(num_tris):
        angle = math.radians(360 / num_tris)
        offset = map_value(mouse_x, 0, Height, 1, 10)
        current_angle = math.radians(t + offset * i * 360 / num_tris)

        # Rotate
        rotated_x = 200 * math.cos(current_angle) - 0 * math.sin(current_angle)
        rotated_y = 200 * math.sin(current_angle) + 0 * math.cos(current_angle)

        # Translate
        tri_x = center_x + rotated_x
        tri_y = center_y + rotated_y

        # Compute the vertices of the triangle
        l = 100
        vertices = [
            (tri_x, tri_y - l),
            (tri_x - l * math.sqrt(3) / 2, tri_y + l / 2),
            (tri_x + l * math.sqrt(3) / 2, tri_y + l / 2)
        ]

        # Draw the triangle
        color = (3 * i % 256, 255, 255)
        draw_triangle(screen, color, vertices)

    t += 0.5
    pygame.display.flip()


setup()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
