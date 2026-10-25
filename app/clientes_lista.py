class Cliente:
    """Representa un cliente registrado en el taller."""

    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre

    def __str__(self):
        return f"DNI: {self.dni} - Nombre: {self.nombre}"


class NodoCliente:
    """Nodo utilizado para construir la lista simplemente enlazada."""

    def __init__(self, cliente):
        self.cliente = cliente
        self.siguiente = None


class ClientesLista:
    """Lista simplemente enlazada de clientes registrados."""

    def __init__(self):
        self.cabeza = None
        self.cantidad = 0

    def esta_vacia(self):
        """Indica si la lista no contiene clientes."""
        # Complejidad temporal: O(1)
        return self.cabeza is None

    def agregar(self, dni, nombre):
        """Agrega un cliente al final de la lista."""
        # Complejidad temporal: O(n)
        nuevo_cliente = Cliente(dni, nombre)
        nuevo_nodo = NodoCliente(nuevo_cliente)

        if self.esta_vacia():
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza

            while actual.siguiente is not None:
                actual = actual.siguiente

            actual.siguiente = nuevo_nodo

        self.cantidad += 1
        return nuevo_cliente

    def buscar_por_nombre(self, nombre):
        """Busca el primer cliente cuyo nombre coincida."""
        # Complejidad temporal: O(n)
        actual = self.cabeza

        while actual is not None:
            if actual.cliente.nombre.lower() == nombre.lower():
                return actual.cliente

            actual = actual.siguiente

        return None

    def mostrar_clientes(self):
        """Devuelve todos los clientes en su orden de registro."""
        # Complejidad temporal: O(n)
        clientes = []
        actual = self.cabeza

        while actual is not None:
            clientes.append(actual.cliente)
            actual = actual.siguiente

        return clientes

    def __len__(self):
        """Devuelve la cantidad de clientes registrados."""
        # Complejidad temporal: O(1)
        return self.cantidad


if __name__ == "__main__":
    # Prueba independiente de la lista enlazada de clientes.
    lista = ClientesLista()

    lista.agregar("0102030405", "Ana")
    lista.agregar("0912345678", "Pedro")

    print("CLIENTES REGISTRADOS")
    for cliente in lista.mostrar_clientes():
        print(cliente)

    nombre_buscado = "Ana"
    cliente_encontrado = lista.buscar_por_nombre(nombre_buscado)

    print(f"\nBUSQUEDA: {nombre_buscado}")
    if cliente_encontrado is not None:
        print("Cliente encontrado:", cliente_encontrado)
    else:
        print("Cliente no encontrado")
