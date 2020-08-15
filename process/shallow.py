# -*- coding: utf-8 -*-
import base64
import hashlib

from Crypto.Cipher import AES


def debase(s: str):
    b = base64.b64decode(s)
    return b[:-32], b[-32:]


def str2int2bytes(s: str, byte_order='dec'):
    if byte_order == 'dec':
        split = [s[i:i + 2] for i in range(0, len(s), 2)]
    elif byte_order == 'inc':
        split = [s[i:i + 2] for i in range(len(s) - 1, -1, -2)]
    else:
        raise ValueError('byte_order must be "dec" or "inc"')
    return bytes(map(lambda x: int(x, 16), split))


def info(s: str):
    b = base64.b64decode(s)
    print(f'Decode length: {len(b)}')
    print(f'Last 32 bytes: {b[-32:]}')
    sh = hashlib.md5()
    sh.update(b[:-32])
    print(f'MD5 without last 32 bytes: {sh.hexdigest()}')


def try_cipher(s: str):
    b = base64.b64decode(s)
    b, k = b[:-32], b[-32:]
    k = str2int2bytes(k)
    c = AES.new(k)
    print(f'AES decrypt: {c.decrypt(b)}')
    print(f'AES encrypt: {c.encrypt(b)}')
    return c.encrypt(b)
