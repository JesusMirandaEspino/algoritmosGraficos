    
class Operaciones:
    def __init__(self):
        self.opcion = 0
        self.run = True
        self.n1 = 0
        self.n2 = 0
        self.error1 = ""
        self.error2 = ""


    def print_word(self):
            word = input("Introduce una palabra: ")
            print("La palabra es ", word)
            print("Sus letras son ")
            for letter in word:
                print(letter)


    def menu(self):
        menu = """
        Menú:
        1. Sumar 
        2. Resta
        3. Multiplicar
        4. Salir
        """
        print(menu)

    def sendError(self):
        return  self.error1, self.error2

    def getNumbers(self):
            try:
                self.n1 = float(input("Intro número uno: "))
            except ValueError:
                self.printError()
                self.error1 = self.n1

            try:
                self.n2 = float(input("Intro número Dos: "))
            except ValueError:
                self.printError()
                self.error2 = self.n2
    

    def operacion(self, tipo):
        match tipo:
            case 1:
                try:
                    return self.n1 + self.n2
                except TypeError:
                    self.operationError()
                    return self.sendError()
            case 2:
                try:
                    return self.n1 - self.n2
                except TypeError:
                    self.operationError()
                    return self.sendError()
            case 3:
                try:
                    return self.n1 * self.n2
                except TypeError:
                    self.operationError()
                    return self.sendError()
            case _:
                return "Internal Error, contact support"
        

    def comenzar(self):
        self.print_word()
        while self.run:
            self.menu()
            try:
                self.opcion = int(input("Ingrese la opción deseada: "))
            except ValueError:
                self.opcion = 0

            match self.opcion:
                case 1:
                    self.getNumbers()
                    print("La suma es: ", self.operacion(1))
                case 2:
                    self.getNumbers()
                    print("La resta es: ", self.operacion(2))
                case 3:
                    self.getNumbers()
                    print("La resta es: ", self.operacion(3))
                case 4:
                    self.run = False
                    print("Que tenga un buen dia")
                case _:
                    print("Opción inválida. Intente nuevamente.")

    def printError(self):
        print("ingreso erroneo")

    def operationError(self):
        print("Error en Operacion")

ejecutar = Operaciones()
ejecutar.comenzar()