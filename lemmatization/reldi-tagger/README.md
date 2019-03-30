```
grep -v '^#' ../../datasets/sl/ssj500k/test.conllu | cut -f 2,5 | python /home/nikola/tools/clarinsi/reldi-tagger/lemmatizer.py sl| python trans.py > ssj500k.test.conllu
python ../conll18_ud_eval.py -v ../../datasets/sl/ssj500k/test.conllu ssj500k.test.conllu
```