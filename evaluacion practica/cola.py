# Nodo individual de la lista
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

# Cola usando lista enlazada
class Cola:
    def __init__(self):
        self.frente = None  # Frente de la cola (el que se va primero)
        self.final = None   # Final de la cola (el que se agrega)
    
    # Agregar elemento (enqueue)
    def encolar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.esta_vacia():
            self.frente = self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo

    # Eliminar elemento (dequeue)
    def desencolar(self):
        if self.esta_vacia():
            raise Exception("Cola vacía")
        valor = self.frente.valor
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        return valor

    # Ver si está vacía
    def esta_vacia(self):
        return self.frente is None

    # Mostrar contenido de la cola
    def mostrar(self):
        actual = self.frente
        elementos = []
        while actual:
            elementos.append(actual.valor)
            actual = actual.siguiente
        return elementos


