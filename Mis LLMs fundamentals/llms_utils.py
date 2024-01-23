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
        """
        Construye un diccionario que mapea palabras a sus índices correspondientes.

        Args:
            text (str): El texto del cual se construirá el diccionario.

        Returns:
            dict or None: Un diccionario que mapea palabras a sus índices correspondientes, o None si ocurre un error.

        Raises:
            ValueError: Si ocurre un ValueError durante la construcción del diccionario.
            Exception: Si ocurre cualquier otra excepción durante la construcción del diccionario.
        """
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

    
    def convert_text_to_indices(self, sentence):
        """
        Convierte un texto en una secuencia de índices utilizando un diccionario de palabras a índices.

        Args:
            sentence (str): El texto a convertir en índices.

        Returns:
            torch.Tensor or None: Un tensor de PyTorch que contiene la secuencia de índices correspondiente al texto,
            o None si ocurre un error durante la conversión.

        Raises:
            KeyError: Si una palabra en el texto no está presente en el diccionario.
            Exception: Si ocurre cualquier otra excepción durante la conversión del texto a índices.
        """
        try:
            word2id = self.get_word2id_dict()  # Llamada a la función que devuelve el diccionario word2id
            input_ids = torch.tensor([word2id[word] for word in sentence.split()])
            return input_ids
        except KeyError as ke:
            print("Error: La palabra '{}' no está presente en el diccionario.".format(str(ke)))
            return None
        except Exception as e:
            print("Error: Se produjo un error durante la conversión del texto a índices:", str(e))
            return None
        
    def get_word_embeddings(self, input_ids, embedding_size):
        """
        Obtiene las representaciones vectoriales de las palabras utilizando una capa de embedding.

        Args:
            input_ids (torch.Tensor): Los índices de las palabras.
            embedding_size (int): El tamaño de las representaciones vectoriales.

        Returns:
            torch.Tensor: Las representaciones vectoriales de las palabras.

        """
        try:
            embedding_layer = nn.Embedding(input_ids.max() + 1, embedding_size)
            return embedding_layer(input_ids)

        except Exception as e:
            print("An error occurred at get_word_embeddings: %s", str(e))
            return None
