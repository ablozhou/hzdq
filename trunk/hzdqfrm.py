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

log = log4py.log4py('[hzdqframe]')

encoding = sys.getfilesystemencoding()

class hzdqframe(mainui_xrc.xrcmframe):
    def __init__(self,parent):

        mainui_xrc.xrcmframe.__init__(self,parent)

        self.txtmain = xrc.XRCCTRL(self, "txtmain")

        self.txtsearch = xrc.XRCCTRL(self, "txtsearch")
        self.txtsearch.SetValue('中'.decode('utf8'))

        s = self.txtsearch.GetValue().encode('utf8')
        f = file('./data/hzidx.dat','rb')
        self.hzidx = pk.load(f)
        f.close()
        #self.procdict = procdict.procdict('../../data/unihan.zip','blog.csdn.net/ablo_zhou')
        #self.unihan = self.procdict.dicttxt

        self.unihan = file('./data/unihan.dat','rb')
        #indx = '㐅'

        self.OnButton_btnsearch(None)

    def __del__(self):
        log.debug('close file')
        self.unihan.close()
        log.debug('close file finished')


#        self.gs = group.Groups(2, 20)
#        self.gs.open('../../data/freq_part.txt')
#        self.g = iter(self.gs)
#        self.group = self.g.next()
#        self.p = iter(self.group)
    def fmtgloss(self,gloss):
        glist = gloss.split(':')
        if glist[0] == 'en':
            return '\n英语解释:\t'+glist[1]
        return ''

    def fmtattr(self,attr):
        if len(attr) < 2: #空的
            return ''
        plist = attr.split(',')
        fmt = ''
        #处理拼音
        for s in plist:
            ph = s.split(':')
            if ph[0] == 'py': #拼音
                fmt += '\n汉语拼音:'+ph[1]
            elif ph[0] == 'Cant':
                fmt += '\n粤语拼音:'+ph[1]
            elif ph[0] == 'Hangul':
                fmt += '\n朝鲜谚文:'+ph[1]
                #print repr(ph[1].decode('utf8'))
            elif ph[0] == 'KoRom':
                fmt += '\n朝鲜罗马字:'+ph[1]
            elif ph[0] == 'JKun':
                fmt += '\n日语训读:'+ph[1]
            elif ph[0] == 'JOn':
                fmt += '\n日语音读:'+ph[1]
            elif ph[0] == 'Viet':
                fmt += '\n越南音标:'+ph[1]
            elif ph[0] == 'wb':
                fmt += '\n五笔:'+ph[1]
            elif ph[0] == 'cj':
                fmt += '\n仓颉:'+ph[1]
            elif ph[0] == '4c':
                fmt += '\n四角号码:'+ph[1]
            elif ph[0] == 'zm':
                fmt += '\n郑码:'+ph[1]
            elif ph[0] == 'fq':
                fmt += '\n频级:'+ph[1]
            elif ph[0] == 'rd':
                fmt += '\n部首:'+ph[1]
            elif ph[0] == 'sn':
                fmt += '\n笔画数:'+ph[1]
            elif ph[0] == 'st':
                fmt += '\n笔顺:'+ph[1]

        return fmt

    def fmtunicode(self,unicode):
        return '\nUnicode:'+unicode

    def OnButton_btnsave(self, evt):
        f = open('save.txt','a')
        r = self.txtmain.GetValue().encode('utf8')
        f.write(r)
        f.close()

    def OnButton_btnsearch(self, evt):
        log.debug('OnButton_btnsearch')
        search = self.txtsearch.GetValue()
        self.txtmain.SetValue(search)
        res = ''
        #p = phonetic.strip();
        space = [' ', '\n', '\t']
        for c in search:
            if c == u'-' or c in space:
                res += c.encode('utf8')
                continue
            if c in string.letters:
                res += c.encode('utf8')+'\n'
                continue
            if c in string.digits:
                res += c.encode('utf8')+'\n'
                continue

            try:

                seek = self.hzidx[c.encode('utf8')]
                self.unihan.seek(seek)
                line = self.unihan.readline()

                log.debug(line.decode('utf8'))
                l = line.split('\t')
                fmt = l[0]+'\n'+'='*15

                fmt += self.fmtunicode(l[1])
                fmt += self.fmtattr(l[2])
                fmt += self.fmtgloss(l[3])
                res += fmt +'\n\n'
                #res += '='*30

            except AttributeError:
                res += c +'\n'
        self.txtmain.SetValue(res.decode('utf8'))

    def OnButton_btnabout(self, evt):
        description = "The dictionary is used to search all Chinese Characters of the latest Unicode Han Database version 5.2"
        licence = "GNU General Public License version 2\n"
        info = wx.AboutDialogInfo()
        info.SetVersion('0.7')
        info.SetName('Hanzi Daquan')
        info.SetCopyright('(C) 2010 ablozhou')
        info.SetWebSite('http://blog.csdn.net/ablo_zhou')
        info.SetDescription(description)
        info.SetLicence(licence)
        info.AddDeveloper('ablozhou(周海汉) ablozhou@gmail.com\n'.decode('utf8'))

        wx.AboutBox(info)

    def OnKey_down_btnabout(self, evt):
        self.OnButton_btnabout(evt)
