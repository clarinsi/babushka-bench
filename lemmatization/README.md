# Error analysis

```
paste  <(grep -v '^#' ../datasets/sl/ssj500k/test.conllu|cut -f 3,4,6) <(cut -f 3 reldi-tagger/ssj500k.test.conllu) <(cut -f 3 stanfordnlp/ssj500k.test.lex.conllu) | awk '{if ($4!=$5) print $0}'|less
```