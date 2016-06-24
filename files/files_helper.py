class FilesHelper:
    def __init__(self):
        pass

    @staticmethod
    def write_file(content, file_name, file_path=None):
        new_file = open(file_name, 'w')
        first_line = True
        for line in content.split('\n'):
            if not first_line:
                line = "{0}{1}".format("\n", line)
            else:
                first_line = False
            new_file.writelines(line)

        new_file.close()
