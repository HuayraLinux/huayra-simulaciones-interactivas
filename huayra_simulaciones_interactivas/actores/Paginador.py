# -*- encoding: utf-8 -*-

import pilas
import main


class Paginador(pilas.actores.Actor):
	
	def __init__(self, x=0, y=0, paginas=0):
		self.botones = pilas.grupo.Grupo()		
		pilas.actores.Actor.__init__(self, 'invisible.png')
		self.paginas = paginas
		self.definir_centro(("centro", "arriba"))
		

	def renderizar(self):
		if self.paginas == 0:
			return
		
		pagina = 1
		pos_x = 0 # primer botón
		pos_y = 0 # primer fila
		maximo_x = 0 # para calcular el centro
		filas = [15, 28, 41]
		
		while pagina <= self.paginas:
			bot = pilas.interfaz.Boton(str(pagina), x=pos_x, y=pos_y)
			if pos_x > maximo_x:
				maximo_x = pos_x
			if pagina in filas:
				pos_y = pos_y - 30
				pos_x = -37
				
			self.botones.append(bot)
			
			separador = 5
			if pagina == 9: # workaround?
				separador = 10			
			
			pos_x = pos_x + bot.ancho + separador
			pagina += 1
		
		for bot in self.botones:
			bot.x -= (maximo_x/2)
		
		
