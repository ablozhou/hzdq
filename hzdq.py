#!/usr/bin/env python
# -*- coding: utf8 -*-
#   Author:        ablozhou
#   E-mail:        ablozhou@gmail.com
#
#   Copyright 2010 ablozhou
#
#   Distributed under the terms of the GPL (GNU Public License)
#
#   HZDQ(Hanzi Daquan) is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
#   HZDQ(Hanzi Daquan) is a dictionary  contains all data from Unicode han database(Unihan),
#   which is a part of the latest Unicode version 5.2. You can find any format of
#   Han ideographic script from this dictionary.
#
#   modify history
#   date          author    notes
#   2010.1.26   ablozhou    release 0.5 OS:ubuntu 9.10 python:2.6.2
#   2010.1.31   ablozhou    release 0.6 OS:run in windows xp, still can't display korean.
#
__appname__ = 'hzdq'
__author__ = 'ablozhou'
__email__='ablozhou@gmail.com'

import sys
import os
import wx
import mainui_xrc
import hzdqfrm
import zipfile

WEB='http://code.google.com/p/hzdq'

workpath = os.path.dirname(os.path.abspath(sys.argv[0]))
datapath = os.path.join(workpath,'data')
os.chdir(workpath)
sys.path.insert(0, workpath)

class HzdqApp(wx.App):
    def OnInit(self):
        
        self.mainfrm = hzdqfrm.hzdqframe(parent = None)
        self.checkfile('unihan.dat')
        self.SetTopWindow(self.mainfrm)
        self.mainfrm.Show()
        return True
        
    def Exit(self):
        pass
        
    def checkfile(self, filename):
        f = os.path.join(datapath,filename)
        
        isf = os.path.isfile(f)
        if isf:
            pass
        else:
            zfile = os.path.join(datapath,'unihan.cpr')
            
            z = zipfile.ZipFile(zfile,'r',zipfile.ZIP_DEFLATED)
            z.setpassword(WEB)
            for fn in z.namelist():
                z.extract(fn,datapath)

            z.close()           
#TODO 设置多行文本控件字体
#指定一个文件的另一个执行文件
def main():
    app = HzdqApp(False)
    app.MainLoop()

if __name__ == '__main__':
    main()
