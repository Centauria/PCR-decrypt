# -*- coding: utf-8 -*-
import base64
import hashlib
from Crypto.Cipher import AES


def info(s: str):
    b = base64.b64decode(s)
    print(f'Decode length: {len(b)}')
    print(f'Last 32 bytes: {b[-32:]}')
    sh = hashlib.md5()
    sh.update(b[:-32])
    print(f'MD5 without last 32 bytes: {sh.hexdigest()}')


def cipher(s: str):
    b = base64.b64decode(s)
    b, k = b[:-32], b[-32:]
    k = bytes(map(lambda x: int(x, 16), [k[i:i + 2] for i in range(len(k) - 1, -1, -2)]))
    c = AES.new(k)
    print(f'AES decrypt: {c.decrypt(b)}')
    print(f'AES encrypt: {c.encrypt(b)}')
    return c.encrypt(b)
