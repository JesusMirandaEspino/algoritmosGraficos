class Paises:

    def __init__(self):
        self.lista = ["Alemania", "Canada", "Camerun", "Colombia", "Finlandia", "India", "Japon", "Mexico", "Rusia" ,  "Suecia"]
        self.paises = sorted(self.lista)
        self.run = True
        self.option = 0
    
    def mostrar_menu(self):
        menu = """
        Menú:
        1. Búsqueda binaria de un país
        2. Búsqueda secuencial de un país
        3. Agregar un país
        4. Eliminar un país
        5. Salir
        """
        print(menu)
        
    def comenzar(self):
        while self.run:
            self.mostrar_menu()
            
            try:
                self.option = int(input("Ingrese la opción deseada: "))
            except ValueError:
                self.opcion = 0
            
            
            match self.option:
                case 1:
                    self.enBinario()
                case 2:
                    self.buscar()
                case 3:
                    self.agregar()
                case 4:
                    self.eliminar()
                case 5:
                    self.run = False
                    print("Ten un buen dia")
                case _:
                    print("Opción inválida. Por favor, ingrese una opción válida.")


    def binario(self, pais):
        izq = 0
        der = len(self.paises) - 1
        while izq <= der:
            middle = (izq + der) // 2
            if self.paises[middle].lower() == pais.lower():
                return middle
            elif self.paises[middle].lower() < pais.lower():
                izq = middle + 1
            else:
                der = middle - 1
        return -1


    def secuencial(self, pais):
        for i, p in enumerate(self.paises):
            if p.lower() == pais.lower():
                return i
        return -1
    
    
    def agregar(self):
        agregar = input("Ingrese el país a agregar: ")
        if agregar in self.paises:
            print(f"El país {agregar} ya  existe en la lista.")
        else:
            self.paises.append(agregar)
            lista_paises = self.paises
            self.paises = sorted(lista_paises)
            print(f"El país {agregar} ha sido agregado a la lista.")
            
            
            
    def eliminar(self):
        eliminar = input("Ingrese el país a eliminar: ")
        if eliminar in self.paises:
            self.paises.remove(eliminar)
            print(f"El país {eliminar} ha sido eliminado de la lista.")
        else:
            print("El país no se encuentra en la lista.")
            
            
            
    def buscar(self):
        pais = input("Ingrese el país a buscar: ")
        index = self.secuencial(pais)
        if index != -1:
            print(f"El país {pais} se encuentra en la posición {index + 1} de la lista.")
        else:
            print("El país no se encuentra en la lista.")
            
            
    def enBinario(self):
        pais = input("Ingrese el país a buscar: ")
        indice = self.binario( pais)
        if indice != -1:
            print(f"El país {pais} se encuentra en la posición {indice + 1} de la lista.")
        else:
            print("El país no se encuentra en la lista.")
            
            

ejecutar = Paises()
ejecutar.comenzar()