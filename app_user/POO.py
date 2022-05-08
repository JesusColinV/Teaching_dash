class Carro:
    def __init__(self) -> None:
        """
        funcion de inicializacion
        """
        self.__puertas = 4 #atributo
        pass

    def __moverse(self): #metodo
        """
        el movimiento del auto
        """
        print("movimiento")


class Mustang(Carro):
    def __init__(self) -> None:
        super().__init__()
        self.__puertas = 25
    
    def moverte_rapido(self):
        print("movimiento rapido")
    

    

mustang = Mustang()

a=0