# -*- encoding: utf-8 -*-

import pilas

class CategoriaSimulacion(pilas.actores.Actor):
	
	
	def __init__(self, x=0, y=0, titulo="", screenshot="", descripcion=""):
		self.actores = pilas.grupo.Grupo([
			pilas.actores.Texto(titulo),
			pilas.actores.Actor(screenshot),
			pilas.actores.Texto(descripcion)
		])
		self.actores[0].y = 200
		self.actores[1].y = 50
		self.actores[2].y = -200
		pilas.actores.Actor.__init__(self, 'invisible.png')
		self.x = x
		self.y = y

	
	def definir_posicion(self, x, y):
		delta_x = x - self.x
		delta_y = y - self.y
		for actor in self.actores:
			actor.x += delta_x
			actor.y += delta_y

		pilas.actores.Actor.definir_posicion(self, x, y)
		
			
