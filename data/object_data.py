class ObjectData:
    def __init__(self, object_name, object_content, inheritance_level, objects_in_object=None, methods_in_object=None):
        self.name = object_name
        self.content = object_content
        self.level = inheritance_level
        self.objects_in_object = objects_in_object
        self.methods_in_object = methods_in_object

    def get_data(self):
        return {"name": self.name,
                "content": self.content,
                "level": self.level,
                "objects_in_object": self.objects_in_object,
                "methods_in_object": self.methods_in_object}
