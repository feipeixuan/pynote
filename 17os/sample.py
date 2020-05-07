#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, sys

# 打开文件
fd = os.open("f1.txt",os.O_RDWR|os.O_CREAT)

# 写入字符串
ret = os.write(fd,"This is runoob.com site".encode("utf-8"))

