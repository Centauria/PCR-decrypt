# -*- coding: utf-8 -*-
import argparse

from Crypto.Cipher import AES

from process.shallow import str2int2bytes

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    parser.add_argument('key')
    parser.add_argument('output')
    args = parser.parse_args()

    with open(args.input) as f:
        s = f.read()
    k = str2int2bytes(args.key)
    c = AES.new(k)
    a = c.encrypt(s)
    print(a)
    with open(args.output, 'wb') as f:
        f.write(a)
    print(c.decrypt(a))
