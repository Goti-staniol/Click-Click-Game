from typing import Tuple, Optional, Union
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
        self.time_of_remove = randint(50, 80)
        self.count = 0

    def update(self, targets: list):
        self.count += 1
        if self.count >= self.time_of_remove:
            targets.remove(self)

    def draw(self):
        window.blit(self.img, (self.rect.x, self.rect.y))


class Text:
    def __init__(
            self,
            position: Tuple[int, int],
            size: int,
            text: str,
            font_txt: Optional[str],
            color_txt: Tuple[int, int, int] = (255, 255, 255)
    ):
        self.position = position
        self.font = font.Font(font_txt, size)
        self.color_txt = color_txt
        self.text = self.font.render(text, True, color_txt)

    def update_text(self, new_text: str):
        self.text = self.font.render(new_text, True, self.color_txt)

    def draw(self):
        window.blit(self.text, self.position)


class MissClick(Text):
    def update_miss(self, miss: Union[int, str]):
        super().update_text(f'Miss: {miss}')


class Score(Text):
    def update_score(self, new_score: Union[int, str]):
        super().update_text(f'Score: {new_score}')


class Record(Text):
    def update_record(self, new_record: Union[int, str]):
        super().update_text(f'Record: {new_record}')

