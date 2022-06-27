import xml.etree.ElementTree as ET
import random
random.seed(42)

def next_sent():
  conllu=open('ssj500k.conllu/ssj500k-ud-morphology.conllu', 'r', encoding='utf-8')
  sent=[]
  for line in conllu:
    if not line.startswith('#'):
      if line.strip()=='':
        yield sent
        sent=[]
      else:
        line=line.split('\t')
        sent.append([line[3],line[5]])


get_next_sent=next_sent()
tree=ET.parse('ssj500k-en.TEI/ssj500k-en.body.xml')
root=tree.getroot()
train=[]
dev=[]
test=[]
train_jos=[]
dev_jos=[]
test_jos=[]
train_ud=[]
dev_ud=[]
test_ud=[]
train_ner=[]
dev_ner=[]
test_ner=[]
train_ner_ud = []
dev_ner_ud = []
test_ner_ud = []
train_srl_ud = []
dev_srl_ud = []
test_srl_ud = []
train_srl_jos = []
dev_srl_jos = []
test_srl_jos = []
train_text=open('train.txt','w', encoding='utf8')
dev_text=open('dev.txt','w', encoding='utf8')
test_text=open('test.txt','w', encoding='utf8')
train_jos_text=open('train_jos.txt','w', encoding='utf8')
dev_jos_text=open('dev_jos.txt','w', encoding='utf8')
test_jos_text=open('test_jos.txt','w', encoding='utf8')
train_ud_text=open('train_ud.txt','w', encoding='utf8')
dev_ud_text=open('dev_ud.txt','w', encoding='utf8')
test_ud_text=open('test_ud.txt','w', encoding='utf8')
train_ner_text=open('train_ner.txt','w', encoding='utf8')
dev_ner_text=open('dev_ner.txt','w', encoding='utf8')
test_ner_text=open('test_ner.txt','w', encoding='utf8')
train_srl_ud_text=open('train_srl_ud.txt','w', encoding='utf8')
dev_srl_ud_text=open('dev_srl_ud.txt','w', encoding='utf8')
test_srl_ud_text=open('test_srl_ud.txt','w', encoding='utf8')
train_srl_jos_text=open('train_srl_jos.txt','w', encoding='utf8')
dev_srl_jos_text=open('dev_srl_jos.txt','w', encoding='utf8')
test_srl_jos_text=open('test_srl_jos.txt','w', encoding='utf8')
do_ner=True
for doc in root.iter('{http://www.tei-c.org/ns/1.0}div'):
  rand=random.random()
  if rand<0.8:
    pointer=train
    pointer_text=train_text
    pointer_ud=train_ud
    pointer_ud_text=train_ud_text
    pointer_jos=train_jos
    pointer_jos_text=train_jos_text
    pointer_ner_text=train_ner_text
    pointer_ner=train_ner
    pointer_ner_ud = train_ner_ud
    pointer_srl_ud = train_srl_ud
    pointer_srl_ud_text = train_srl_ud_text
    pointer_srl_jos = train_srl_jos
    pointer_srl_jos_text = train_srl_jos_text
  elif rand<0.9:
    pointer=dev
    pointer_text=dev_text
    pointer_ud=dev_ud
    pointer_ud_text=dev_ud_text
    pointer_jos=dev_jos
    pointer_jos_text=dev_jos_text
    pointer_ner=dev_ner
    pointer_ner_text=dev_ner_text
    pointer_ner_ud = dev_ner_ud
    pointer_srl_ud = dev_srl_ud
    pointer_srl_ud_text = dev_srl_ud_text
    pointer_srl_jos = dev_srl_jos
    pointer_srl_jos_text = dev_srl_jos_text
  else:
    pointer=test
    pointer_text=test_text
    pointer_ud=test_ud
    pointer_ud_text=test_ud_text
    pointer_jos=test_jos
    pointer_jos_text=test_jos_text
    pointer_ner=test_ner
    pointer_ner_text=test_ner_text
    pointer_ner_ud = test_ner_ud
    pointer_srl_ud = test_srl_ud
    pointer_srl_ud_text = test_srl_ud_text
    pointer_srl_jos = test_srl_jos
    pointer_srl_jos_text = test_srl_jos_text
  for p in doc.iter('{http://www.tei-c.org/ns/1.0}p'):
    #print p.attrib
    if p.attrib['{http://www.w3.org/XML/1998/namespace}id']=='ssj500.2653':
      do_ner=False
    for element in p:
      if element.tag.endswith('s'):
        sent_id=element.attrib['{http://www.w3.org/XML/1998/namespace}id']
        sentence=element
        text=''
        tokens=[]
        ners=[]
        uposfeats=next(get_next_sent)
        jos=None
        ud=None
        srl_ud=None
        srl=None if int(sent_id.split('.')[-1]) > 5501 else {}
        for element in sentence:
          if element.tag[-3:]=='seg':
            if element.attrib['type']=='name':
              ner=element.attrib['subtype']
            else:
              ner=None
            for idx,subelement in enumerate(element):
              text+=subelement.text
              if not subelement.tag.endswith('}c'):
                if subelement.tag.endswith('w'):
                  lemma=subelement.attrib['lemma']
                else:
                  lemma=subelement.text
                if do_ner:
                  if ner is not None:
                    if idx==0:
                      ners.append('B-'+ner)
                    else:
                      ners.append('I-'+ner)
                  else:
                    ners.append('O')
                tokens.append([subelement.text,lemma,subelement.attrib['ana'].split(':')[1], False])
          if element.tag[-2:] not in ('pc','}w','}c'):
            if element.tag[-7:]=='linkGrp':
              if element.attrib['type']=='UD-SYN':
                ud=[]
                for subelement in element:
                  label=subelement.attrib['ana'].split(':')[1]
                  head,dep=subelement.attrib['target'].split(' ')
                  head=head.split('.')[-1]
                  if head[0]!='t':
                    head='0'
                  else:
                    head=head[1:]
                  ud.append((head,label))
              elif element.attrib['type']=='JOS-SYN':
                jos=[]
                for subelement in element:
                  label=subelement.attrib['ana'].split(':')[1]
                  head,dep=subelement.attrib['target'].split(' ')
                  head=head.split('.')[-1]
                  if head[0]!='t':
                    head='0'
                  else:
                    head=head[1:]
                  jos.append((head,label))
              elif element.attrib['type']=='SRL':
                srl_ud = {}
                srl = {}
                for subelement in element:
                  label = subelement.attrib['ana'].split(':')[1]
                  head, dep = subelement.attrib['target'].split(' ')
                  head = head.split('.')[-1]
                  dep = dep.split('.')[-1]
                  if dep[0] != 't':
                    dep = '0'
                  else:
                    dep = dep[1:]
                  if head[0] != 't':
                    head = '0'
                  else:
                    head = head[1:]
                  if dep in srl_ud:
                    assert 'A srl dependency is repeated!'
                  srl_ud[dep] = (head, label)
                  srl[dep] = (head, label)
            continue
          text+=element.text
          if not element.tag.endswith('}c'):
            if element.tag.endswith('w'):
              lemma=element.attrib['lemma']
            else:
              lemma=element.text
            tokens.append([element.text,lemma,element.attrib['ana'].split(':')[1], False])
            if do_ner:
              ners.append('O')
          else:
            if len(tokens) > 0:
              tokens[-1][-1] = True

        tokens=[a+b for a,b in zip(tokens,uposfeats)]
        pointer.append((sent_id,text,tokens))
        pointer_text.write(text)
        if ud!=None:
          pointer_ud.append((sent_id,text,tokens,ud))
          pointer_ud_text.write(text)
          if do_ner:
            pointer_ner_ud.append((sent_id, text, tokens, ners, ud))
        if jos!=None:
          pointer_jos.append((sent_id,text,tokens,jos))
          pointer_jos_text.write(text)
        if do_ner:
          pointer_ner.append((sent_id,text,tokens,ners))
          pointer_ner_text.write(text)
        if srl_ud!=None and ud!=None:
          pointer_srl_ud.append((sent_id,text,tokens,ud,srl_ud))
          pointer_srl_ud_text.write(text)
        if srl!=None:
          pointer_srl_jos.append((sent_id,text,tokens,jos,srl))
          pointer_srl_jos_text.write(text)
      else:
        pointer_text.write(element.text)
        if ud!=None:
          pointer_ud_text.write(element.text)
        if jos!=None:
          pointer_jos_text.write(element.text)
        if do_ner:
          pointer_ner_text.write(element.text)
        if srl_ud!=None and ud!=None:
          pointer_srl_ud_text.write(element.text)
        if srl!=None:
          pointer_srl_jos_text.write(element.text)
    pointer_text.write('\n')
    if ud!=None:
      pointer_ud_text.write('\n')
    if jos!=None:
      pointer_jos_text.write('\n')
    if do_ner:
      pointer_ner_text.write('\n')
    if srl_ud!=None and ud!=None:
      pointer_srl_ud_text.write('\n')
    if srl!=None:
      pointer_srl_jos_text.write('\n')
  #pointer_text.write('\n')

