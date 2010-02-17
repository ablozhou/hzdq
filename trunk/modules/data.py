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
#   modify history
#   date          author    notes
#   2010.2.18       zhouhh  init data api

import sys
import log4py
import char
import string
import cPickle as pk
import traceback

log = log4py.log4py('[data]')

class HzdqData():
    def __init__(self,idxfile, datafile):
        self.idxname = idxfile
        self.dataname = datafile
        f = file(idxfile,'rb')#'./data/hzidx.dat'
        self.hzidx = pk.load(f)
        f.close()
        self.unihan = file(datafile,'rb')#'./data/unihan.dat'


    #def open(self,filename):
    #    pass

    #得到某个汉字在文件中的偏移
    def gethzfilepos(self, char):
        seek = self.hzidx[char.encode('utf8')]
        return seek

    #得到某个汉字所在文件的行
    def gethzline(self, char):
        seek = self.gethzfilepos(char)
        self.unihan.seek(seek)
        line = self.unihan.readline()
        log.debug(line.decode('utf8'))
        return line

    def getgloss(self, ch, gloss):
        glist = gloss.split(':')
        if glist[0] == 'en':
            ch.addgloss(glist[1],char.English)

            return '\n英语解释:'+glist[1]
        return ''

    def getattr(self, ch, attr):
        if len(attr) < 2: #空的
            return ''
        plist = attr.split(',')
        fmt = ''
        #处理拼音
        for s in plist:
            ph = s.split(':')
            if ph[0] == 'py': #拼音
                ch.addphonetic(ph[1])
                fmt += '\n汉语拼音:'+ph[1]
            elif ph[0] == 'Cant':
                ch.addphonetic(ph[1],char.Cantonese,char.Chinese)
                fmt += '\n粤语拼音:'+ph[1]
            elif ph[0] == 'Hangul':
                ch.addphonetic(ph[1],char.Hangul,char.Korean)
                fmt += '\n朝鲜谚文:'+ph[1]
                #print repr(ph[1].decode('utf8'))
            elif ph[0] == 'KoRom':
                ch.addphonetic(ph[1],char.Korean_roman,char.Korean)
                fmt += '\n朝鲜罗马字:'+ph[1]
            elif ph[0] == 'JKun':
                ch.addphonetic(ph[1],char.JapaneseKun,char.Japanese)
                fmt += '\n日语训读:'+ph[1]
            elif ph[0] == 'JOn':
                ch.addphonetic(ph[1],char.JapaneseOn,char.Japanese)
                fmt += '\n日语音读:'+ph[1]
            elif ph[0] == 'Viet':
                ch.addphonetic(ph[1],char.Vietnamese,char.Vietnamese)
                fmt += '\n越南音标:'+ph[1]

            elif ph[0] == 'wb':
                ch.consult[char.CANGJIE]=ph[1]
                fmt += '\n五笔:'+ph[1]
            elif ph[0] == 'cj':
                ch.consult[char.WUBI]=ph[1]
                fmt += '\n仓颉:'+ph[1]
            elif ph[0] == '4c':
                ch.consult[char.FOURCORNER]=ph[1]
                fmt += '\n四角号码:'+ph[1]
            elif ph[0] == 'zm':
                ch.consult[char.ZHENGMA]=ph[1]
                fmt += '\n郑码:'+ph[1]

            elif ph[0] == 'fq':
                ch.freq=int(ph[1])
                fmt += '\n频级:'+ph[1]
            elif ph[0] == 'rd':
                ch.radical = ph[1]
                fmt += '\n部首:'+ph[1]
            elif ph[0] == 'sn':
                ch.strokenum=int(ph[1])
                fmt += '\n笔画数:'+ph[1]
            elif ph[0] == 'st':
                ch.strokes = ph[1]
                fmt += '\n笔顺:'+ph[1]

        return fmt

    def getunicode(self, unicode):
        return '\nUnicode:'+unicode

    def query(self, c):
        #try:
        line = self.gethzline(c)
        hzdict = {}

        l = line.split('\t')
        fmt = l[0]+'\n'+'='*15
        ch = char.Char(c)
        hzdict[c] = ch

        fmt += self.getunicode(l[1])
        fmt += self.getattr(ch, l[2])
        fmt += self.getgloss(ch, l[3])
        fmt += '\n\n'
        #log.debug(fmt.decode('utf8'))

        #except AttributeError:
        #    print traceback.format_exception(*sys.exc_info())
        #    log.error('AttributeError',True)
        return ch,fmt

    def querys(self,search):
        space = [' ', '\n', '\t', '\r', '\f', '\v']
        hzdict = {}
        fmts = ''
        for c in search:
            if c == u'-' or c in space or c in string.letters or c in string.digits:
                hzdict[c] = None
                continue

            ch,fmt = self.query(c)
            fmts += fmt
            hzdict[c] = ch

        return hzdict,fmts

    def __del__(self):
        log.debug('close file')
        self.unihan.close()
        log.debug('close file finished')

class FmtData():
    def gettxtfmt(self):
        fmt = l[0]+'\n'+'='*15

        fmt += self.fmtunicode(l[1])
        fmt += self.fmtattr(l[2])
        fmt += self.fmtgloss(l[3])
        res += fmt +'\n\n'

    def fmtgloss(self,gloss):
        glist = gloss.split(':')
        if glist[0] == 'en':
            return '\n英语解释:'+glist[1]
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

if __name__ == '__main__':
    import sys
    print sys.path
    hzdq = HzdqData('../data/hzidx.dat','../data/unihan.dat')
    hz = '中华汉'.decode('utf8')
    hzdict, fmt = hzdq.querys(hz)
#    s = hzdict[hz]
#    p = s.getphonetics()
#    t = s.char
#    g = s.getgloss()
#    print g.encode('utf8')
#    print t.encode('utf8')
#    print p#.encode('utf8')
    print fmt