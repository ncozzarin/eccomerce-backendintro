class Monitor:
    contador_monitor = 0
    
    def __init__(self,marca,tamanio):
        Monitor.contador_monitor += 1
        self.__id_monitor = Monitor.contador_monitor
        self._marca = marca
        self._tamanio = tamanio

    def __str__(self):
        return "El monitor es: " + self._marca + str(self._tamanio)



