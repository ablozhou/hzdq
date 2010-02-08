#!/bin/env python
# -*- coding: utf8 -*-
#周海汉

import os, sys
import glob
from distutils.core import setup
import py2exe

import version

#要包含的其它库文件
includes = ['encodings', 'encodings.*', 'gettext', 'glob',
            
            'wx.xrc']

options = {'py2exe':{
    'compressed': 1, #压缩
    'optimize': 2,
    'ascii': 1,
    'includes':includes,
    'bundle_files': 1 #所有文件打包成一个exe文件
    }}

setup(
    
    version = version.VERSION,
    description = 'hanzi dict',  
    name = 'hanzi daquan', 
    author = 'ablo(周海汉)',
    author_email = 'ablozhou@gmail.com',
    url = 'http://code.google.com/p/hzdq/',
    zipfile=None,#不生成library.zip文件

    data_files = [
                #('img', glob.glob('img/*')),
                  ('lang/zh_CN/LC_MESSAGES', glob.glob('lang/zh_CN/LC_MESSAGES/*')),
                  ('lang/en_US/LC_MESSAGES', glob.glob('lang/en_US/LC_MESSAGES/*')),
                  #('ui', glob.glob('ui/*.py')),
                  ('data',glob.glob('data/unihan.cpr')),
                  #('modules',glob.glob('modules/*.py')),
                  #('.',glob.glob('*.py')),
                  ('.',glob.glob('main.xrc')),
                  #('.', [os.path.join(os.environ['SystemRoot'], 'system32', 'msvcp71.dll')]),
                  ],
    options = options,
    windows = [{'script': 'hzdq.pyw', 'icon_resources': [(1, 'img/hzdq.ico')]}],#源文件，程序图标

)
 

