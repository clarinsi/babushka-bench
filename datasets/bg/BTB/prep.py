import xml.etree.ElementTree as ET
import random
random.seed(42)
def next_sent():
  conllu=open('BulTreeBankPOSALL.txt')
  sent=[]
  for line in conllu:
    if not line.startswith('#'):
      if line.strip()=='':
        yield sent
        sent=[]
      else:
        line=line.strip().split('\t')
        assert len(line)==6,str(line)+' not of right length'
        sent.append(line)
train=[]
dev=[]
test=[]
train_ud=[]
dev_ud=[]
test_ud=[]
train_ner=[]
dev_ner=[]
test_ner=[]
"""
train_text=open('train.txt','w')
dev_text=open('dev.txt','w')
test_text=open('test.txt','w')
train_ud_text=open('train_ud.txt','w')
dev_ud_text=open('dev_ud.txt','w')
test_ud_text=open('test_ud.txt','w')
train_ner_text=open('train_ner.txt','w')
dev_ner_text=open('dev_ner.txt','w')
test_ner_text=open('test_ner.txt','w')
"""
do_ner=True
for sent in next_sent():
  rand=random.random()
  if rand<0.8:
    pointer=train
    #pointer_text=train_text
    #pointer_ud=train_ud
    #pointer_ud_text=train_ud_text
    #pointer_ner_text=train_ner_text
    #pointer_ner=train_ner
  elif rand<0.9:
    pointer=dev
    #pointer_text=dev_text
    #pointer_ud=dev_ud
    #pointer_ud_text=dev_ud_text
    #pointer_ner=dev_ner
    #pointer_ner_text=dev_ner_text
  else:
    pointer=test
    #pointer_text=test_text
    #pointer_ud=test_ud
    #pointer_ud_text=test_ud_text
    #pointer_ner=test_ner
    #pointer_ner_text=test_ner_text
  pointer.append(sent)

def write_list(lst,fname,synt=False,ner=False):
  f=open(fname,'w')
  for tokens in lst:
    for idx,token in enumerate(tokens):
      f.write(str(idx+1)+'\t'+token[1]+'\t'+token[2]+'\t'+token[3]+'\t'+token[4]+'\t'+token[5]+'\t_\t_\t_\t_\n')
    f.write('\n')
  f.close()

write_list(train,'train.conllu')
write_list(dev,'dev.conllu')
write_list(test,'test.conllu')
"""
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
train_jos_text.close()
dev_jos_text.close()
test_jos_text.close()
train_ner_text.close()
dev_ner_text.close()
test_ner_text.close()
"""
