from queue import Queue
from sklearn import tree
from sqlalchemy import true

class Grafo: 
    def __init__(self, numero_nodos, locaciones, dirigido=True):
        try:
            self.m_numero_nodos = numero_nodos
            self.m_dirigido = dirigido
            self.m_locaciones = locaciones
            self.m_lista_adyacencia = {nodo: set() for nodo in self.m_nodos}
        except Exception as e:  
            print(e)
    