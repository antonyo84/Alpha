from base_element import BaseElement


class Element(BaseElement):
    def get_properties(self):
        pass

    def get_method_info(self, method_name):
        pass

    def get_inheritance_level(self):
        return super(self).get_inheritance_level() + 1
