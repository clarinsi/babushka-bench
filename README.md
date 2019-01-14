# bench

Benchmarking NLP tools on Slovene, Croatian and Serbian

## Segmentation

### Tokens

| tool | revision | parameters | dataset | language | P | R | F1 |
| --- | --- | --- | --- | --- | --- | --- |
| reldi-tokeniser | fb85138 | -l sl | ssj500k | sl | 99.67 | 99.17 | 99.42 |
| Obeliks4J | 32266e7 | ssj500k | default | sl | 99.94 | 99.95 | 99.95 |

### Words

Will come later when tagging is included?

### Sentences

| tool | revision | parameters | dataset | language | P | R | F1 |
| --- | --- | --- | --- | --- | --- | --- |
| reldi-tokeniser | fb85138 | -l sl | ssj500k | sl | 96.57 | 93.85 | 95.19 |
| Obeliks4J | 32266e7 | default | ssj500k | sl | 97.11 | 96.02 | 96.56 |

## Morphosyntactic tagging

## Lemmatization

