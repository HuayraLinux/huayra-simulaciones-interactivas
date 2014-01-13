# -*- encoding: utf-8 -*-

from math import ceil

class Paginacion():
	
	def __init__(self, pagina_actual=1, cantidad_elementos=0, elementos_por_pagina=3):
		
		self.pagina_actual = pagina_actual
		self.cantidad_elementos = cantidad_elementos
		self.elementos_por_pagina = elementos_por_pagina
		self.paginas = int(ceil(self.cantidad_elementos / float(self.elementos_por_pagina)))
