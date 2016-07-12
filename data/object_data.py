class ObjectData:
    def __init__(self, object_name, inheritance_level, object_string, objects_in_object=None,
                 methods_in_object=None, parameters=None):
        self.name = object_name
        self.level = inheritance_level
        self.objects_in_object = objects_in_object
        self.methods_in_object = methods_in_object
        self.object_string = object_string
        self.parameters = parameters
        self.need_parameters = "YES" if parameters is not None else "NO"

    def get_data(self):
        return {"name": self.name,
                "level": self.level,
                "objects_in_object": self.objects_in_object,
                "methods_in_object": self.methods_in_object,
                "need_parameters": self.need_parameters,
                "parameters": self.parameters}

    def object_string(self):
        return self.object_string


class MethodData(object, ObjectData):
    def get_data(self):
        parent_data = super(MethodData, self).get_data()
        parent_data["parameters"] = self.parameters
        return parent_data


class PrimitiveData(object, ObjectData):
    def __init__(self, object_name, object_string, primitive_type):
        ObjectData.__init__(self, object_name, -1, object_string)

    def get_data(self):
        parent_data = super(PrimitiveData, self).get_data()
        parent_data["primitive_type"] = self.primitive_type
