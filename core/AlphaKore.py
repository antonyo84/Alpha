# coding=utf-8
from Randomizer import get_random
import data.object_data
import base.template_constants as template
from names import get_name
from base.template_constants import *


class Loops:
    LOOP_FROM = 0
    LOOP_TO = 1

    WHILE = 0
    FOR = 1


class AlphaKore(object):
    MIN_METHODS = 1
    MAX_METHODS = 3

    MIN_LOOPS = 0
    MAX_LOOPS = 4

    MIN_ACTIONS = 1
    MAX_ACTIONS = 6

    def __init__(self):
        pass

    def generate_child_object(self, parent_object):

        new_methods_to_generate = get_random(AlphaKore.MIN_METHODS, AlphaKore.MAX_METHODS)
        new_methods = ""
        generated_methods = 0
        loaded_template = TEMPLATE

        loaded_template = loaded_template.replace(PARENT, parent_object.get_data()["name"])
        loaded_template = loaded_template.replace(CLASS_NAME, get_name())
        loaded_template = loaded_template.replace(LOCAL_OBJECTS, 'pass')
        loaded_template = loaded_template.replace(INIT_ARGS, "")
        loaded_template = loaded_template.replace(IMPORTS, "")

        while generated_methods < new_methods_to_generate:
            method = self.generate_method()
            new_methods = "{0}{1}".format(new_methods, method)
            generated_methods += 1

        loaded_template = loaded_template.replace(METHODS, new_methods)

        return loaded_template

    def generate_single_action(self, usable_objects=None, usable_methods=None):
        # TODO Hay que desarrollar esto (está así para pruebas)
        return "print ('Hola ke ase!')"

    def generate_actions(self, usable_objects=None, usable_methods=None):
        result = ""
        actions_to_generate = get_random(AlphaKore.MIN_ACTIONS, AlphaKore.MAX_ACTIONS)
        generated_actions = 0

        while generated_actions < actions_to_generate:
            result = "{0}\n{1}".format(result, self.generate_single_action(usable_objects, usable_methods))
            generated_actions += 1
        return result

    def generate_loop(self, usable_objects=None, usable_methods=None):
        pass

    def generate_method(self, usable_objects=None, usable_methods=None):
        result = "\tdef {0}():\n".format(get_name())
        loops_to_generate = get_random(AlphaKore.MIN_LOOPS, AlphaKore.MAX_LOOPS)
        # TODO De momento no vamos a generar loops
        loops_to_generate = 0
        if loops_to_generate == 0:
            for action in self.generate_actions(usable_objects, usable_methods).split("\n"):
                if action is not None and len(action) > 0:
                    result = "{0}\t\t{1}\n".format(result, action)
        else:
            generated_loops = 0

            while generated_loops < loops_to_generate:
                if generated_loops > 0:
                    result = "{0}\n\t".format(result)

                actions_in_loop = self.generate_actions(usable_objects, usable_methods)
                for generated_action in actions_in_loop.split("\n"):
                    if generated_action is not None and len(generated_action) > 0:
                        result = "{0}\t\t\t{1}\n".format(result, generated_action)

                generated_loops += 1

        result = "{0}\n".format(result)
        return result
