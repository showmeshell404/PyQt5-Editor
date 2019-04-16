# -*- coding: utf-8 -*-
# @Time    : 2019/4/16 21:48
# @Author  : ShowMeShell
# @File    : frozen_dir.py
# @Software: PyCharm

import sys
import os

def app_path():
    if hasattr(sys, 'frozen'):
        return os.path.dirname(sys.executable)
    return os.path.dirname(__file__)

