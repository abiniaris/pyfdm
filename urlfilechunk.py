#    This file is part of PYFDM.
#
#    PYFDM is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    PYFDM is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with PYFDM.  If not, see <http://www.gnu.org/licenses/>.

import urllib.request
from threading import Thread

class UrlFileChunk(Thread):

    def __init__(self, url, filename, startbyte, endbyte):
        super(UrlFileChunk,self).__init__()

        self.url        =url
        self.filename   =filename
        self.startbyte  =startbyte
        self.endbyte    =endbyte
        self.progress   =0 

    def run(self):

        header= { 'Range' : 'bytes={}-{}'.format(self.startbyte,self.endbyte) }
        request = urllib.request.Request(self.url, headers=header)
        u = urllib.request.urlopen(request)
        
        f = open(self.filename, 'wb')
        
        block_size-8192
        while True:
            buffer = u.read(block_size)
            
            if not buffer:
                break
          
            self.progress += len(buffer)
            f.write(buffer)
            
        f.close()