#
#
#
#

import os
import pickle
import hashlib

def save_obj(obj, name):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)

def get_hash(text):
    return hashlib.md5(text.encode('utf-8')).digest()

# класс для хранения всего кода в файл
class file_code():
    def __init__(self):
        self.files = []
        self.code = ''
        self.hash = ''

class fuck_import():
    def __init__(self, path='objects'):

        self.path = path         # дтректория где будут лежать файлы
        self.main_file_name = '' # название основного списка

        self.code = ''  # здесь будет храниться код после сборки (build)
        self.files = [] # здесь будет храниться список файлов и размер каждого файла в строках

    # чтение списка файлов проекта
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
                            (name + '.list').replace( # название и путь у файлу
                                name.split('/')[len(name.split('/'))-1] + '.list',
                                file_name
                            ),
                            0 # количество строк в файле (по умалочанию 0)
                        ]
                    )

    # сборка всех файлов из списка в код
    def build(self):
        self.code = ''
        for file_code_name in self.files:
            try:
                file_code_buf = open(self.path + '/' + file_code_name[0], 'r', encoding="utf-8").read() + '\n'
                file_code_name[1] = len(file_code_buf.split('\n'))
                self.code += file_code_buf

            except:
                print('gg')

    # функция для сохранения всего кода в 1 собранный файл
    def pack(self, name):
        file_code_buf = file_code()
        file_code_buf.files = self.files
        file_code_buf.code = self.code
        file_code_buf.hash = get_hash(self.code)

        save_obj(file_code_buf, name)

    # функция для чтения собранного файла
    def read_pack(self, name):
        file_code_buf = load_obj(name)

        if (get_hash(file_code_buf.code) == file_code_buf.hash):
            self.code = file_code_buf.code
            self.files = file_code_buf.files

            return True
        else:
            print('error hash')
            return False

    # возврат кода
    def get_code(self):
        return self.code
