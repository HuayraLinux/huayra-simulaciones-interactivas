# -*- encoding: utf-8 -*-

import pilas

class CategoriaSimulacion(pilas.actores.Actor):
	
	def __init__(self, imagen):
		pilas.actores.Actor.__init__(self, imagen)
		self.subcategorias = None
		self.simulaciones = None
