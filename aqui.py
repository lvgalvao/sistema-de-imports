a = 1
b = 2

from dotenv import load_dotenv
import os
import pprint

AMBIENTE = os.getenv('AMBIENTE')

def soma(x,y):
    return x + y

import importlib

if AMBIENTE == 'PROD':
    f = pprint.pprint(importlib.import_module('pathlib').Path().resolve())
else:
    f = importlib.import_module('dotenv')