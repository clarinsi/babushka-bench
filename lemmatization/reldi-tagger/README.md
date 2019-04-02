```
grep -v '^#' ../../datasets/sl/ssj500k/test.conllu | cut -f 2,5 | python /home/nikola/tools/clarinsi/reldi-tagger/lemmatizer.py sl| python trans.py > ssj500k.test.conllu
python ../conll18_ud_eval.py -v ../../datasets/sl/ssj500k/test.conllu ssj500k.test.conllu
grep -v '^#' ../../morphosyntax/reldi-tagger/ssj500k.test.conllu | cut -f 2,5 | python /home/nikola/tools/clarinsi/reldi-tagger/lemmatizer.py sl| python trans.py > ssj500k.test.reldi-tagger.conllu
python ../conll18_ud_eval.py -v ../../datasets/sl/ssj500k/test.conllu ssj500k.test.reldi-tagger.conllu
grep -v '^#' ../../morphosyntax/stanfordnlp/ssj500k.test.emb_clarinft.conllu | cut -f 2,5 | python /home/nikola/tools/clarinsi/reldi-tagger/lemmatizer.py sl| python trans.py > ssj500k.test.stanfordnlp.conllu
python ../conll18_ud_eval.py -v ../../datasets/sl/ssj500k/test.conllu ssj500k.test.stanfordnlp.conllu

grep -v '^#' ../../datasets/hr/hr500k/test.conllu | cut -f 2,5 | python /home/nikola/tools/clarinsi/reldi-tagger/lemmatizer.py hr| python trans.py > hr500k.test.conllu
python ../conll18_ud_eval.py -v ../../datasets/hr/hr500k/test.conllu hr500k.test.conllu
grep -v '^#' ../../morphosyntax/reldi-tagger/hr500k.test.conllu | cut -f 2,5 | python /home/nikola/tools/clarinsi/reldi-tagger/lemmatizer.py hr| python trans.py > hr500k.test.reldi-tagger.conllu
python ../conll18_ud_eval.py -v ../../datasets/hr/hr500k/test.conllu hr500k.test.reldi-tagger.conllu
grep -v '^#' ../../morphosyntax/stanfordnlp/hr500k.test.emb_clarinft.conllu | cut -f 2,5 | python /home/nikola/tools/clarinsi/reldi-tagger/lemmatizer.py hr| python trans.py > hr500k.test.stanfordnlp.conllu
python ../conll18_ud_eval.py -v ../../datasets/hr/hr500k/test.conllu hr500k.test.stanfordnlp.conllu

grep -v '^#' ../../datasets/sr/SETimes.SR/test.conllu | cut -f 2,5 | python /home/nikola/tools/clarinsi/reldi-tagger/lemmatizer.py sr| python trans.py > SETimes.SR.test.conllu
python ../conll18_ud_eval.py -v ../../datasets/sr/SETimes.SR/test.conllu SETimes.SR.test.conllu
grep -v '^#' ../../morphosyntax/reldi-tagger/SETimes.SR.test.conllu | cut -f 2,5 | python /home/nikola/tools/clarinsi/reldi-tagger/lemmatizer.py sr| python trans.py > SETimes.SR.test.reldi-tagger.conllu
python ../conll18_ud_eval.py -v ../../datasets/sr/SETimes.SR/test.conllu SETimes.SR.test.reldi-tagger.conllu
grep -v '^#' ../../morphosyntax/stanfordnlp/SETimes.SR.test.emb_clarinft.conllu | cut -f 2,5 | python /home/nikola/tools/clarinsi/reldi-tagger/lemmatizer.py sr| python trans.py > SETimes.SR.test.stanfordnlp.conllu
python ../conll18_ud_eval.py -v ../../datasets/sr/SETimes.SR/test.conllu SETimes.SR.test.stanfordnlp.conllu
```
