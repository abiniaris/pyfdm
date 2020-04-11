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

import configparser, os
from urlfile import UrlFile
from argparse import ArgumentParser

def getArgs():
    """
    Configure and parse CLI Arguments
    """
    parser = ArgumentParser()
    parser.add_argument("-f", "--file", required=True, dest="urlfile", help="URL File")
    parser.add_argument("-t", "--threads", default=2, type=int, choices=range(1,10),metavar="[1-10]", dest="threads", help="Number of parallel threads",)
    options=parser.parse_args()
    
    return options

def getConfig():
    """
    Load configuration file
    """
    config = configparser.ConfigParser()
    config.read('config.ini')
    
    if not os.path.exists(config['settings']['download_path']):
        raise ValueError("Please config proper download path in config.ini file")
    
    return config['settings']['download_path'] 

#dm = UrlFile("https://download-cf.jetbrains.com/idea/ideaIC-2019.3.4.exe",8).download()
options=getArgs()
path = getConfig()
dm = UrlFile(options.urlfile,path,options.threads).download()
 