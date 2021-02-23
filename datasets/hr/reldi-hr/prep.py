import random
random.seed(42)
train=[]
dev=[]
test=[]
ner_type='O'
import re
ner_re=re.compile(r' type="(.+?)"')
id_re=re.compile(r' id="(.+?)"')
for line in open('ReLDI-hr.vert/reldi_hr.vert'):
  if line.startswith('<text'):
    rand=random.random()
    if rand<0.8:
      pointer=train
    elif rand<0.9:
      pointer=dev
    else:
      pointer=test
  elif line.startswith('</s>'):
    pointer.append(s)
  elif line.startswith('<s '):
    s=[id_re.search(line).group(1)]
  elif line.startswith('<name'):
    ner_type='B-'+ner_re.search(line).group(1)
  elif line.startswith('</name>'):
    ner_type='O'
  else:
    if not line.startswith('<'):
      line=line.split('\t')
      s.append((line[0],line[1],line[3],line[4],line[5],ner_type))
    if ner_type.startswith('B-'):
      ner_type='I-'+ner_type[2:]

def write_list(lst,fname,norm=False):
  f=open(fname,'w')
  for el in lst:
    sent_id=el[0]
    tokens=el[1:]
    if not norm:
      f.write('# sent_id = '+sent_id+'\n')
    for idx,token in enumerate(tokens):
      if not norm:
        f.write(str(idx+1)+'\t'+token[0]+'\t'+token[1]+'\t'+token[3]+'\t'+token[2]+'\t'+token[4]+'\t_\t_\t_\t'+token[5]+'\n')
      else:
        f.write(token[0]+'\t'+token[1]+'\n')
    f.write('\n')
  f.close()
write_list(train,'train_ner.conllu')
write_list(dev,'dev_ner.conllu')
write_list(test,'test_ner.conllu')
write_list(train,'train_norm.tbl',True)
write_list(dev,'dev_norm.tbl',True)
write_list(test,'test_norm.tbl',True)
