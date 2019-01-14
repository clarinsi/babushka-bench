import xml.etree.ElementTree as ET
import random
random.seed(42)
tree=ET.parse('ssj500k-en.TEI/ssj500k-en.body.xml')
root=tree.getroot()
train=[]
dev=[]
test=[]
train_text=open('train.txt','w')
dev_text=open('dev.txt','w')
test_text=open('test.txt','w')
for doc in root.iter('{http://www.tei-c.org/ns/1.0}div'):
  rand=random.random()
  if rand<0.8:
    pointer=train
    pointer_text=train_text
  elif rand<0.9:
    pointer=dev
    pointer_text=dev_text
  else:
    pointer=test
    pointer_text=test_text
  for p in doc.iter('{http://www.tei-c.org/ns/1.0}p'):
    for element in p:
      if element.tag.endswith('s'):
        sentence=element
        text=''
        tokens=[]
        for element in sentence:
          if element.tag[-3:]=='seg':
            for subelement in element:
              text+=subelement.text
              if not subelement.tag.endswith('}c'):
                if subelement.tag.endswith('w'):
                  lemma=subelement.attrib['lemma']
                else:
                  lemma=subelement.text
                tokens.append((subelement.text,lemma,subelement.attrib['ana'].split(':')[1]))
          if element.tag[-2:] not in ('pc','}w','}c'):
            continue
          text+=element.text
          if not element.tag.endswith('}c'):
            if element.tag.endswith('w'):
              lemma=element.attrib['lemma']
            else:
              lemma=element.text
            tokens.append((element.text,lemma,element.attrib['ana'].split(':')[1]))
        pointer.append((text,tokens))
        pointer_text.write(text.encode('utf8'))
      else:
        pointer_text.write(element.text.encode('utf8'))
    pointer_text.write('\n')
  #pointer_text.write('\n')

def write_list(lst,fname):
  f=open(fname,'w')
  for text,tokens in lst:
    f.write('# text = '+text.encode('utf8')+'\n')
    for idx,token in enumerate(tokens):
      f.write(str(idx+1)+'\t'+token[0].encode('utf8')+'\t'+token[1].encode('utf8')+'\t_\t'+token[2]+'\t_\t_\t_\t_\t_\n')
    f.write('\n')
  f.close()
write_list(train,'train.conllu')
write_list(dev,'dev.conllu')
write_list(test,'test.conllu')
train_text.close()
dev_text.close()
test_text.close()
    