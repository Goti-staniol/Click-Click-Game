from random import randint

from pygame import *

from src.models import Target, MissClick, Record, Score


init()
font.init()

FPS = 30
clock = time.Clock()
window = display.get_surface()

targets = []
spawn_delay = randint(30, 50)
count = 0
miss_count = 3

miss = MissClick((5, 15), 30, 'Miss: 3', None)


def restart_game() -> None:
    global miss_count, count, targets
    targets.clear()
    count = 0
    miss_count = 3
    miss.update_miss(3)

def run_game(status=True) -> None:
    global count, spawn_delay, miss_count
    while status:
        window.fill((0, 0, 0))
        miss.draw()

        count += 1

        if miss_count <= 0:
            restart_game()

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
                    else:
                        miss_count -= 1
                        miss.update_miss(miss_count)

        for target in targets[:]:
            target.draw()
            target.update(targets)

        display.update()
        clock.tick(FPS)