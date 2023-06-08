class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izq = None
        self.der = None

class Arbol:
    def __init__(self):
        self.raiz = None
        self.opcion = 0
        self.run = True
        self.nodos_lista = [20,9,3,4]
        
        
    def crear(self):
        # Crear el árbol binario
        for nodo in self.nodos_lista:
            self.agregar(nodo)


    def agregar(self, dato):
        if self.raiz is None:
            self.raiz = Nodo(dato)
        else:
            self.agregarR(dato, self.raiz)

    def recorrer(self):
        self.recorrerR(self.raiz)

    def buscar(self, dato):
        return self.busquedaR(dato, self.raiz)

        
    def menu(self):
        menu = """
        Menú:
        1. Agregar un dato
        2. Recorrer el árbol
        3. Buscar un nodo
        4. Salir
        """
        print(menu)
        
    def iniciar(self):
        self.crear()
        while self.run:
            self.menu()
            
            try:
                self.opcion = int(input("Ingrese la opción deseada: "))
            except ValueError:
                self.opcion = 0
                
            match self.opcion:
                case 1:
                    dato = int(input("Ingrese el dato a agregar: "))
                    self.agregar(dato)
                    print("Dato agregado exitosamente.")
                case 2:
                    print("\nRecorrido del árbol:")
                    self.recorrer()
                case 3:
                    self.buscar_Nodo()
                case 4:
                    print("Ten un buen dia") 
                    self.run = False
                case _:
                    print("Opción inválida. Por favor, ingrese una opción válida.")


    def buscar_Nodo(self):
        dato = int(input("Ingrese el dato a buscar: "))
        nodo_encontrado = self.buscar(dato)
        if nodo_encontrado is not None:
            print("El nodo fue encontrado en el árbol.")
        else:
            print("El nodo no fue encontrado en el árbol.")

    def agregarR(self, dato, nodo_actual):
        if dato < nodo_actual.dato:
            if nodo_actual.izq is None:
                nodo_actual.izq = Nodo(dato)
            else:
                self.agregarR(dato, nodo_actual.izq)
        else:
            if nodo_actual.der is None:
                nodo_actual.der = Nodo(dato)
            else:
                self.agregarR(dato, nodo_actual.der)
                
    def recorrerR(self, nodo_actual):
        if nodo_actual is not None:
            self.recorrerR(nodo_actual.izq)
            print(nodo_actual.dato)
            self.recorrerR(nodo_actual.der)
            
    
    def busquedaR(self, dato, nodo_actual):
        if nodo_actual is None or nodo_actual.dato == dato:
            return nodo_actual
        if dato < nodo_actual.dato:
            return self.busquedaR(dato, nodo_actual.izq)
        else:
            return self.busquedaR(dato, nodo_actual.der)
        

ejecutar = Arbol()
ejecutar.iniciar()