def write_list(lst,fname,synt=False,ner=False,all=False,has_srl_ud=False, has_srl_jos=False):
  f=open(fname,'w', encoding='utf8')
  if all:
    f.write('# global.columns = ID TOKEN LEMMA UPOS XPOS FEATS NER_TYPE UD\n')
  for el in lst:
    if not synt and not ner:
      sid,text,tokens=el
    elif synt:
      if all:
        sid, text, tokens, nes, dep = el
      elif has_srl_ud:
        sid, text, tokens, dep, srl_ud = el
      elif has_srl_jos:
        sid, text, tokens, dep, srl = el
      else:
        sid, text, tokens, dep = el
    else:
      sid, text, tokens, nes = el

    f.write('# sent_id = '+sid+'\n')
    f.write('# text = '+text+'\n')
    for idx,token in enumerate(tokens):
      if not synt and not ner:
        f.write(str(idx+1)+'\t'+token[0]+'\t'+token[1]+'\t'+token[4]+'\t'+token[2]+'\t'+token[5]+'\t_\t_\t_\t_\n')
      elif synt:
        if all:
          f.write(str(idx+1)+'\t'+token[0]+'\t'+token[1]+'\t'+token[4]+'\t'+token[2]+'\t'+token[5]+'\t'+nes[idx]+'\t'
                  +dep[idx][1]+'\n')
        elif has_srl_ud:
          misc = f'SRL={srl_ud[str(idx+1)][1]}' if str(idx+1) in srl_ud else '_'
          if not token[3]:
            misc = misc + '|SpaceAfter=No' if misc != '_' else 'SpaceAfter=No'
          f.write(str(idx + 1) + '\t' + token[0] + '\t' + token[1] + '\t' + token[4] + '\t' + token[2] + '\t' + token[
            5] + '\t' + dep[idx][0]+'\t'+dep[idx][1] +'\t_\t' + misc + '\n')
        elif has_srl_jos:
          misc = f'SRL={srl[str(idx+1)][1]}' if str(idx+1) in srl else '_'
          if not token[3]:
            misc = misc + '|SpaceAfter=No' if misc != '_' else 'SpaceAfter=No'
          if dep is None:
            head = '0'
            deprel = 'Root'
          else:
            head = dep[idx][0]
            deprel = dep[idx][1]
          f.write(str(idx + 1) + '\t' + token[0] + '\t' + token[1] + '\t' + token[4] + '\t' + token[2] + '\t' + token[
            5] + '\t' + head + '\t' + deprel + '\t_\t' + misc + '\n')
        else:
          f.write(str(idx+1)+'\t'+token[0]+'\t'+token[1]+'\t'+token[4]+'\t'+token[2]+'\t'+token[5]+'\t'+dep[idx][0]+'\t'
                  +dep[idx][1]+'\t_\t_\n')
      else:
        f.write(str(idx+1)+'\t'+token[0]+'\t'+token[1]+'\t'+token[4]+'\t'+token[2]+'\t'+token[5]+'\t_\t_\t_\t'
                +nes[idx]+'\n')
    f.write('\n')
  f.close()

