#! /usr/bin/env python
# -*- coding:utf-8 -*-

import base64

dec_file = base64.urlsafe_b64decode( "ここにurlsafeなbase64でエンコードしたimage文字列を入れる" )

with open("base64.png", 'w') as f4:
    f4.write(dec_file)