# -*- coding: utf-8 -*-
import os
import argparse

from process import info

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    args = parser.parse_args()
    
    for obj in os.walk(args.input):
        current, dirs, files = obj
        for file in files:
            file_path = os.path.join(current, file)
            print(f'Processing file {file_path}')
            with open(file_path, encoding='utf-8') as f:
                s = f.read()
                info(s)
