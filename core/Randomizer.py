import random

max_default_random = 10


def get_random(minimum=1, maximum=max_default_random):
    return random.randint(minimum, maximum)


def do_something():
    use_pairs = get_random(1, 2) == 2
    return get_random(1, 2) == 2 if use_pairs else 1
