#
#
#
#

import sys
sys.path.append('libs')

from console import *
from args import *
from fuckimport import *
from pickle_func import *

console_term = console_term()
game_args = game_args()
fuck_import = fuck_import()

if (game_args.args.source.split('.')[1] == 'list'):
    fuck_import.read(game_args.args.source.split('.')[0])
    fuck_import.build()

elif (game_args.args.source.split('.')[1] == 'pkl'):
    fuck_import.read_pack(game_args.args.source.split('.')[0])

else:
    console_term.print('Bad source argument', 3)

CODE = fuck_import.get_code()

if (game_args.args.pack and CODE):
    fuck_import.pack(game_args.args.source.split('.')[0])

else:
    if (CODE):
        console_term.run_terminal()
        exec(CODE)
