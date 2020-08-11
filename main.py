# -*- coding: utf-8 -*-
import argparse
import base64
import hashlib

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    args = parser.parse_args()
    
    with open(args.input) as f:
        b = base64.b64decode(f.read())
        print(f'Decode length: {len(b)}')
        print(f'Last 32 bytes: {b[-32:]}')
        sh = hashlib.md5()
        sh.update(b[:-32])
        print(f'MD5 without last 32 bytes: {sh.hexdigest()}')
