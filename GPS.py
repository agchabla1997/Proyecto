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

    def agregar_sector(self, nodo1, nodo2, peso=1):
        try:
            self.m_lista_adyacencia[nodo1].add((nodo2, peso))
            if not self.m_dirigido:
                self.m_lista_adyacencia[nodo2].add((nodo1, peso))
        except Exception as e:
            print(e)   
    
    def dfs(self, inicio, final, recorrido = [], visitado = set()):
        try:
            visitado.add(inicio)
            recorrido.append(self.m_locaciones[inicio])
        except Exception as e:
            print(e)
        
        try:
            if inicio == final:
                return recorrido
            for(vecino, peso) in self.m_lista_adyacencia[inicio]:
                if vecino not in visitado:
                    resultado = self.dfs(vecino, final, recorrido, visitado) 
                    if resultado is not None:
                        return resultado 
        except Exception as e:
            print(e)
        
        try:
            recorrido.pop()
            return None
        except Exception as e:
            print(e)

