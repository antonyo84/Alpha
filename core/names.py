from Randomizer import get_random

PARTS = ["get", "set", "miau", "destroy", "kill", "create", "enjoy", "smoke", "drink", "eat", "love", "hate", "gang",
         "crew", "style", "the", "or", "smack", "jump"]


def get_name(min=2, max=6):
    method_name_parts = get_random(min, max)
    obtained_parts = 0
    method_name = ""
    while obtained_parts < method_name_parts:
        new_part = PARTS[get_random(1, len(PARTS) - 1)]
        if obtained_parts == 0:
            method_name = new_part
        else:
            method_name = "{0}_{1}".format(method_name, new_part)
        obtained_parts += 1

    return method_name
