#!/bin/env python
# coding: cp936

import os
import gettext

def install(localdir, languages):
    gettext.translation('hzdq', localedir=localdir, languages=languages).install(True)

if __name__ == '__main__':
    install('lang',['zh_CN'])
    print _('hello')
