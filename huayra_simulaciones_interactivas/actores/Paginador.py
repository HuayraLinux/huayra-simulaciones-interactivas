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
		pos_x = 0
		while pagina <= self.paginas:
			# print "[" + str(pagina) + "]"
			bot = pilas.interfaz.Boton(str(pagina), x=pos_x)
			
			self.botones.append(
				bot
			)
			pagina += 1
			pos_x = pos_x + bot.ancho + 5
		
