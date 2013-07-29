# -*- encoding: utf-8 -*-
import pilas
from pilas.escena import Base

class EscenaBienvenida(pilas.escena.Base):
	
	def __init__(self):
		Base.__init__(self)
	
	def iniciar(self):
		pilas.fondos.Color(pilas.colores.negro)
		texto = pilas.actores.Texto("Simulaciones Interactivas")
