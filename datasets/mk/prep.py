import random
random.seed(42)
train=open('train.conllu','w')
dev=open('dev.conllu','w')
test=open('test.conllu','w')
sent=''
for line in open('mk.conllu'):
  sent+=line
  if line.strip()=='':
    rand=random.random()
    if rand<0.8:
      train.write(sent)
    elif rand<0.9:
      dev.write(sent)
    else:
      test.write(sent)
    sent=''
train.close()
dev.close()
test.close()
