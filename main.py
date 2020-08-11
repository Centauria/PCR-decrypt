# -*- coding: utf-8 -*-
import argparse
from process import info

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    args = parser.parse_args()
    
    with open(args.input) as f:
        info(f.read())
