
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
| Obeliks | | | gold | ssj500k | sl | 92.67 |     92.67 |     92.67 |
| meta-tagger | | | gold | ssj500k | sl | 94.34 | 94.34 | 94.34 |
| Parser-v3 | 9ee9e8f | CLARIN.SI FT embeddings | gold | ssj500k | sl | 96.58 |     96.58 |     96.58 |
| Parser-v3 | 9ee9e8f | CLARIN.SI FT embeddings | Obeliks4J | ssj500k | sl | 96.56 |     96.55 |     96.56 |
| Parser-v3 | 9ee9e8f | CLARIN.SI FT embeddings | reldi-tokeniser | ssj500k | sl | 96.39 |     96.35 |     96.37 |
| stanfordnlp | 828ef2e | CoNLL17 embeddings | gold | ssj500k | sl | 96.45 |     96.45 |     96.45 |
| stanfordnlp | 828ef2e | CLARIN.SI FT embeddings | gold | ssj500k | sl |  96.72 |     96.72 |     96.72 |
| stanfordnlp | 828ef2e | CLARIN.SI W2V embeddings | gold | ssj500k | sl | 96.79 |     96.79 |     96.79 |
| stanfordnlp |  828ef2e | CLARIN.SI FT embeddings | gold | ssj500k_ud | sl | 95.65 |     95.65 |     95.65 |
| reldi-tagger | 994f746 | | gold | hr500k | hr | 91.91 |     91.91 |     91.91 |
| Parser-v3 | 9ee9e8f | CLARIN.SI FT embeddings | gold | hr500k | hr | 94.29 |     94.29 |     94.29 |
| Parser-v3 | 9ee9e8f | CLARIN.SI FT embeddings | reldi-tokeniser | hr500k | hr | 93.89 |     93.86 |     93.87 |
| stanfordnlp | 828ef2e | CoNLL17 embeddings | gold | hr500k | hr | 93.85 |     93.85 |     93.85 |
| stanfordnlp | 828ef2e | CLARIN.SI FT embeddings | gold | hr500k | hr | 94.13 |     94.13 |     94.13 |
| stanfordnlp | 828ef2e | CLARIN.SI W2V embeddings | gold | hr500k | hr | 94.18 |     94.18 |     94.18 |
| stanfordnlp | 828ef2e | CLARIN.SI FT embeddings | gold | hr500k_ud | hr | 94.60 |     94.60 |     94.60 |
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
| reldi-tagger | 994f746 | | gold | ssj500k | sl | 99.46 |     99.46 |     99.46 |
| reldi-tagger | 994f746 | | gold segmentation, reldi-tagger | ssj500k | sl | 98.35 |     98.35 |     98.35 |
| reldi-tagger | 994f746 | | gold segmentation, stanfordnlp | ssj500k | sl | 98.77 |     98.77 |     98.77 |
| Obeliks | | | gold segmentation, Obeliks | ssj500k | sl | 98.19 |     98.19 |     98.19 |
| meta-tagger | | | gold segmentation, meta-tagger | ssj500k | sl | 98.66 |     98.66 |     98.66 |
| stanfordnlp | 828ef2e | | gold | ssj500k | sl | 97.75 |     97.75 |     97.75 |
| stanfordnlp | 828ef2e | | gold segmentation, stanfordnlp | ssj500k | sl | 97.51 |     97.51 |     97.51 |
| classla-stanfordnlp |  | | gold | ssj500k | sl | 99.63 | 99.63 | 99.63 |
| classla-stanfordnlp |  | | gold segmentation, stanfordnlp | ssj500k | sl | 99.02 | 99.02 |  99.02 |
| reldi-tagger | 994f746 | | gold | hr500k | hr |98.17 |     98.17 |     98.17 |
| reldi-tagger | 994f746 | | gold segmentaton, reldi-tagger | hr500k | hr | 96.82 |     96.82 |     96.82 |
| reldi-tagger | 994f746 | | gold segmentation, stanfordnlp | hr500k | hr | 97.22 |     97.22 |     97.22 |
| stanfordnlp | 828ef2e | | gold | hr500k | hr | 96.22 |     96.22 |     96.22 |
| stanfordnlp | 828ef2e | | gold segmentation, stanfordnlp | hr500k | hr | 95.85 |     95.85 |     95.85 |
| classla-stanfordnlp | 56c7241 | | gold | hr500k | hr | 98.57 | 98.57 | 98.57 |
| classla-stanfordnlp | 56c7241 | | gold segmentation, stanfordnlp | hr500k | hr | 97.60 | 97.60 | 97.60 |
| reldi-tagger | 994f746 | | gold | SETimes.SR | sr | 97.89 |     97.89 |     97.89 |
| reldi-tagger | 994f746 | | gold segmentation, reldi-tagger | SETimes.SR | sr | 96.44 |     96.44 |     96.44 |
| reldi-tagger | 994f746 | | gold segmentation, stanfordnlp | SETimes.SR | sr | 97.26 |     97.26 |     97.26 |
| stanfordnlp | 828ef2e | | gold | SETimes.SR | sr | 95.29 |     95.29 |     95.29 |
| stanfordnlp | 828ef2e | | gold segmentation, stanfordnlp | SETimes.SR | sr | 95.18 |     95.18 |     95.18 |
| classla-stanfordnlp | 56c7241 | | gold | SETimes.SR | sr | 98.49 | 98.49 | 98.49 |
| classla-stanfordnlp | 56c7241 | | gold segmentation, stanfordnlp | SETimes.SR | sr | 97.89 | 97.89 | 97.89 |

### Parsing

| tool | revision | comment | preprocessing | dataset | language | P | R | F1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| classla-stanfordnlp | 56c7241 | | gold segmentation, classla-stanfordnlp | ssj500k | sl | 92.68 | 92.68 | 92.68 |
| classla-stanfordnlp | 56c7241 | | gold | ssj500k | sl | 94.19 | 94.19 | 94.19 |
| classla-stanfordnlp | 56c7241 | | gold segmentation, classla-stanfordnlp | hr500k | hr | 85.86 | 85.86 | 85.86 |
| classla-stanfordnlp | 56c7241 | | gold | hr500k | hr | 86.64 | 86.64 | 86.64 |
| classla-stanfordnlp | 56c7241 | | gold segmentation, classla-stanfordnlp | SETimes.SR | sr | 88.96 | 88.96 | 88.96 |
| classla-stanfordnlp | 56c7241 | | gold | SETimes.SR | sr | 90.20 | 90.20 | 90.20 |
