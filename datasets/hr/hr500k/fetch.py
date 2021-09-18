import urllib.request
response = urllib.request.urlopen('https://www.clarin.si/repository/xmlui/bitstream/handle/11356/1183/hr500k.TEI.zip')
archive = response.read()
file = open('hr500k.TEI.zip', 'wb')
file.write(archive)
file.close()
import zipfile
zipfile.ZipFile('hr500k.TEI.zip').extractall('.')
