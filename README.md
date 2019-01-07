# google-2.0

> Implementation of a search engine from scratch

This project is developed by 2 students from CentraleSupélec as part of the "Fondements en Recherche d'Information" course:
- Cécile Gontier - [cecile.gontier@student.ecp.fr](mailto:cecile.gontier@student.ecp.fr) - [@CecileSerene](https://github.com/CecileSerene)
- Delphine Shi - [delphine.shi@student.ecp.fr](mailto:delphine.shi@student.ecp.fr) - [@dlphn](https://github.com/dlphn)

We are working on two given collections:

- CACM collection
- CS276 collection

## Task 1: inverted index

### Linguistic processing

Entry point: `CACMIndex.py` and `CS276Index.py`.

Helper functions:

- `textProcessing.py`
- `indexBuilder.py`
- `CACMParser.py`

Heap Law: `heapRegression.py`

Frequency graphs: `frequencyRankGraph.py`


### Indexation

Entry point : `BSBIndex.py`.

Running this file will generate the different dictionaries (documents, terms, index) in the `index/` folder.

#### Boolean search

Entry point : `boolean/booleanEvaluation.py`.
