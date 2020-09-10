# -*- coding: utf-8 -*-
import argparse
from process import info, try_cipher

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    args = parser.parse_args()
    
    with open(args.input) as f:
        s = f.read()
        info(s)
        try_cipher(s)
