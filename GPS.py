from queue import Queue
from sklearn import tree
from sqlalchemy import true

class Grafo: 
    def __init__(self, numero_nodos, locaciones, dirigido=True):
        try:
            self.m_numero_nodos = numero_nodos
            self.m_nodos = range(self.m_numero_nodos)
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


if __name__ == "__main__":
    try:
        locaciones = {0:"URB. EMMANUEL",1:"URB. SAN JUAN",2:"LOT. VOLUNTAD DE DIOS",3:"LOTIZACION 2000",4:"COOP. LAS PLAYAS No. 1",
        5:"URB. BARRAGAN",6:"BARRIO 4 DE ABRIL",7:"BARRIO 25 DE DICIEMBRE", 8:"COMITE DE VIV. ROSITA DE SARON", 9:"LAS ALBORADA", 
        10:"COOP. 30 DE JUNIO", 11:"BARRIO EL MIRADOR", 12:"LAS PLAYAS 4", 13:"COOP. LAURA FLORES", 14:"ASENT. COSTA AZUL", 
        15:"NUEVA ESPERANZA", 16:"LAS ACACIAS", 17:"COOP. MODELO", 18:"PROVINCIAS UNIDAS", 19:"CAMINO AL FUTURO "}

        gps = Grafo(20, locaciones)

        gps.agregar_sector(0, 1, 0.7)
        gps.agregar_sector(1, 2, 0.9) 
        gps.agregar_sector(2, 3, 1.2) 
        gps.agregar_sector(2, 6, 1.8)
        gps.agregar_sector(2, 7, 1.3)
        gps.agregar_sector(3, 4, 0.9)
        gps.agregar_sector(4, 5, 1.2)
        gps.agregar_sector(4, 9, 2.2)
        gps.agregar_sector(6, 8, 1.9)
        gps.agregar_sector(7, 11, 2.6)
        gps.agregar_sector(8, 9, 1.3)
        gps.agregar_sector(8, 12, 2.4)
        gps.agregar_sector(9, 10, 1.4)
        gps.agregar_sector(10, 16, 2.3)
        gps.agregar_sector(11, 13, 1.9)
        gps.agregar_sector(12, 14, 1.6)
        gps.agregar_sector(13, 14, 1.2) 
        gps.agregar_sector(14, 15, 1.1) 
        gps.agregar_sector(15, 16, 1.3) 
        gps.agregar_sector(15, 19, 2.4) 
        gps.agregar_sector(16, 17, 1.1)
        gps.agregar_sector(19, 18, 1.7) 
        gps.agregar_sector(19, 17, 1.3)

        while(True):
            print("*** Menú de GPS ***")

            print("1. Observar sectores de Entrega")
            print("2. Analizar recorrido")
            print("3. Salir")

            menu = int(input("Ingrese una Opción: "))

            if menu == 1:
                print(locaciones)
            elif(menu == 2):
                gps_recorrido = []

                while true:
                    punto_partida = int(input("Ingrese su punto de Partida: "))
                    punto_llegada = int(input("Ingrese el sector de llegada: "))
                    if(punto_partida >= 0 and punto_partida <= 19 and punto_llegada >= 0 and punto_llegada <= 19):
                        gps_recorrido = gps.dfs(punto_partida, punto_llegada)
                        print(f"Esta es la mejor ruta:  {gps_recorrido}")
                        break
                    else:
                        print("No exíste el sector ingresado, porfavor revise en la opcion 1 los sectores existentes ")
            elif menu == 3:
                break
            else:
                print("Por favor ingrese una Opción válida")
    except Exception as e:
        print(e)        