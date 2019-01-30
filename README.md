# google-2.0

> Implementation of a search engine from scratch

This project is developed by 2 students from CentraleSupélec as part of the "Fondements en Recherche d'Information" course:
- Cécile Gontier - [@CecileSerene](https://github.com/CecileSerene)
- Delphine Shi - [delphine.shi@student.ecp.fr](mailto:delphine.shi@student.ecp.fr) - [@dlphn](https://github.com/dlphn)

We are working on two given collections:

- CACM collection
- CS276 collection

## Installation
When installing, create a file `config.py` in main directory and fill with global path to colections and path where you want the index to be stored:
```
CACM_path = '/path/to/CACM'
CS276_path = '/path/to/pa1-data'
index_path = '/path/to/index'
```

## Task 1: inverted index

### Linguistic processing

Entry point: `CACMIndex.py` and `CS276Index.py`. Each will calculate token size and number of vocabulary of the collection, and also draw the corresponding frequency graphs.

Helper functions:

- `textProcessing.py` Process text with langage processing tools like tokenize, lemmatize, removing stop words etc.
- `indexBuilder.py` To help build each index.
- `CACMParser.py` tTo parse CACM document and get title, summary and key words.

Heap Law: `heapRegression.py` Run to calculate Heap Law parameters of each collection. You will need to uncomment to change collection.

Frequency graphs: `frequencyRankGraph.py` Helper class to draw frequency graphs.


### Indexation

Entry point : `BSBIndex.py`.

Running this file will generate the different dictionaries (documents, terms, index) in the `index/` folder given in `config.py`.

#### Boolean search

Entry point : `boolean/booleanEvaluation.py`.

Run tests on `boolean/test.py`

#### Vectorial search

Entry point : `vectorial/vectorialEvaluation.py`.

Run tests on `vectorial/test.py`

Both search models that we implemented inherit from `evaluation.py`.

