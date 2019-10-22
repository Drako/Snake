#!/usr/bin/env python3

import pygame

from controllers import KeyboardController, KeyMap
from objects import Goal, Score, Snake, Field
from util import random_rect, Rect, random_direction, random_point, Point
from util.collisions import rect_contains_point
from util.colors import BLACK, WHITE

SIZE = WIDTH, HEIGHT = 800, 600


def generate_goal_area(*, snake: Snake, field: Field) -> Rect:
    collision = True
    possible_goal: Rect = Rect(x=0, y=0, w=0, h=0)
    while collision:
        possible_goal = random_rect(size=9, area=field.client_area())
        collision = False
        for point in snake:
            if rect_contains_point(possible_goal, point):
                collision = True
    return possible_goal


def check_collisions(snake: Snake, screen: pygame.Surface, goal: Goal, field: Field) -> bool:
    head = snake.head()
    if screen.get_at(head) == WHITE:
        if head in goal:
            goal.move_to(generate_goal_area(snake=snake, field=field))
            snake.grow()
        else:
            print(f'Game over! Your score: {len(snake)}')
            return False
    return True


def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()

    noto_sans = pygame.font.Font('NotoSans-Regular.ttf', 12)

    field = Field(area=Rect(x=10, y=50, w=WIDTH - 20, h=HEIGHT - 60))
    snake = Snake(starting_point=random_point(offset=100, area=field.client_area()))
    score = Score(font=noto_sans, position=Point(x=10, y=10))
    goal = Goal(area=generate_goal_area(snake=snake, field=field))
    controller = KeyboardController(snake=snake, start_direction=random_direction(), key_map=KeyMap(
        up=pygame.K_UP, down=pygame.K_DOWN, left=pygame.K_LEFT, right=pygame.K_RIGHT
        # up=pygame.K_w, down=pygame.K_s, left=pygame.K_a, right=pygame.K_d
    ))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            controller.handle_event(event)

        if not running:
            break

        score.update(score=len(snake))

        screen.fill(BLACK)
        for go in [field, snake, score, goal]:
            go.draw_to(screen)
        pygame.display.flip()

        controller.update()
        running = check_collisions(snake, screen, goal, field)
        clock.tick(120)

    pygame.quit()


if __name__ == '__main__':
    main()
