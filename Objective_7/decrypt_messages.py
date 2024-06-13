# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 19:36:53 2024

@author: janma
"""

import pandas as pd
import base64
from itertools import cycle
from io import BytesIO

def xore(data, key):
    return bytes(a ^ b for a, b in zip(data, cycle(key)))


input_dir = r'./input/'
input_file = r'./messages.txt'

messages = pd.read_csv(input_file, sep='\t')


for index, row in messages.iterrows():
    base64str = base64.b64decode(row['message'])
    
    with BytesIO(base64str) as f:
        decrypted = xore(f.read(), b'ULRIEKE')
        print(decrypted)
