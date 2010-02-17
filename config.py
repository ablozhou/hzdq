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
#   date                author                  notes
#   2010.2.17       ablozhou            init config

import ConfigParser

class Configure(ConfigParser.ConfigParser):
    def __init__(self, filename):
        ConfigParser.RawConfigParser.__init__(self)
        self.filename=filename
        
        self.read(self.filename)
        
    def getlocale(self):
        locale = [ ]
        default = 'en_US'
        try:
            default = self.get('locale', 'lang',1)
        except ConfigParser.NoOptionError:
            print 'NoOptionError'
        except ConfigParser.NoSectionError:
            print 'NoSectionError'
            
        locale.append(default)
        return locale
            
        
if __name__ == '__main__':
    config = Configure('hzdq.ini')
    print   config.getlocale()      
