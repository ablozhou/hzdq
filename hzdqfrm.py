#!/bin/env python
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
#   modify history
#   date          author    notes
#   2010.1.26    ablozhou   release 0.5 OS:ubuntu 9.10 python:2.6.2
#   2010.1.31   ablozhou    release 0.6 OS:run in windows xp, still can't display korean.

import sys
import wx
import mainui_xrc
import wx.xrc as xrc

import modules.log4py as log4py
import string
import procdict
import cPickle as pk
import config
import gettext
import i18n
import modules.data as data

log = log4py.log4py('[hzdqframe]')

encoding = sys.getfilesystemencoding()

idxfile = './data/hzidx.dat'
datafile = './data/unihan.dat'


class hzdqframe(mainui_xrc.xrcmframe):
    def __init__(self,parent):
        #config file
        conf = config.Configure('hzdq.ini')
        lang = conf.getlocale()

        #i18n
        i18n.install(self, 'lang', lang)

        mainui_xrc.xrcmframe.__init__(self,parent)
        self.icon = wx.Icon('img/hzdq.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
        self.txtmain = xrc.XRCCTRL(self, "txtmain")

        self.txtsearch = xrc.XRCCTRL(self, "txtsearch")
        self.txtsearch.SetValue('中'.decode('utf8'))

        s = self.txtsearch.GetValue().encode('utf8')

        #datafile
        self.data = data.HzdqData(idxfile, datafile)
        #index file
#        f = file('./data/hzidx.dat','rb')
#        self.hzidx = pk.load(f)
#        f.close()

        #self.procdict = procdict.procdict('../../data/unihan.zip','blog.csdn.net/ablo_zhou')
        #self.unihan = self.procdict.dicttxt

        #self.unihan = file('./data/unihan.dat','rb')
        #indx = '㐅'

        self.OnButton_btnsearch(None)

    def __del__(self):
        pass

    def OnButton_btnsave(self, evt):
        f = open('save.txt','a')
        r = self.txtmain.GetValue().encode('utf8')
        f.write(r)
        f.close()

    def OnButton_btnsearch(self, evt):
        log.debug('OnButton_btnsearch')
        search = self.txtsearch.GetValue()
        self.txtmain.SetValue(search)
        hzdict,fmt = self.data.querys(search)
        log.debug(fmt.decode('utf8'))
        #space = [' ', '\n', '\t', '\r', '\f', '\v']

        self.txtmain.SetValue(fmt.decode('utf8'))

    def OnButton_btnabout(self, evt):
        import version
        description = version.DESC
        license = version.LICENSE
        info = wx.AboutDialogInfo()
        info.SetVersion(version.VERSION)
        info.SetName(version.NAME)
        info.SetCopyright(version.COPYRT)
        info.SetWebSite(version.WEB)
        info.SetDescription(description)
        info.SetLicence(license)
        info.AddDeveloper('ablozhou(周海汉) ablozhou@gmail.com\n'.decode('utf8'))

        wx.AboutBox(info)

    def OnKey_down_btnabout(self, evt):
        self.OnButton_btnabout(evt)
