from dispositivo_entrada import DispositivoEntrada
class Raton(DispositivoEntrada):
    contador_ratones = 0
    def __init__(self,marca,tipo_entrada):
        Raton.contador_ratones += 1
        self.__id_raton = "R" + str(Raton.contador_ratones)
        self._marca = marca
        self._tipo_entrada = tipo_entrada

    def __str__(self):
        return "ID: {0}, Marca: {1}, Tipo: {2}".format(self.__id_raton,self._marca,self._tipo_entrada) 

