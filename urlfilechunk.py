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
        
        block_sz = 8192
        while True:
        
            buffer = u.read(block_sz)
            
            if not buffer:
                break
          
            self.progress += len(buffer)
            f.write(buffer)
            
        f.close()