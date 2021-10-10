import urllib.request
import zipfile

response = urllib.request.urlopen('https://www.clarin.si/repository/xmlui/bitstream/handle/11356/1210/ssj500k-en.TEI.zip')
archive = response.read()
file = open('ssj500k-en.TEI.zip','w')
file.write(archive)
file.close()
zipfile.ZipFile('ssj500k-en.TEI.zip').extractall('.')
