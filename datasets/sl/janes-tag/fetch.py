import urllib.request
response=urllib.request.urlopen('https://www.clarin.si/repository/xmlui/bitstream/handle/11356/1238/Janes-Tag.conllu.zip')
archive=response.read()
file=open('Janes-Tag.conllu.zip','wb')
file.write(archive)
file.close()
import zipfile
zipfile.ZipFile('Janes-Tag.conllu.zip').extractall('.')
