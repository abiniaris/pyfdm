from urlfile import UrlFile
import argparse

#Get input parameters 
#inputurl = input ("Please provide URL :") 
#threadsurl = input ("Number of threads (default:10):")

"""parser = argparse.ArgumentParser(description='Download File from URL')
parser.add_argument('-f', metavar='URL', type=str, help='URL of the file to be dowloaded')
parser.add_argument('-p', metavar='File Parts', type=int, help='Number of file parts that will be downloaded in parallel')
args = parser.parse_args()"""

dm = UrlFile("https://download-cf.jetbrains.com/idea/ideaIC-2019.3.4.exe",8).download()
#dm = UrlFile("https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v7.8.5/npp.7.8.5.Installer.exe",20).download()



