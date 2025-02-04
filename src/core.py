from random import randint

from pygame import *

from src.models import Target


init()
FPS = 30
clock = time.Clock()
window = display.get_surface()

targets = []
spawn_delay = randint(30, 50)
count = 0


def run_game(status=True) -> None:
    global count, spawn_delay
    while status:
        window.fill((0, 0, 0))
        count += 1
        if count >= spawn_delay:
            new_target = Target()
            can_spawn = True

            for target in targets:
                if new_target.rect.colliderect(target.rect):
                    can_spawn = False

            if can_spawn:
                targets.append(new_target)
                count = 0
                spawn_delay = randint(30, 50)

        for e in event.get():
            if e.type == QUIT:
                status = False

            for target in targets:
                if e.type == MOUSEBUTTONDOWN and e.button == 1:
                    if target.rect.collidepoint(e.pos):
                        targets.remove(target)

        for target in targets:
            target.draw()

        display.update()
        clock.tick(FPS)