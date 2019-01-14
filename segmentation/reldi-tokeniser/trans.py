import sys
for line in sys.stdin:
  if line.strip()=='':
    sys.stdout.write(line)
  else:
    tid,tok=line.split('\t')
    sys.stdout.write(tid.split('.')[2]+'\t'+tok.strip()+'\t_'*8+'\n')
