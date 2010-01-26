#!/bin/env python
# -*- coding: utf8 -*-
#	Author:	    ablozhou
#	E-mail:		ablozhou@gmail.com
#
#	Copyright 2010 ablozhou
#
#	Distributed under the terms of the GPL (GNU Public License)
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
#

class Phonetic():
    ''' Process phonetic symbols of Chiese characters
    or other languages.
    '''
    def replace(self,phonestr,tone):

        if tone=='5':
            return phonestr
        arry_a = ['ā', 'á', 'ǎ', 'à']
        arry_o = ['ō', 'ó', 'ǒ', 'ò']
        arry_e = ['ē', 'é', 'ě', 'è']
        arry_i = ['ī', 'í', 'ǐ', 'ì']
        arry_u = ['ū', 'ú', 'ǔ', 'ù']
        arry_v = ['ǖ', 'ǘ', 'ǚ', 'ǜ']
        #arry_A = ['Ā', 'Á', 'Ǎ', 'À']
        #arry_O = ['Ō', 'Ó', 'Ǒ', 'Ò']
        #arry_E = ['Ē', 'É', 'Ě', 'È']
        if 'iu' in phonestr :
            return string.replace(phonestr,'u',arry_u[int(tone)-1],maxsplit=1)
        if 'ui' in phonestr:
            return string.replace(phonestr,'i',arry_i[int(tone)-1],maxsplit=1)
        if 'a' in phonestr:
            return string.replace(phonestr,'a',arry_a[int(tone)-1],maxsplit=1)
        if 'o' in phonestr:
            return string.replace(phonestr,'o',arry_o[int(tone)-1],maxsplit=1)
        if 'e' in phonestr:
            return string.replace(phonestr,'e',arry_e[int(tone)-1],maxsplit=1)
        if 'i' in phonestr :
            return string.replace(phonestr,'i',arry_i[int(tone)-1],maxsplit=1)
        if 'u' in phonestr:
            return string.replace(phonestr,'u',arry_u[int(tone)-1],maxsplit=1)
        if 'v' in phonestr:
            return string.replace(phonestr,'v',arry_v[int(tone)-1],maxsplit=1)

        return phonestr
