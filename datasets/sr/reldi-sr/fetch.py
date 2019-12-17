import urllib2
response=urllib2.urlopen('https://www.clarin.si/repository/xmlui/bitstream/handle/11356/1240/ReLDI-sr.conllu.zip')
archive=response.read()
file=open('ReLDI-sr.conllu.zip','w')
file.write(archive)
file.close()
import zipfile
zipfile.ZipFile('ReLDI-sr.conllu.zip').extractall('.')
