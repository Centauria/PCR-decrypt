# -*- coding: utf-8 -*-
import base64
import hashlib


def info(s: str):
    b = base64.b64decode(s)
    print(f'Decode length: {len(b)}')
    print(f'Last 32 bytes: {b[-32:]}')
    sh = hashlib.md5()
    sh.update(b[:-32])
    print(f'MD5 without last 32 bytes: {sh.hexdigest()}')
