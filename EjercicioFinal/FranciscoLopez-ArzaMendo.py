# Clase que permite almacenar y gestionar una lista de tareas
class ListaTareas:

    # Constructor de la clase
    def __init__(self):
        self.tareas = []

    # Metodos
    def agregar_tarea(self, tarea):
        self.tareas.append({"descripcion": tarea, "completada": False})

    # Marca una tarea como completada
    def marcar_completada(self, indice):
        try:
            self.tareas[indice]["completada"] = True
            print("Tarea marcada como completada.")
        except IndexError:
            print("La posición ingresada no es válida.")

    # Muestra todas las tareas
    def mostrar_tareas(self):
        print("Tareas pendientes:")
        for i, tarea in enumerate(self.tareas):
            estado = "Completada" if tarea["completada"] else "Pendiente"
            print(f"{i + 1}. {tarea['descripcion']} - {estado}")

    # Elimina una tarea
    def eliminar_tarea(self, indice):
        try:
            tarea_eliminada = self.tareas.pop(indice)
            print(f"Tarea '{tarea_eliminada['descripcion']}' eliminada.")
        except IndexError:
            print("La posición ingresada no es válida.")


# Función principal del programa
def main():
    lista = ListaTareas()

    while True:
        print("\nMenú:")
        print("1. Agregar nueva tarea")
        print("2. Marcar tarea como completada")
        print("3. Mostrar todas las tareas")
        print("4. Eliminar tarea")
        print("5. Salir")

        opcion = input("Ingrese el número de la opción que desea realizar: ")

        if opcion == "1":
            tarea = input("Ingrese la nueva tarea: ")
            lista.agregar_tarea(tarea)
        elif opcion == "2":
            indice = int(input("Ingrese el número de la tarea que desea marcar como completada: ")) - 1
            lista.marcar_completada(indice)
        elif opcion == "3":
            lista.mostrar_tareas()
        elif opcion == "4":
            indice = int(input("Ingrese el número de la tarea que desea eliminar: ")) - 1
            lista.eliminar_tarea(indice)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")


# Llamado de la función principal
if __name__ == "__main__":
    main()
