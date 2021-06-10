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
train_ner=[]
dev_ner=[]
test_ner=[]
train_text=open('train.txt','w', encoding='utf8')
dev_text=open('dev.txt','w', encoding='utf8')
test_text=open('test.txt','w', encoding='utf8')
train_ud_text=open('train_ud.txt','w', encoding='utf8')
dev_ud_text=open('dev_ud.txt','w', encoding='utf8')
test_ud_text=open('test_ud.txt','w', encoding='utf8')
train_ner_text=open('train_ner.txt','w', encoding='utf8')
dev_ner_text=open('dev_ner.txt','w', encoding='utf8')
test_ner_text=open('test_ner.txt','w', encoding='utf8')
newline=False
for doc in root.iter('{http://www.tei-c.org/ns/1.0}ab'):
  rand=random.random()
  if rand<0.8:
    pointer=train
    pointer_text=train_text
    pointer_ud=train_ud
    pointer_ud_text=train_ud_text
    pointer_ner=train_ner
    pointer_ner_text=train_ner_text
  elif rand<0.9:
    pointer=dev
    pointer_text=dev_text
    pointer_ud=dev_ud
    pointer_ud_text=dev_ud_text
    pointer_ner=dev_ner
    pointer_ner_text=dev_ner_text
  else:
    pointer=test
    pointer_text=test_text
    pointer_ud=test_ud
    pointer_ud_text=test_ud_text
    pointer_ner=test_ner
    pointer_ner_text=test_ner_text
  for element in doc:
    if element.tag.endswith('s'):
      sent_id=element.attrib['{http://www.w3.org/XML/1998/namespace}id']
      sentence=element
      text=''
      tokens=[]
      ners=[]
      ud=None
      for element in sentence:
        if element.tag[-4:]=='name':
          ner=element.attrib['type']
          for idx,subelement in enumerate(element):
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
              if idx==0:
                ners.append('B-'+ner)
              else:
                ners.append('I-'+ner)
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
          ners.append('O')
      pointer.append((sent_id,text,tokens))
      pointer_ner.append((sent_id,text,tokens,ners))
      if len(set(text[-2:]).intersection(set('.!?')))>0:
        newline=False
        pointer_text.write(text)
        pointer_ner_text.write(text)
      else:
        newline=True
        pointer_text.write(text+'\n')
        pointer_ner_text.write(text+'\n')
      if ud!=None:
        pointer_ud.append((sent_id,text,tokens,ud))
        if not newline:
          pointer_ud_text.write(text)
        else:
          pointer_ud_text.write(text+'\n')
    else:
      if not newline:
        pointer_text.write(element.text)
        pointer_ner_text.write(element.text)
      if ud!=None:
        if not newline:
          pointer_ud_text.write(element.text)
      newline=False
  pointer_text.write('\n')
  pointer_ner_text.write('\n')
  if ud!=None:
    pointer_ud_text.write('\n')

def write_list(lst,fname,synt=False,ner=False):
  f=open(fname,'w', encoding='utf8')
  for el in lst:
    if not synt and not ner:
      sent_id,text,tokens=el
    elif synt:
      sent_id,text,tokens,dep=el
    else:
      sent_id,text,tokens,nes=el
    f.write('# sent_id = '+sent_id+'\n')
    f.write('# text = '+text+'\n')
    for idx,token in enumerate(tokens):
      if not synt and not ner:
        f.write(str(idx+1)+'\t'+token[0]+'\t'+token[1]+'\t'+token[2]+'\t'+token[3]+'\t'+token[4]+'\t_\t_\t_\t_\n')
      elif synt:
        f.write(str(idx+1)+'\t'+token[0]+'\t'+token[1]+'\t'+token[2]+'\t'+token[3]+'\t'+token[4]+'\t'+dep[idx][0]+'\t'+dep[idx][1]+'\t_\t_\n')
      else:
        f.write(str(idx+1)+'\t'+token[0]+'\t'+token[1]+'\t'+token[3]+'\t'+token[2]+'\t'+token[4]+'\t_\t_\t_\t'+nes[idx]+'\n')
    f.write('\n')
  f.close()
write_list(train,'train.conllu')
write_list(dev,'dev.conllu')
write_list(test,'test.conllu')
write_list(train_ud,'train_ud.conllu',True)
write_list(dev_ud,'dev_ud.conllu',True)
write_list(test_ud,'test_ud.conllu',True)
write_list(train_ner,'train_ner.conllu',ner=True)
write_list(dev_ner,'dev_ner.conllu',ner=True)
write_list(test_ner,'test_ner.conllu',ner=True)
train_text.close()
dev_text.close()
test_text.close()
train_ud_text.close()
dev_ud_text.close()
test_ud_text.close()
train_ner_text.close()
dev_ner_text.close()
test_ner_text.close()