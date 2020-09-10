# -*- coding: utf-8 -*-
import argparse
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    args = parser.parse_args()

    key_dict = dict()
    for kf in os.listdir(args.input):
        kf = os.path.join(args.input, kf)
        with open(kf) as f:
            k = f.read()
        if k not in key_dict.keys():
            print(f'{k} not in the dict')
            key_dict[k] = kf
        else:
            print(f'{k} collide with {key_dict[k]}')
