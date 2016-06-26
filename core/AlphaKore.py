from Randomizer import get_random
import data.object_data


class AlphaKore(object):
    def __init__(self):
        pass

    def generate_child_object(self, parent_object):
        new_methods_to_generate = get_random(1, 3)
        new_content = ""
        generated_methods = 0
        while generated_methods < new_methods_to_generate:
            new_content += self.generate_method()
            generated_methods += 1

    def generate_method(self, usable_objects=None, usable_methods=None):
        result = ""

        return result
