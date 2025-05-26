"""✓ Ejercicio #1: Inversión de palabras en una frase. Desarrolle un programa que
utilice una pila para invertir el orden de las palabras en una frase dada. Por ejemplo,
la frase "Hola mundo desde UAM" debería invertirse a "UAM desde mundo Hola"."""

# Nodo para la lista enlazada
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

# Pila (Stack) implementation usando listas enlazadas
class Pila:
    def __init__(self):
        self._cima_nodo = None  # Cambiamos _items por _cima_nodo que apunta al nodo superior

    def esta_vacia(self):
        return self._cima_nodo is None

    def apilar(self, item):
        nuevo_nodo = Nodo(item)
        nuevo_nodo.siguiente = self._cima_nodo
        self._cima_nodo = nuevo_nodo

    def desapilar(self):
        if not self.esta_vacia():
            valor_desapilado = self._cima_nodo.valor
            self._cima_nodo = self._cima_nodo.siguiente
            return valor_desapilado
        return None # devuelve dato vacio si no hay elementos en la pila

    def cima(self):
        return self._cima_nodo # Ensures the actual top node is returned




