# Error analysis

```
paste  <(grep -v '^#' ../datasets/sl/ssj500k/test.conllu|cut -f 3,4,6) <(cut -f 3 reldi-tagger/ssj500k.test.conllu) <(cut -f 3 stanfordnlp/ssj500k.test.lex.conllu) | awk '{if ($4!=$5) print $0}'|less

paste  <(grep -v '^#' ../../stanfordnlp/out/pos.ssj500k.test.conllu|cut -f 2,3,4,6) <(cut -f 3 reldi-tagger/ssj500k.test.stanfordnlp.conllu) <(cut -f 3 ../../stanfordnlp/out/lemma.my_ssj500k+lex.test.conllu) | awk '{if ($2!=$5 || $2!=$6) print $0}'|less
```
