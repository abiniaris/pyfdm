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

import urllib.request, time
from math import ceil
from urlfilechunk import UrlFileChunk
import os

class UrlFile:
    
    BLOCK_SZ=8192

    def __init__(self, url, path, threads):
        
        self.url        = url
        self.path       = path
        self.threads    = threads
        self.filename   = url.split('/')[-1]
        request         = urllib.request.urlopen(self.url)
        metadata        = request.info()
        self.filesize   = int(metadata.get_all("Content-Length")[0])
    
    def download(self):
        """
        Split and Start downloading file chunks in parallel
        """        
        #Split file in multiple chunks
        filechunks= self.__split()

        #Start threads
        for filechunk in filechunks:
            th=filechunk.start() 
        
        #Monitor and print progress
        step=0
        while True:
            
            downloaded=self.__downloaded(filechunks)
            step    =downloaded - step

            self.printProgressBar(downloaded, self.filesize, speed=step)
            
            if self.filesize<=downloaded:
                break

            step=downloaded
            time.sleep(1)

        #Merge file chuncks to one file
        self.__merge(filechunks)
        self.__cleanup(filechunks)

    def __downloaded(self, filechunks):
        """
        Return download progress for all file chunks 
        """
        progress=0
        for filechunk in filechunks:
                progress+=filechunk.progress
        return progress       

    def __split(self):
        """
        Split file to multiple chunks based on number of threads provided
        """
        filechunks=[]
        chunksize = ceil(self.filesize / self.threads)
        startbyte=0 

        for i in range (0, self.threads):
            chunkfilename=os.path.join(self.path,self.filename+'.part'+str(i))  
            filechunks.append(UrlFileChunk(self.url,chunkfilename,startbyte,startbyte+chunksize))
            startbyte +=chunksize+1 
        
        return filechunks

    def __cleanup(self, filechunks):
        
        for filechunk in filechunks:
            os.remove(filechunk.filename)

    def __merge(self, filechunks):
        """
        Merge file chunks to one file
        """
        urlfile=open(os_path_join(self.path,self.filename), 'wb')
        
        for filechunk in filechunks:
            tmpfile=open(filechunk.filename, 'rb')
        
            while True:
                buffer = tmpfile.read(BLOCK_SZ)
                
                if not buffer:
                    break
            
                urlfile.write(buffer)
            
        urlfile.close()   

    
    def printProgressBar (self,iteration,total=0,speed=0):
        """
        Progress bar with completion percentage 
        """
        #prefix,suffix,length,fill,printEnd='Progress:','Complete',50,'█',"\r"
        
        print('\r%s |%s|%s%% %s (%s)'%\
                    ('Progress','█' * int(50 * iteration // total) + '-' * (50 - int(50 * iteration // total)),\
                    '{0:.1f}'.format(100 * (iteration / float(total))),\
                     'Complete','{:.2f} MB/sec'.format(speed/1024/1024)),end ="\r")      
        
"""
        dispeed = '{:.2f} MB/sec'.format(speed/1024/1024)
        percent = ("{0:.1f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print('\r%s |%s|%s%% %s (%s)' % (prefix, bar, percent,suffix,dispeed), end = printEnd)"""
