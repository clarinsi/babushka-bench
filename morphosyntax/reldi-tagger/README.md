```
grep -v '^#' ../../datasets/sl/ssj500k/test.conllu | cut -f 2 | python /home/nikola/tools/clarinsi/reldi-tagger/tagger.py ssj500k | python trans.py > ssj500k.test.conllu
grep -v '^#' ../../datasets/hr/hr500k/test.conllu | cut -f 2 | python /home/nikola/tools/clarinsi/reldi-tagger/tagger.py hr500k | python trans.py > hr500k.test.conllu
grep -v '^#' ../../datasets/sr/SETimes.SR/test.conllu | cut -f 2 | python /home/nikola/tools/clarinsi/reldi-tagger/tagger.py SETimes.SR | python trans.py > SETimes.SR.test.conllu
python ../conll18_ud_eval.py -v ../../datasets/sl/ssj500k/test.conllu ssj500k.test.conllu
python ../conll18_ud_eval.py -v ../../datasets/hr/hr500k/test.conllu hr500k.test.conllu
python ../conll18_ud_eval.py -v ../../datasets/sr/SETimes.SR/test.conllu SETimes.SR.test.conllu
```