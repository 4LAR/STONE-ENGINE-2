#
#
#
#

import os
import pickle

class fuck_import():
    def __init__(self, path='objects'):

        self.path = path
        self.main_file_name = ''

        self.code = ''
        self.files = []

    def read(self, name='objects'):
        file_objects = (
            open(self.path + '/' + name + '.list', 'r', encoding="utf-8").read()
        ).split('\n')

        for file_name in file_objects:
            if (len(file_name) > 0):
                if (file_name.split('.')[1] == 'list'):
                    self.read(file_name.split('.')[0])
                else:
                    self.files.append(
                        [
                            file_name,
                            0
                        ]
                    )

    def get_code(self):
        return self.code
