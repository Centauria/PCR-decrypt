# -*- coding: utf-8 -*-
import argparse
import os

from process.shallow import debase

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    parser.add_argument('output')
    args = parser.parse_args()

    b_dir = os.path.join(args.output, 'bin')
    k_dir = os.path.join(args.output, 'key')
    os.makedirs(b_dir, exist_ok=True)
    os.makedirs(k_dir, exist_ok=True)

    index = 1
    for current, dirs, files in os.walk(args.input):
        for file in files:
            current_file = os.path.join(current, file)
            with open(current_file, encoding='ascii') as f:
                print(f'Processing file {index:05} {current_file} ...', end='')
                try:
                    s = f.read()
                except UnicodeDecodeError:
                    print('Failed')
                    continue
                if os.linesep in s or '{' in s:
                    print('Failed')
                    continue
                b, k = debase(s)
                with open(os.path.join(b_dir, f'{index:05}.b'), 'wb') as w:
                    w.write(b)
                with open(os.path.join(k_dir, f'{index:05}.key'), 'wb') as w:
                    w.write(k)
                print('OK')
                index += 1
