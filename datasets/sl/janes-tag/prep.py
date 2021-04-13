import copy
import random
import conllu
random.seed(42)
# def next_sent():
#   conll=open('Janes-Tag.conllu/Janes-Tag.conllu')
#   sent=[]
#   a = conll.read()
#   b = conllu.parse(a)
#   for tree in b:
#     c = tree.serialize()
#     pass
#   for line in conll:
#     metadata = ''
#     if not line.startswith('#'):
#       if line.strip()=='':
#         yield sent, metadata
#         sent=[]
#       else:
#         line=line.split('\t')
#         sent.append([line[3],line[5]])
#     else:
#       metadata += line
# get_next_sent=next_sent()
# a = next(get_next_sent)
# b = next(get_next_sent)
train=[]
dev=[]
test=[]
train_normed=[]
dev_normed=[]
test_normed=[]
conll=open('Janes-Tag.conllu/Janes-Tag.conllu')
sent=[]
conlls = conllu.parse(conll.read())
for tree in conlls:
  rand=random.random()
  if rand<0.8:
    pointer=train
    pointer_normed=train_normed
  elif rand<0.9:
    pointer=dev
    pointer_normed=dev_normed
  else:
    pointer=test
    pointer_normed=test_normed
  tree_normed = copy.deepcopy(tree)
  for word in tree_normed:
    if word['misc'] is not None and 'Normalized' in word['misc']:
      word['form'] = word['misc']['Normalized']
      del word['misc']['Normalized']
  c = tree.serialize()
  pointer.append(tree.serialize())
  pointer_normed.append(tree_normed.serialize())

  #pointer_text.write('\n')

def write_list(lst,fname):
  f=open(fname,'w')
  for el in lst:
    f.write(el)
  f.close()

write_list(train,'train.conllu')
write_list(dev,'dev.conllu')
write_list(test,'test.conllu')
write_list(train_normed,'train_normed.conllu')
write_list(dev_normed,'dev_normed.conllu')
write_list(test_normed,'test_normed.conllu')
conll.close()
