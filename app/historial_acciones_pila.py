class NodoAccion:
    """Nodo que almacena una accion dentro de la pila."""

    def __init__(self, accion):
        self.accion = accion
        self.siguiente = None


class HistorialAccionesPila:
    """Pila enlazada para guardar el historial de acciones del operador."""

    def __init__(self):
        self.cima = None
        self.cantidad = 0

    def esta_vacia(self):
        """Indica si la pila no contiene acciones."""
        # Complejidad temporal: O(1)
        return self.cima is None

    def push(self, accion):
        """Agrega una accion en la cima de la pila."""
        # Complejidad temporal: O(1)
        nuevo_nodo = NodoAccion(accion)
        nuevo_nodo.siguiente = self.cima
        self.cima = nuevo_nodo
        self.cantidad += 1

    def pop(self):
        """Retira y devuelve la ultima accion registrada."""
        # Complejidad temporal: O(1)
        if self.esta_vacia():
            return None

        accion_eliminada = self.cima.accion
        self.cima = self.cima.siguiente
        self.cantidad -= 1
        return accion_eliminada

    def ver_ultima_accion(self):
        """Devuelve la accion de la cima sin retirarla."""
        # Complejidad temporal: O(1)
        if self.esta_vacia():
            return None

        return self.cima.accion

    def mostrar_historial(self):
        """Devuelve las acciones desde la mas reciente hasta la mas antigua."""
        # Complejidad temporal: O(n)
        acciones = []
        actual = self.cima

        while actual is not None:
            acciones.append(actual.accion)
            actual = actual.siguiente

        return acciones

    def __len__(self):
        """Devuelve la cantidad de acciones almacenadas."""
        # Complejidad temporal: O(1)
        return self.cantidad


if __name__ == "__main__":
    # Prueba independiente de la pila de acciones.
    historial = HistorialAccionesPila()

    historial.push("Se registro el turno de Ana")
    historial.push("Se atendio el turno de Pedro")

    print("HISTORIAL DE ACCIONES")
    for accion in historial.mostrar_historial():
        print(accion)

    accion_eliminada = historial.pop()
    print("\nULTIMA ACCION RETIRADA")
    print(accion_eliminada)

    print("\nHISTORIAL ACTUAL")
    for accion in historial.mostrar_historial():
        print(accion)