write_list(train,'train.conllu')
write_list(dev,'dev.conllu')
write_list(test,'test.conllu')
write_list(train_jos,'train_jos.conllu',True)
write_list(dev_jos,'dev_jos.conllu',True)
write_list(test_jos,'test_jos.conllu',True)
write_list(train_ud,'train_ud.conllu',True)
write_list(dev_ud,'dev_ud.conllu',True)
write_list(test_ud,'test_ud.conllu',True)
write_list(train_ner,'train_ner.conllu',ner=True)
write_list(dev_ner,'dev_ner.conllu',ner=True)
write_list(test_ner,'test_ner.conllu',ner=True)
write_list(train_ner_ud, 'train_ner_ud.conllup', synt=True, ner=True, all=True)
write_list(dev_ner_ud, 'dev_ner_ud.conllup', synt=True, ner=True, all=True)
write_list(test_ner_ud, 'test_ner_ud.conllup', synt=True, ner=True, all=True)
write_list(train_srl_ud, 'train_srl_ud.conllu', synt=True, has_srl_ud=True)
write_list(dev_srl_ud, 'dev_srl_ud.conllu', synt=True, has_srl_ud=True)
write_list(test_srl_ud, 'test_srl_ud.conllu', synt=True, has_srl_ud=True)
write_list(train_srl_jos, 'train_srl_jos.conllu', synt=True, has_srl_jos=True)
write_list(dev_srl_jos, 'dev_srl_jos.conllu', synt=True, has_srl_jos=True)
write_list(test_srl_jos, 'test_srl_jos.conllu', synt=True, has_srl_jos=True)

train_text.close()
dev_text.close()
test_text.close()
train_ud_text.close()
dev_ud_text.close()
test_ud_text.close()
train_jos_text.close()
dev_jos_text.close()
test_jos_text.close()
train_ner_text.close()
dev_ner_text.close()
test_ner_text.close()
train_srl_ud_text.close()
dev_srl_ud_text.close()
test_srl_ud_text.close()
train_srl_jos_text.close()
dev_srl_jos_text.close()
test_srl_jos_text.close()