def test_item_creation():
    from base.base_element import BaseElement
    item = BaseElement()
    print(item.get_methods())


def file_writing():
    from files.files_helper import FilesHelper
    FilesHelper.write_file("def testing_method():\n\tprint('hello test!')\n\ntesting_method()", "test_file.py")


def write_base_element():
    base_element_text = ''
    base_element_file = open('base/base_element.py', 'r')
    for line in base_element_file.readlines():
        base_element_text += '{0}{1}'.format(line, '\n')

    from files.files_helper import FilesHelper
    FilesHelper.write_file(base_element_text, 'base_element_copy.py')

write_base_element()