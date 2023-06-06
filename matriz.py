class Matriz:
    def __init__(self):
        #Inicializar variables
        self.matriz = []
        self.option  = 0

    # Lee lo seleccionado del menu 
    def accion(self):
        continuar = True
        while continuar:
            self.menu()
            self.option = int(input("Seleccione una opción: "))

            match self.option:
                case 1:
                    fila = int(input("Ingrese el número de fila a sumar (1-3): "))
                    self.sumar_fila(fila)
                case 2:
                    columna = int(input("Ingrese el número de columna a sumar (1-3): "))
                    self.sumar_columna(columna)
                case 3:
                    self.sumar_matriz()
                case 4:
                    print("¡Que tengas un buen dia!")
                    continuar  = False
                case _:
                    print("Opción inválida. Intente nuevamente.")

            
    # Iniciar la ejecucion del programa
    def comenzar(self):
        self.iniciar_matriz(3,3)
        self.accion()
        
        
        
    # Sumar toda la matriz
    def sumar_matriz(self):
        suma = sum(sum(fila) for fila in self.matriz)
        print(f"La suma de toda la matriz es: {suma}")
        
    # Menu principal
    def menu(self):
        print('*****************************')
        menu = """
        Menú:
        1. Sumar una fila de la matriz
        2. Sumar una columna de la matriz
        3. Sumar toda la matriz
        4. Salir
        """
        print(menu)

    # Sumar una fila seleccionada
    def sumar_fila(self, fila):
        suma = sum( self.matriz[fila - 1])
        print(f"La suma de la fila {fila} es: {suma}")
        
    
    # Sumar una columna seleccionada
    def sumar_columna(self, columna):
        suma = sum(fila[columna - 1] for fila in self.matriz)
        print(f"La suma de la columna {columna} es: {suma}")

                
    # Crear la matriz ingresando los valores
    def iniciar_matriz(self, filas, columnas):
        for line in range(filas):
            fila = []
            for col in range(columnas):
                valor = int(input(f"Ingrese un número para la matriz, fila {line + 1} y columna {col + 1} :  "))
                fila.append(valor)
            self.matriz.append(fila)
 
    
ejecutar = Matriz()
ejecutar.comenzar()
