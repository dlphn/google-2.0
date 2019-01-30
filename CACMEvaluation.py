from BSBIndex import BSBIndex
from CACMIndex import CACMIndex
import config

import time
import os
from hurry.filesize import size

def index_creation_time():
    start = time.time()
    cacm = CACMIndex()
    cacm.build()
    index = BSBIndex('CACM', cacm.get_term_dict(), cacm.get_document_dict())
    index.build()
    end = time.time()

    return end-start

def get_file_size(filename):
    return size(os.path.getsize(config.index_path +"/"+ filename))


# print("The index is created in {}".format(index_creation_time()))
print("the index has a size {}".format(get_file_size("index_CACM.json")))


# Performance : temps de calcul indexation, temps de réponse requete, espace disque index

# Pertinence : precision, rappel, F mesure, E mesure, R mesure, Mean average precision
