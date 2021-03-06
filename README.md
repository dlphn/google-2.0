# google-2.0

> Implementation of a search engine from scratch

This project is developed by 2 students from CentraleSupélec as part of the "Fondements en Recherche d'Information" course:
- Cécile Gontier - [@CecileSerene](https://github.com/CecileSerene)
- Delphine Shi - [@dlphn](https://github.com/dlphn)

We are working on two given collections:

- CACM collection
- CS276 collection

## Installation
When installing, create a file `config.py` in the main directory and fill with global paths to collections and path where you want the index to be stored:
```
CACM_path = '/path/to/CACM/'
CS276_path = '/path/to/pa1-data/'
index_path = '/path/to/index/'
```

## Easy testing
Go to `RunMe.ipynb` for a notebook with main results and explanations.

## Download the index
If you don't want to spend too much time generating the index, you can download it from there :
https://drive.google.com/drive/folders/17glYdz6KY_PJsnANKrYi4xooNkDQ0ua1?usp=sharing.
Be sure to replace the `index/` folder with the unzipped folder.

## Task 1: inverted index

### Linguistic processing

Entry point: `CACMIndex.py` and `CS276Index.py`. Each will calculate token size and number of vocabulary of the collection, and also draw the corresponding frequency graphs.

Helper functions:

- `textProcessing.py` processes text with language processing tools like tokenize, lemmatize, removing stop words etc.
- `indexBuilder.py` to help build each index.
- `CACMParser.py` to parse CACM document and get title, summary and key words.

Heap Law: `heapRegression.py`. Run to calculate Heap Law parameters of each collection. You will need to uncomment to change collection.

Frequency graphs: `frequencyRankGraph.py` - helper class to draw frequency graphs.


### Indexation

Entry point : `BSBI.py`.

Running this file will generate the different dictionaries (documents, terms, index) in the `index/` folder given in `config.py`.

#### Boolean search

Entry point : `boolean/booleanEvaluation.py`.

Run tests on `boolean/test.py`

#### Vectorial search

Entry point : `vectorial/vectorialEvaluation.py`.

Run tests on `vectorial/test.py`

Both search models that we implemented inherit from `evaluation.py`.

### Evaluation

Evaluate our CACM search models by running functions in `CACMEvaluation.py`.
