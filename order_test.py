from orden import Orden
from computadoras import Computadora
from monitor import Monitor
from raton import Raton
from teclado import Teclado

tecladoHP = Teclado("HP","USB")
ratonHP = Raton("HP","USB")
monitorHP = Monitor("HP","23 pulgadas")

computadoraHP = Computadora("HP comput", monitorHP,tecladoHP,ratonHP)

tecladoRAZER = Teclado("Razer","HDMI")
ratonRAZER = Raton("Razer","HDMI")
monitorRAZER = Monitor("Razer","40 pulgadas")

computadoraRAZER = Computadora("Razern",tecladoRAZER,ratonRAZER,monitorRAZER)

computadora_armada = Computadora("Armada 1", tecladoRAZER,ratonHP,monitorHP)
computadora_armada2 = Computadora("Armada 2", tecladoHP,ratonRAZER,monitorRAZER)

computadoras1 = [computadora_armada, computadoraRAZER]
orden1 = Orden(computadoras1)
print(orden1)