import sys
i=0
for line in sys.stdin:
  if line.strip()=='':
    i=0
    sys.stdout.write(line)
  else:
    tok,tag=line.split('\t')
    i+=1
    sys.stdout.write(str(i)+'\t'+tok+'\t_\t_\t'+tag.strip()+'\t_'*5+'\n')
