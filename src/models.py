from typing import Tuple
from random import randint

from pygame import *


W, H = 700, 500
window = display.set_mode((W, H))
display.set_caption('CPG')


class Target(sprite.Sprite):
    def __init__(self, img: str = 'src/images/target.png'):
        super().__init__()
        random_size = randint(50, 100)
        size = (random_size, random_size)
        self.img = transform.scale(
            image.load(img),
            size
        )
        self.rect = self.img.get_rect()
        self.rect.x, self.rect.y = randint(50, 590), randint(50, 380)
        self.count = 0

    def draw(self):
        window.blit(self.img, (self.rect.x, self.rect.y))


class Text:
    def __init__(
            self,
            position: Tuple[int, int],
            size: int,
            text: str,
            font_txt: str = None,
            color_txt: Tuple[int, int, int] = (0, 0, 0)
    ):
        self.position = position
        self.font_txt = font.Font(font_txt, size)
        self.color_txt = color_txt
        self.text = self.font_txt.render(text, True, color_txt)

    def update_text(self, new_text: str):
        self.text = self.font_txt.render(new_text, True, self.color_txt)

    def draw(self):
        window.blit(self.text, self.position)


class MissClick(Text):
    def update_miss(self, miss: int | str):
        super().update_text(f'Miss: {miss}')


class Score(Text):
    def update_score(self, new_score: int | str):
        super().update_text(f'Score: {new_score}')


class Record(Text):
    def update_record(self, new_record: int):
        super().update_text(f'Record: {new_record}')

