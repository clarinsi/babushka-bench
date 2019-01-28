```
python [...]/reldi-tokeniser/tokeniser.py sl < ../../datasets/sl/ssj500k/test.txt | python trans.py > ssj500k.test.conllu
python [...]/reldi-tokeniser/tokeniser.py hr < ../../datasets/hr/hr500k/test.txt | python trans.py > hr500k.test.conllu
python [...]/reldi-tokeniser/tokeniser.py sr < ../../datasets/sr/SETimes.SR/test.txt | python trans.py > SETimes.SR.test.conllu
```

## Error analysis on the training portion, example on ssj500k

```
python [...]/reldi-tokeniser/tokeniser.py sl < ../../datasets/sl/ssj500k/train.txt | python trans.py > ssj500k.train.conllu
diff <(cut -f 2 ssj500k.train.conllu) <(grep -v '^#' ../../datasets/sl/ssj500k/train.conllu | cut -f 2) | less
```
