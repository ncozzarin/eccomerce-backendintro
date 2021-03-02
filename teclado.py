from dispositivo_entrada import DispositivoEntrada
class Teclado(DispositivoEntrada):
    contador_teclados = 0
    def __init__(self,marca,tipo_entrada):
        Teclado.contador_teclados += 1
        self.__id_reclado = "R" + str(Teclado.contador_teclados)
        self._marca = marca
        self._tipo_entrada = tipo_entrada

    def __str__(self):
        return "ID: {0}, Marca: {1}, Tipo: {2}".format(self.__id_teclado,self._marca,self._tipo_entrada) 