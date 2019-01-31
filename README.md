# bench

Benchmarking NLP tools on Slovene, Croatian and Serbian

## Segmentation

### Tokens

| tool | revision | parameters | dataset | language | P | R | F1 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| reldi-tokeniser | fb85138 | -l sl | ssj500k | sl | 99.68 |     99.18 |     99.43 |
| Obeliks4J | 32266e7 | ssj500k | default | sl | 99.98 |     99.98 |     99.98 |
| reldi-tokeniser | fb85138 | -l hr | hr500k | hr | 99.57 |     99.55 |     99.56 |
| reldi-tokeniser | fb85138 | -l sr |  SETimes.SR | sr | 99.92 |     99.97 |     99.94 |

### Words

Will come later when tagging is included?

### Sentences

| tool | revision | parameters | dataset | language | P | R | F1 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| reldi-tokeniser | fb85138 | -l sl | ssj500k | sl | 97.85 |     96.49 |     97.17 |
| Obeliks4J | 32266e7 | default | ssj500k | sl | 99.09 |     99.26 |     99.18 |
| reldi-tokeniser | fb85138 | -l hr | hr500k | hr | 90.64 |     93.45 |     92.02 |
| reldi-tokeniser | fb85138 | -l sr | SETimes.SR | sr | 97.45 |     95.92 |     96.68 |

## Morphosyntactic tagging

| tool | revision | comment | segmentation | dataset | language | P | R | F1 |
| reldi-tagger | 994f746 | | | gold | ssj500k | sl | 94.21 |     94.21 |     94.21 |
| Parser-v3 | 9ee9e8f |  | gold | ssj500k | sl | 96.58 |     96.58 |     96.58 |
| Parser-v3 | 9ee9e8f |  | Obeliks4J | ssj500k | sl | 96.56 |     96.55 |     96.56 |
| Parser-v3 | 9ee9e8f |  | reldi-tokeniser | ssj500k | sl | 96.39 |     96.35 |     96.37 |
| reldi-tagger | 994f746 | | | gold | hr500k | hr | 91.91 |     91.91 |     91.91 |
| Parser-v3 | 9ee9e8f |  | gold | hr500k | hr | 94.29 |     94.29 |     94.29 |
| Parser-v3 | 9ee9e8f |  | reldi-tokeniser | hr500k | hr | 93.89 |     93.86 |     93.87 |
| reldi-tagger | 994f746 | | | gold | ssj500k | sr | 92.03 |     92.03 |     92.03 |
| Parser-v3 | 9ee9e8f |  | gold | SETimes.SR | sr | 95.12 |     95.12 |     95.12 |
| Parser-v3 | 9ee9e8f |  | reldi-tokeniser | SETimes.SR | sr | 95.07 |     95.12 |     95.10 |

## Lemmatization

