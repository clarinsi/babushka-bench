import xml.etree.ElementTree as ET
import random
random.seed(42)
tree=ET.parse('setimes-sr.TEI/setimes-sr.body.xml')
root=tree.getroot()
train=[]
dev=[]
test=[]
train_ud=[]
dev_ud=[]
test_ud=[]
train_text=open('train.txt','w')
dev_text=open('dev.txt','w')
test_text=open('test.txt','w')
train_ud_text=open('train_ud.txt','w')
dev_ud_text=open('dev_ud.txt','w')
test_ud_text=open('test_ud.txt','w')
newline=False
for doc in root.iter('{http://www.tei-c.org/ns/1.0}ab'):
  rand=random.random()
  if rand<0.8:
    pointer=train
    pointer_text=train_text
    pointer_ud=train_ud
    pointer_ud_text=train_ud_text
  elif rand<0.9:
    pointer=dev
    pointer_text=dev_text
    pointer_ud=dev_ud
    pointer_ud_text=dev_ud_text
  else:
    pointer=test
    pointer_text=test_text
    pointer_ud=test_ud
    pointer_ud_text=test_ud_text
  for element in doc:
    if element.tag.endswith('s'):
      sentence=element
      text=''
      tokens=[]
      ud=None
      for element in sentence:
        if element.tag[-4:]=='name':
          for subelement in element:
            text+=subelement.text
            if not subelement.tag.endswith('}c'):
              if subelement.tag.endswith('w'):
                lemma=subelement.attrib['lemma']
              else:
                lemma=subelement.text
              upos=subelement.attrib['msd'].split('||')[0].split('|')
              feats='|'.join(upos[1:])
              if len(feats)==0:
                feats='_'
              upos=upos[0].split('=')[1]
              tokens.append((subelement.text,lemma,upos,subelement.attrib['ana'].split(':')[1],feats))
        if element.tag[-2:] not in ('pc','}w','}c'):
          if element.tag[-7:]=='linkGrp':
            if element.attrib['type']=='UD-SYN':
              ud=[]
              for subelement in element:
                label=subelement.attrib['ana'].split(':')[1]
                head,dep=subelement.attrib['target'].split(' ')
                head=head.split('.')
                if len(head)==1:
                  head='0'
                else:
                  head=head[1]
                ud.append((head,label))
          continue
        text+=element.text
        if not element.tag.endswith('}c'):
          if element.tag.endswith('w'):
            lemma=element.attrib['lemma']
          else:
            lemma=element.text
          upos=element.attrib['msd'].split('||')[0].split('|')
          feats='|'.join(upos[1:])
          if len(feats)==0:
            feats='_'
          upos=upos[0].split('=')[1]
          tokens.append((element.text,lemma,upos,element.attrib['ana'].split(':')[1],feats))
      pointer.append((text,tokens))
      if len(set(text[-2:]).intersection(set('.!?')))>0:
        newline=False
        pointer_text.write(text.encode('utf8'))
      else:
        newline=True
        pointer_text.write(text.encode('utf8')+'\n')
      if ud!=None:
        pointer_ud.append((text,tokens,ud))
        if not newline:
          pointer_ud_text.write(text.encode('utf8'))
        else:
          pointer_ud_text.write(text.encode('utf8')+'\n')
    else:
      if not newline:
        pointer_text.write(element.text.encode('utf8'))
      if ud!=None:
        if not newline:
          pointer_ud_text.write(element.text.encode('utf8'))
      newline=False
  pointer_text.write('\n')
  if ud!=None:
    pointer_ud_text.write('\n')

def write_list(lst,fname,synt=False):
  f=open(fname,'w')
  for el in lst:
    if not synt:
      text,tokens=el
    else:
      text,tokens,dep=el
    f.write('# text = '+text.encode('utf8')+'\n')
    for idx,token in enumerate(tokens):
      if not synt:
        f.write(str(idx+1)+'\t'+token[0].encode('utf8')+'\t'+token[1].encode('utf8')+'\t'+token[2].encode('utf8')+'\t'+token[3].encode('utf8')+'\t'+token[4].encode('utf8')+'\t_\t_\t_\t_\n')
      else:
        f.write(str(idx+1)+'\t'+token[0].encode('utf8')+'\t'+token[1].encode('utf8')+'\t'+token[2].encode('utf8')+'\t'+token[3].encode('utf8')+'\t'+token[4].encode('utf8')+'\t'+dep[idx][0].encode('utf8')+'\t'+dep[idx][1].encode('utf8')+'\t_\t_\n')
    f.write('\n')
  f.close()
write_list(train,'train.conllu')
write_list(dev,'dev.conllu')
write_list(test,'test.conllu')
write_list(train_ud,'train_ud.conllu',True)
write_list(dev_ud,'dev_ud.conllu',True)
write_list(test_ud,'test_ud.conllu',True)
train_text.close()
dev_text.close()
test_text.close()
train_ud_text.close()
dev_ud_text.close()
test_ud_text.close()
