import urllib2
response=urllib2.urlopen('https://www.clarin.si/repository/xmlui/bitstream/handle/11356/1241/ReLDI-hr.conllu.zip')
archive=response.read()
file=open('ReLDI-hr.conllu.zip','w')
file.write(archive)
file.close()
import zipfile
zipfile.ZipFile('ReLDI-hr.conllu.zip').extractall('.')
