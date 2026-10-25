# Gestor de turnos CarUPS

Proyecto académico de la asignatura **Algoritmos y Estructuras de Datos**. El objetivo es desarrollar un programa de consola en Python para gestionar los turnos de atención del taller ficticio CarUPS.

El proyecto permite aplicar las estructuras de datos lineales estudiadas en la Unidad 1:

- Una lista simplemente enlazada para registrar y buscar clientes.
- Una cola enlazada para atender los turnos en orden de llegada.
- Una pila enlazada para guardar el historial de acciones del operador.

Todas las estructuras se implementan desde sus nodos para demostrar su funcionamiento interno.

## Estructura actual del proyecto

```text
unidad_1/
├── app/
│   ├── __init__.py
│   ├── clientes_lista.py
│   └── historial_acciones_pila.py
├── .gitignore
└── README.md
```

El archivo `main.py` se creará en la raíz del proyecto cuando las tres estructuras estén terminadas.

## Funcionalidades implementadas

### Lista enlazada de clientes

El archivo `app/clientes_lista.py` contiene:

- La clase `Cliente`, que almacena el DNI y el nombre.
- La clase `NodoCliente`, utilizada para enlazar los clientes.
- La clase `ClientesLista`, que administra la lista.
- Registro de clientes.
- Búsqueda de clientes por nombre.
- Recorrido y presentación de todos los clientes.

### Pila del historial de acciones

El archivo `app/historial_acciones_pila.py` contiene:

- La clase `NodoAccion`.
- La clase `HistorialAccionesPila`.
- Registro de acciones mediante `push`.
- Retiro de la última acción mediante `pop`.
- Consulta de la última acción registrada.
- Recorrido del historial desde la acción más reciente.

La pila utiliza el principio **LIFO**: la última acción registrada es la primera que se retira.

## Complejidad de las operaciones actuales

| Estructura     | Operación                  | Complejidad |
| -------------- | -------------------------- | ----------: |
| Lista enlazada | Comprobar si está vacía    |        O(1) |
| Lista enlazada | Agregar al final           |        O(n) |
| Lista enlazada | Buscar por nombre          |        O(n) |
| Lista enlazada | Mostrar clientes           |        O(n) |
| Pila           | Comprobar si está vacía    |        O(1) |
| Pila           | `push`                     |        O(1) |
| Pila           | `pop`                      |        O(1) |
| Pila           | Consultar la última acción |        O(1) |
| Pila           | Mostrar el historial       |        O(n) |

`n` representa la cantidad de elementos almacenados en la estructura.

## Ejecución final

```bash
python main.py
```
