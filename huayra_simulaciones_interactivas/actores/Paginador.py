# -*- encoding: utf-8 -*-

import pilas
import main


class Paginador(pilas.actores.Actor):
	
	def __init__(self, x=0, y=0, paginas=0):
		self.botones = pilas.grupo.Grupo()		
		pilas.actores.Actor.__init__(self, 'invisible.png')
		
		self.x = x
		self.y = y
		self.paginas = paginas
		self.definir_centro(("centro", "arriba"))
		

	def renderizar(self):
		if self.paginas == 0:
			return
		
		pagina = 1
		while pagina <= self.paginas:
			print "[" + str(pagina) + "]"
			pagina += 1
		
