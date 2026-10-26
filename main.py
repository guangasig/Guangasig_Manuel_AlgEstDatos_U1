from app.clientes_lista import ClientesLista
from app.historial_acciones_pila import HistorialAccionesPila
from app.turnos_cola import ColaTurnos


def mostrar_menu():
    """Muestra las opciones disponibles en el sistema."""
    print("\nGESTOR DE TURNOS CARUPS")
    print("1. Registrar cliente y turno")
    print("2. Atender siguiente turno")
    print("3. Buscar cliente por nombre")
    print("4. Mostrar clientes registrados")
    print("5. Mostrar turnos pendientes")
    print("6. Mostrar historial de acciones")
    print("7. Deshacer ultima accion del historial")
    print("0. Salir")


def registrar_turno(clientes, turnos, historial):
    """Registra un cliente y lo agrega a la cola de turnos."""
    dni = input("Ingrese el DNI del cliente: ").strip()
    nombre = input("Ingrese el nombre del cliente: ").strip()

    if not dni or not nombre:
        print("El DNI y el nombre son obligatorios.")
        return

    cliente = clientes.agregar(dni, nombre)
    turnos.enqueue(cliente)
    historial.push(f"Se registro el turno de {cliente.nombre} con DNI {cliente.dni}")

    print("Turno registrado correctamente:", cliente)


def atender_turno(turnos, historial):
    """Atiende al primer cliente que ingreso en la cola."""
    cliente = turnos.dequeue()

    if cliente is None:
        print("No existen turnos pendientes.")
        return

    historial.push(f"Se atendio el turno de {cliente.nombre} con DNI {cliente.dni}")
    print("Cliente atendido:", cliente)


def buscar_cliente(clientes):
    """Solicita un nombre y busca al cliente en la lista enlazada."""
    nombre = input("Ingrese el nombre que desea buscar: ").strip()

    if not nombre:
        print("Debe ingresar un nombre.")
        return

    cliente = clientes.buscar_por_nombre(nombre)

    if cliente is None:
        print("Cliente no encontrado.")
    else:
        print("Cliente encontrado:", cliente)


def mostrar_clientes(clientes):
    """Muestra todos los clientes registrados."""
    clientes_registrados = clientes.mostrar_clientes()

    if not clientes_registrados:
        print("No existen clientes registrados.")
        return

    print("\nCLIENTES REGISTRADOS")
    for numero, cliente in enumerate(clientes_registrados, start=1):
        print(f"{numero}. {cliente}")


def mostrar_turnos(turnos):
    """Muestra los clientes que esperan atención."""
    turnos_pendientes = turnos.mostrar_turnos()

    if not turnos_pendientes:
        print("No existen turnos pendientes.")
        return

    print("\nTURNOS PENDIENTES")
    for numero, cliente in enumerate(turnos_pendientes, start=1):
        print(f"{numero}. {cliente}")


def mostrar_historial(historial):
    """Muestra las acciones desde la más reciente hasta la más antigua."""
    acciones = historial.mostrar_historial()

    if not acciones:
        print("El historial de acciones esta vacio.")
        return

    print("\nHISTORIAL DE ACCIONES")
    for numero, accion in enumerate(acciones, start=1):
        print(f"{numero}. {accion}")


def deshacer_ultima_accion(historial):
    """Retira la última acción registrada mediante pop."""
    accion = historial.pop()

    if accion is None:
        print("No existen acciones para deshacer.")
    else:
        print("Accion retirada del historial:", accion)


def main():
    """Inicia el gestor de turnos y controla el menú principal."""
    clientes = ClientesLista()
    turnos = ColaTurnos()
    historial = HistorialAccionesPila()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            registrar_turno(clientes, turnos, historial)
        elif opcion == "2":
            atender_turno(turnos, historial)
        elif opcion == "3":
            buscar_cliente(clientes)
        elif opcion == "4":
            mostrar_clientes(clientes)
        elif opcion == "5":
            mostrar_turnos(turnos)
        elif opcion == "6":
            mostrar_historial(historial)
        elif opcion == "7":
            deshacer_ultima_accion(historial)
        elif opcion == "0":
            print("Programa finalizado.")
            break
        else:
            print("Opcion no valida. Intente nuevamente.")


if __name__ == "__main__":
    main()
