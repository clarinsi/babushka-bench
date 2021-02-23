import random
random.seed(42)
tags = ['<g/>', '<corpus', '<text', '</corpus', '</text']
train=[]
dev=[]
test=[]
for line in open('Janes-Norm.vert/janes.norm.vert'):
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
  elif line.startswith('<s'):
    s=[]
  else:
    if not any(line.startswith(t) for t in tags):
      line=line.split('\t')
      s.append((line[0],line[1]))

def write_list(lst,fname):
  f=open(fname,'w')
  for el in lst:
    tokens=el
    for idx,token in enumerate(tokens):
      f.write(token[0]+'\t'+token[1]+'\n')
    f.write('\n')
  f.close()
write_list(train,'train_norm.tbl')
write_list(dev,'dev_norm.tbl')
write_list(test,'test_norm.tbl')
