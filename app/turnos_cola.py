if __package__:
    from app.clientes_lista import Cliente
else:
    from clientes_lista import Cliente


class NodoTurno:
    """Nodo que almacena un cliente dentro de la cola de turnos."""

    def __init__(self, cliente):
        self.cliente = cliente
        self.siguiente = None


class ColaTurnos:
    """Cola enlazada que atiende clientes en orden de llegada."""

    def __init__(self):
        self.head = None
        self.tail = None
        self.cantidad = 0

    def esta_vacia(self):
        """Indica si la cola no contiene turnos."""
        # Complejidad temporal: O(1)
        return self.head is None

    def enqueue(self, cliente):
        """Agrega un cliente al final de la cola."""
        # Complejidad temporal: O(1)
        nuevo_nodo = NodoTurno(cliente)

        if self.esta_vacia():
            self.head = nuevo_nodo
        else:
            self.tail.siguiente = nuevo_nodo

        self.tail = nuevo_nodo
        self.cantidad += 1

    def dequeue(self):
        """Retira y devuelve al primer cliente de la cola."""
        # Complejidad temporal: O(1)
        if self.esta_vacia():
            return None

        cliente_atendido = self.head.cliente
        self.head = self.head.siguiente
        self.cantidad -= 1

        if self.head is None:
            self.tail = None

        return cliente_atendido

    def ver_siguiente(self):
        """Devuelve el siguiente cliente sin retirarlo de la cola."""
        # Complejidad temporal: O(1)
        if self.esta_vacia():
            return None

        return self.head.cliente

    def mostrar_turnos(self):
        """Devuelve los clientes en su orden de atención."""
        # Complejidad temporal: O(n)
        clientes = []
        actual = self.head

        while actual is not None:
            clientes.append(actual.cliente)
            actual = actual.siguiente

        return clientes

    def __len__(self):
        """Devuelve la cantidad de turnos pendientes."""
        # Complejidad temporal: O(1)
        return self.cantidad


if __name__ == "__main__":
    # Prueba independiente de la cola enlazada de turnos.
    cola = ColaTurnos()

    cola.enqueue(Cliente("0102030405", "Ana"))
    cola.enqueue(Cliente("0912345678", "Pedro"))

    print("TURNOS PENDIENTES")
    for cliente in cola.mostrar_turnos():
        print(cliente)

    cliente_atendido = cola.dequeue()
    print("\nCLIENTE ATENDIDO")
    print(cliente_atendido)

    print("\nTURNOS PENDIENTES DESPUES DE ATENDER")
    for cliente in cola.mostrar_turnos():
        print(cliente)
