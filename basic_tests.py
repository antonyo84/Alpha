def test_function(function):
    def func_wrapper(*args, **kwargs):
        try:
            function_result = function(*args, **kwargs)
            print("\n\nLa funcion {0} ha pasado los test correctamente\n\n__________".format(function))
            return function_result
        except Exception as e:
            print("\n\nLa funcion {0} no ha pasado los test\n\n__________\n\nException:\n\n{1}\n\n__________".format(function,e))
    return func_wrapper


@test_function
def test_item_creation():
    from base.base_element import BaseElement
    item = BaseElement()
    print(item.get_methods())


@test_function
def file_writing():
    from files.files_helper import FilesHelper
    FilesHelper.write_python_file("def testing_method():\n\tprint('hello test!')\n\ntesting_method()", "test_file.py")


@test_function
def write_base_element():
    base_element_text = ''
    base_element_file = open('base/base_element.py', 'r')
    for line in base_element_file.readlines():
        base_element_text += '{0}{1}'.format(line, '\n')

    from files.files_helper import FilesHelper
    FilesHelper.write_python_file(base_element_text, 'base_element_copy.py')


@test_function
def test_randoms():
    from core.Randomizer import get_random
    print('first get_random_tests')
    print(get_random(0, 12))
    print(get_random(3, 7))
    print(get_random(9, 16))
    print(get_random())
    print('second get_random_tests')
    print(get_random(0, 12))
    print(get_random(3, 7))
    print(get_random(9, 16))
    print(get_random())

test_randoms()