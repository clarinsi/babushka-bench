```
python [...]/reldi-tokeniser/tokeniser.py sl < ../../datasets/sl/ssj500k/test.txt | python trans.py > ssj500k.test.conllu
```

## Error analysis on the training portion

```
python [...]/reldi-tokeniser/tokeniser.py sl < ../../datasets/sl/ssj500k/train.txt | python trans.py > ssj500k.train.conllu
diff <(cut -f 2 ssj500k.train.conllu) <(grep -v '^#' ../../datasets/sl/ssj500k/train.conllu | cut -f 2) | less
```
