import urllib2
response=urllib2.urlopen('https://www.clarin.si/repository/xmlui/bitstream/handle/11356/1210/ssj500k-en.TEI.zip')
archive=response.read()
file=open('ssj500k-en.TEI.zip','w')
file.write(archive)
file.close()
import zipfile
zipfile.ZipFile('ssj500k-en.TEI.zip').extractall('.')
