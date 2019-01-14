```
cat ../../datasets/sl/ssj500k/test.txt | java -cp [...]/Obeliks4J/target/classes org.obeliks.Tokenizer | python trans.py > ssj500k.test.conllu
```

## Error analysis on the training portion

```
cat ../../datasets/sl/ssj500k/train.txt | java -cp [...]/Obeliks4J/target/classes org.obeliks.Tokenizer | python trans.py > ssj500k.train.conllu
diff <(cut -f 2 ssj500k.train.conllu) <(grep -v '^#' ../../datasets/sl/ssj500k/train.conllu | cut -f 2) | less
```
