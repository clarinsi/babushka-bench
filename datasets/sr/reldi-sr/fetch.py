import urllib.request
response=urllib.request.urlopen('https://www.clarin.si/repository/xmlui/bitstream/handle/11356/1240/ReLDI-sr.conllu.zip')
archive=response.read()
file=open('ReLDI-sr.conllu.zip','wb')
file.write(archive)
file.close()
import zipfile
zipfile.ZipFile('ReLDI-sr.conllu.zip').extractall('.')
