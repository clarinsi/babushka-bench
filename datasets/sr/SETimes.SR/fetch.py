import urllib2
response=urllib2.urlopen('https://www.clarin.si/repository/xmlui/bitstream/handle/11356/1200/setimes-sr.TEI.zip')
archive=response.read()
file=open('setimes-sr.TEI.zip','w')
file.write(archive)
file.close()
import zipfile
zipfile.ZipFile('setimes-sr.TEI.zip').extractall('.')
