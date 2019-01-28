# bench

Benchmarking NLP tools on Slovene, Croatian and Serbian

## Segmentation

### Tokens

| tool | revision | parameters | dataset | language | P | R | F1 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| reldi-tokeniser | fb85138 | -l sl | ssj500k | sl | 99.68 |     99.18 |     99.43 |
| Obeliks4J | 32266e7 | ssj500k | default | sl | 99.98 |     99.98 |     99.98 |
| reldi-tokeniser | fb85138 | -l hr | hr500k | hr | 99.57 |     99.55 |     99.56 |
| reldi-tokeniser | fb85138 | -l sr |  SETimes.SR | sr | 99.92 |     99.97 |     99.94 |

### Words

Will come later when tagging is included?

### Sentences

| tool | revision | parameters | dataset | language | P | R | F1 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| reldi-tokeniser | fb85138 | -l sl | ssj500k | sl | 97.85 |     96.49 |     97.17 |
| Obeliks4J | 32266e7 | default | ssj500k | sl | 99.09 |     99.26 |     99.18 |
| reldi-tokeniser | fb85138 | -l hr | hr500k | hr | 84.30 |     78.18 |     81.13 |
| reldi-tokeniser | fb85138 | -l sr | SETimes.SR | sr | 92.67 |     87.15 |     89.82 |

## Morphosyntactic tagging

## Lemmatization

