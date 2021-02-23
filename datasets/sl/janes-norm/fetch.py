import os
import urllib.request
response=urllib.request.urlopen('https://www.clarin.si/repository/xmlui/bitstream/handle/11356/1084/Janes-Norm.vert.zip')
archive=response.read()
file=open('Janes-Norm.vert.zip','wb')
file.write(archive)
file.close()
import zipfile
if not os.path.exists('Janes-Norm.vert'):
    os.makedirs('Janes-Norm.vert')
zipfile.ZipFile('Janes-Norm.vert.zip').extractall('Janes-Norm.vert/')
