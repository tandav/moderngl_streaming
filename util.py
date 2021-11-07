import random
import string

import config


def random_xy():
    return random.randrange(config.frame_width), random.randrange(config.frame_height)


def random_text(words=tuple(''.join(random.choices(string.ascii_letters, k=random.randint(1, 15))) for _ in range(200))):
    return random.choice(words)


def random_color():
    return random.randrange(255), random.randrange(255), random.randrange(255)
