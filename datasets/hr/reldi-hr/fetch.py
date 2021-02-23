import urllib.request
response=urllib.request.urlopen('https://www.clarin.si/repository/xmlui/bitstream/handle/11356/1241/ReLDI-hr.vert.zip')
archive=response.read()
file=open('ReLDI-hr.vert.zip','wb')
file.write(archive)
file.close()
import zipfile
zipfile.ZipFile('ReLDI-hr.vert.zip').extractall('.')
