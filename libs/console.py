#
#
#
#

import os
import threading
import termcolor

#def print_char(x, y, char):
#    print("\033[" + str(y) + ";" + str(x) + "H" + char)

class console_term():
    def __init__(self):
        super().__init__()

        os.system('color')

        self.type_color = ['white', 'green', 'yellow', 'red']

        self.promt = ""

        self.console = threading.Thread(target=self.input_terminal)

    #

    def run_terminal(self):
        self.console.start()

    def input_terminal(self):
        while True:
            command = input(self.promt)
            self.exec(command)

    def exec(self, command):
        try:
            exec(command)

        except Exception as e:
            self.print(e, 3)

    def print(self, text, type=0):
        termcolor.cprint(text, self.type_color[type])
