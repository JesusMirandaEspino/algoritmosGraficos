class Turnos:
    def __init__(self):
        # Se genera una estructura de datos
        self.disponibles = [*range(1, 21, 1) ]
        self.asignados = []
        self.opcion = 0

    # funcion para asignar un turno
    def asginar(self):
        if len(self.disponibles) > 0:
            turno = self.disponibles.pop(0)
            self.asignados.append(turno)
            print("Persona agregada a turno")
        else:
            print("Sin turnos disponibles.")

    # funcion para terminar un turno
    def terminar(self):
        if len(self.asignados) > 0:
            turno = self.asignados.pop(0)
            self.disponibles.append(turno)
            print("Salio persona de un turno")
        else:
            print("No hay turnos activos")

    # funcion para mostrar los turnos pendientes
    def pendientes(self):
        print("Turnos pendientes:", len(self.disponibles))

    # Menu principal
    def menu(self):
        menu = """
        Menú:
        1. Asignar un turno
        2. Terminar un turno
        3. Mostrar cantidad de turnos pendientes
        4. Salir
        """
        print(menu)

    #Iniciar programa
    def iniciar(self):
        iniciar = True
        while iniciar:
            self.menu()
            print("Ingrese una opción: ")
            try:
                self.opcion = int(input())
            except ValueError:
                self.opcion = 0
            
            print('************************')
            match self.opcion:
                case 1:
                    self.asginar()
                case 2:
                    self.terminar()
                case 3:
                    self.pendientes()
                case 4:
                    print("Saliendo. Que tenga un Buen dia.")
                    iniciar = False
                case _:
                    print("Opción inválida. Intente nuevamente.")
            

banco = Turnos()
banco.iniciar()