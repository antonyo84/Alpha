from method import ElementMethod


class BaseElement:
    def __init__(self):
        self.methods = [method for method in dir(self) if callable(getattr(self, method))]

    def get_methods(self):
        return self.methods

    def get_method_info(self, method_name):
        raise NotImplementedError

    def get_properties(self):
        raise NotImplementedError

    def get_inheritance_level(self):
        return -1
