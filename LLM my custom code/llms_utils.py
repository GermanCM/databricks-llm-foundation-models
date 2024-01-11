import logging
logging.basicConfig(level=logging.ERROR)

import torch
import torch.nn as nn
import torch.nn.functional as F
import math
import time
import numpy as np


class TextUtils:
    def __init__(self):
        # Inicialización de la clase
        pass

    def build_word2id_dict(self, text):
        try:
            word2id = {word: i for i, word in enumerate(set(text.split()))}
            self.word2id = word2id
            return word2id
        except ValueError as ve:
            logging.error("ValueError occurred at build_word2id_dict: %s", str(ve))
            return None
        except Exception as e:
            logging.error("An error occurred at build_word2id_dict: %s", str(e))
            return None

        def remove_stopwords(self, text):
            # Función para eliminar las palabras vacías (stopwords)
            pass


# Define a sentence and a simple word2id mapping
sentence = "The quick brown fox jumps over the lazy dog"
word2id = {word: i for i, word in enumerate(set(sentence.split()))}

# Convert text to indices
input_ids = torch.tensor([word2id[word] for word in sentence.split()])
print(input_ids)
# Define a simple word embedding function
def get_word_embeddings(input_ids, embedding_size):
    embedding_layer = nn.Embedding(input_ids.max() + 1, embedding_size)
    return embedding_layer(input_ids)


