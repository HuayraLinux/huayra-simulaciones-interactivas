# -*- encoding: utf-8 -*-

import pilas
from math import ceil

class Paginacion(pilas.actores.Actor):
	
	def __init__(self, pagina_actual=1, cantidad_elementos=0, elementos_por_pagina=3):
		
		self.pagina_actual = pagina_actual
		self.cantidad_elementos = cantidad_elementos
		self.elementos_por_pagina = elementos_por_pagina
		self.paginas = int(ceil(self.cantidad_elementos / float(self.elementos_por_pagina)))
		
		self.numeros = pilas.grupo.Grupo()
		
		pilas.actores.Actor.__init__(self, 'invisible.png')
			
