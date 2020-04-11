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

class ProgressBar:
    FILL    ='█'
    EMPTY   ='-'
    PREFIX  ='Progress: '
    LENGTH  =50
    PRINTEND="\r"

def formatSize(downloaded):
    
    if   downloaded < 1000      : literal,num = 'By', downloaded
    elif downloaded < 1000**2   : literal,num = 'Kb',downloaded / 1000
    elif downloaded < 1000**3   : literal,num = 'Mb',downloaded / 1000**2
    elif downloaded < 1000**4   : literal,num = 'Gb',downloaded / 1000**3
    else                        : literal,num = 'Tb',downloaded / 1000**4

    return '{:>12.2f}'.format(num)+' '+literal

def formatSpeed(step):
    
    if   step < 1000      : literal,num = 'B/s', step
    elif step < 1000**2   : literal,num = 'kB/s',step / 1000
    else                  : literal,num = 'MB/s',step / 1000**2

    return '{:>12.2f}'.format(num)+' '+literal

def formatBar(downloaded, total):
    filled = int(ProgressBar.LENGTH * downloaded // total)
    return ProgressBar.FILL * filled + ProgressBar.EMPTY * (ProgressBar.LENGTH - filled)

def formatPercent(downloaded, total):
    return '{0:.2f}'.format(100 * (downloaded / float(total)))

def printProgressBar (downloaded,total,step):
    """
    Progress bar with completion percentage 
    """
    print('\r%s |%s|%s%% %s %s' % (ProgressBar.PREFIX,\
                                    formatBar(downloaded,total),\
                                    formatPercent(downloaded,total),\
                                    formatSize(downloaded),\
                                    formatSpeed(step)),\
                                    end=ProgressBar.PRINTEND)
