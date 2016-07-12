# coding=utf-8
from Randomizer import get_random
import data.object_data
import base.template_constants as template
import alpha_logging.AlphaLogger as AlphaLogger
from names import get_name
from base.template_constants import *


class Loops:
    LOOP_FROM = 0
    LOOP_TO = 1

    WHILE = 0
    FOR = 1

class ActionsCode:
    PRINT = 1
    ADD = 2
    SUBSTRACT = 3
    

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
        new_class_name = get_name()
        new_methods_to_generate = get_random(AlphaKore.MIN_METHODS, AlphaKore.MAX_METHODS)
        new_methods = ""
        generated_names = 0
        loaded_template = TEMPLATE
        AlphaLogger.AlphaLogger.log("Se empieza a generar la clase {0}, con {1} métodos crear".format(new_class_name, new_methods_to_generate))
        loaded_template = loaded_template.replace(PARENT, parent_object.get_data()["name"])
        loaded_template = loaded_template.replace(CLASS_NAME, new_class_name)
        loaded_template = loaded_template.replace(LOCAL_OBJECTS, 'pass')
        loaded_template = loaded_template.replace(INIT_ARGS, "")
        loaded_template = loaded_template.replace(IMPORTS, "")

        method_names = []
        while generated_names < new_methods_to_generate:
            method_names.append(get_name())
            generated_names += 1

        for method_name in method_names:
            method = self.generate_method(method_name, usable_methods=[usable_method for usable_method in method_names if usable_method != method_name])
            new_methods = "{0}{1}".format(new_methods, method)

        loaded_template = loaded_template.replace(METHODS, new_methods)

        return loaded_template

    def generate_single_action(self, usable_objects=None, usable_methods=None):
        """
        
        :param usable_objects: collection of  {"name": name,
                                                "content": content,
                                                "level": level,
                                                "objects_in_object": objects_in_object of same kind of this(usable_object),
                                                "methods_in_object": methods_in_object} 
        :param usable_methods: Array of methods
        :return: a single action string of type of ActionsCode
        """
        # TODO Hay que desarrollar esto (está así para pruebas)
        action_code_to_create = get_random(1, 5)
        action_to_return = ""
        if action_code_to_create == ActionsCode.PRINT:
            action_to_return = "print (PRINT_TAG)"
            
            options_to_print = []
            if usable_objects is not None:
                for object in usable_objects:
                    options_to_print.append(object)

            if usable_methods is not None:
                for method in usable_methods:
                    options_to_print.append(method)

        elif action_code_to_create == ActionsCode.ADD:
            pass
        elif action_code_to_create == ActionsCode.SUBSTRACT:
            pass
        elif action_code_to_create == 4:
            pass
        elif action_code_to_create == 5:
            pass

        return action_to_return

    def generate_actions(self, usable_objects=None, usable_methods=None):
        """
        Éste método genera 'acciones' diversas con objetos, variables o métodos aleatoriamente
        :param usable_objects: Objetos que pueden ser utilizados en las acciones
        :param usable_methods: Métodos de la propia instancia que pueden ser llamados
        :return: Cadena de texto con las acciones tabuladas
        """
        result = ""
        actions_to_generate = get_random(AlphaKore.MIN_ACTIONS, AlphaKore.MAX_ACTIONS)
        generated_actions = 0

        while generated_actions < actions_to_generate:
            # Incluimos un salto de linea a continuacion del resultado (excepto la primera vez)
            if generated_actions > 0:
                result = "{0}\n{1}".format(result, self.generate_single_action(usable_objects, usable_methods))
            generated_actions += 1
        return result

    def generate_conditionals(self, usable_objects=None, usable_methods=None):
        """
        Éste método genera 'condiciones' diversas tipo if...else
        :param usable_objects: Objetos que pueden ser utilizados en las condiciones
        :param usable_methods: Métodos de la propia instancia que pueden ser llamados
        :return: Cadena de texto con las condiciones tabuladas
            """
        pass

    def generate_loop(self, usable_objects=None, usable_methods=None):
        """
        Éste método genera 'iteraciones' diversas tipo for ... in, while
        :param usable_objects: Objetos que pueden ser utilizados en las iteraciones
        :param usable_methods: Métodos de la propia instancia que pueden ser llamados
        :return: Cadena de texto con las iteraciones tabuladas
            """
        pass

    def generate_method(self, method_name, usable_objects=None, usable_methods=None):
        """
        Éste método genera 'métodos' completos con iteraciones, condiciones y acciones
        :param usable_objects: Objetos que pueden ser utilizados en las acciones
        :param usable_methods: Métodos de la propia instancia que pueden ser llamados
        :return: Cadena de texto con el método completo correctamente tabulado
            """
        result = "\tdef {0}():\n".format(method_name)
        things_to_do = get_random(AlphaKore.MIN_LOOPS, AlphaKore.MAX_LOOPS)
        AlphaLogger.AlphaLogger.log("En el método {0}, tenemos {1} cosas que crear".format(method_name, things_to_do))
        # TODO De momento no vamos a generar loops
        things_to_do = 0

        if things_to_do == 0:
            for action in self.generate_actions(usable_objects, usable_methods).split("\n"):
                if action is not None and len(action) > 0:
                    result = "{0}\t\t{1}\n".format(result, action)
        else:
            generated_loops = 0

            while generated_loops < things_to_do:
                if generated_loops > 0:
                    result = "{0}\n\t".format(result)

                actions_in_loop = self.generate_actions(usable_objects, usable_methods)
                for generated_action in actions_in_loop.split("\n"):
                    if generated_action is not None and len(generated_action) > 0:
                        result = "{0}\t\t\t{1}\n".format(result, generated_action)

                generated_loops += 1

        result = "{0}\n".format(result)
        return result
