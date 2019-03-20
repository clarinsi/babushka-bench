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
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| reldi-tagger | 994f746 | | gold | ssj500k | sl | 94.21 |     94.21 |     94.21 |
| Parser-v3 | 9ee9e8f | CLARIN.SI FT embeddings | gold | ssj500k | sl | 96.58 |     96.58 |     96.58 |
| Parser-v3 | 9ee9e8f | CLARIN.SI FT embeddings | Obeliks4J | ssj500k | sl | 96.56 |     96.55 |     96.56 |
| Parser-v3 | 9ee9e8f | CLARIN.SI FT embeddings | reldi-tokeniser | ssj500k | sl | 96.39 |     96.35 |     96.37 |
| stanfordnlp | 828ef2e | CoNLL17 embeddings | gold | ssj500k | sl | 96.45 |     96.45 |     96.45 |
| stanfordnlp | 828ef2e | CLARIN.SI FT embeddings | gold | ssj500k | sl |  96.72 |     96.72 |     96.72 |
| stanfordnlp | 828ef2e | CLARIN.SI W2V embeddings | gold | ssj500k | sl | 96.79 |     96.79 |     96.79 |
| reldi-tagger | 994f746 | | gold | hr500k | hr | 91.91 |     91.91 |     91.91 |
| Parser-v3 | 9ee9e8f | CLARIN.SI FT embeddings | gold | hr500k | hr | 94.29 |     94.29 |     94.29 |
| Parser-v3 | 9ee9e8f | CLARIN.SI FT embeddings | reldi-tokeniser | hr500k | hr | 93.89 |     93.86 |     93.87 |
| stanfordnlp | 828ef2e | CoNLL17 embeddings | gold | hr500k | hr | 93.85 |     93.85 |     93.85 |
| stanfordnlp | 828ef2e | CLARIN.SI FT embeddings | gold | hr500k | hr | 94.13 |     94.13 |     94.13 |
| stanfordnlp | 828ef2e | CLARIN.SI W2V embeddings | gold | hr500k | hr | 94.18 |     94.18 |     94.18 |
| reldi-tagger | 994f746 | | gold | SETimes.SR | sr | 92.03 |     92.03 |     92.03 |
| Parser-v3 | 9ee9e8f | CLARIN.SI FT embeddings | gold | SETimes.SR | sr | 95.12 |     95.12 |     95.12 |
| Parser-v3 | 9ee9e8f | CLARIN.SI FT embeddings | reldi-tokeniser | SETimes.SR | sr | 95.07 |     95.12 |     95.10 |
| stanfordnlp | 828ef2e | CoNLL17 (Croatian) embeddings | gold | SETimes.SR | sr | 94.78 |     94.78 |     94.78 |
| stanfordnlp | 828ef2e | CLARIN.SI FT (Croatian) embeddings| gold | SETimes.SR | sr |     94.69 |     94.69 |     94.69 |
| stanfordnlp | 828ef2e | CLARIN.SI FT (Serbian) embeddings | gold | SETimes.SR | sr |  95.23 |     95.23 |     95.23 |
| stanfordnlp | 828ef2e | CLARIN.SI W2V (Serbian) embeddings | gold | SETimes.SR | sr | 94.91 |     94.91 |     94.91 |

### Lemmatization

| tool | revision | comment | preprocessing | dataset | language | P | R | F1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| stanfordnlp | 828ef2e | | gold | ssj500k | sl | 97.75 |     97.75 |     97.75 |
| stanfordnlp | 828ef2e | | gold | hr500k | hr | 96.22 |     96.22 |     96.22 |
| stanfordnlp | 828ef2e | | gold | SETimes.SR | sr | 95.29 |     95.29 |     95.29 |
