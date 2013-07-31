# -*- encoding: utf-8 -*-
import pilas
import main
from pilas.escena import Base

class EscenaCategorias(pilas.escena.Base):
	
	def __init__(self):
		Base.__init__(self)
	
	def iniciar(self):
		pilas.fondos.Color(pilas.colores.gris)
		self.texto = pilas.actores.Texto(u"mostrando categorías")
