# -*- encoding: utf-8 -*-

import pilas

class CategoriaSimulacion(pilas.actores.Actor):
	
	subcategorias = None
	simulaciones = None
	
	def __init__(self, imagen):
		pilas.actores.Actor.__init__(self, imagen)


	def set_subcategorias(self, subcategorias):
		return
