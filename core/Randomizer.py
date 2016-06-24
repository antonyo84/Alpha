import random

max_default_random = 10

def get_random(minimum=1, maximum=max_default_random):
    return random.randint(minimum, maximum)
