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
  elif line.startswith('<g/>'):
    previous_glue = True
  elif line.startswith('</s>'):
    pointer.append(s)
  elif line.startswith('<s'):
    s=[]
    previous_glue = True
  else:
    if not any(line.startswith(t) for t in tags):
      line=line.split('\t')
      if previous_glue:
        glue = ''
      else:
        glue = ' '
      previous_glue = False
      s.append([line[0],line[1],glue])

def write_list(lst,fname,raw=False):
  f=open(fname,'w')
  for el in lst:
    tokens=el
    raw_list = []
    for idx,token in enumerate(tokens):
      if not raw:
        f.write(token[0]+'\t'+token[1]+'\n')
      else:
        if len(token) == 3:
          raw_list.append(token[2])
          raw_list.append(token[0])
    if not raw:
      f.write('\n')
    else:
      f.write(''.join(raw_list) + '\n')
  f.close()
write_list(train,'train_norm.tbl')
write_list(dev,'dev_norm.tbl')
write_list(test,'test_norm.tbl')
write_list(train,'train_norm.txt',True)
write_list(dev,'dev_norm.txt',True)
write_list(test,'test_norm.txt',True)
