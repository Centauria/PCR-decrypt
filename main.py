# -*- coding: utf-8 -*-
import argparse
import base64

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    args = parser.parse_args()
    
    with open(args.input) as f:
        b = base64.b64decode(f.read())
        print(b)
