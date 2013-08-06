# -*- encoding: utf-8 -*-

import pilas

class CategoriaSimulacion(pilas.actores.Actor):
	
	ancho = 300
	separacion = 10
	total = 0
	
	def __init__(self, x=0, y=0, titulo="", screenshot="", descripcion=""):
		self.actores = pilas.grupo.Grupo([
			pilas.actores.Texto(titulo, magnitud=15, fijo=False),
			pilas.actores.Actor(screenshot),
			pilas.actores.Texto(descripcion, magnitud=10, fijo=False)
		])
		# Título
		self.actores[0].y = 200
		# Screenshot
		self.actores[1].y = 60		
		# Descripción
		self.actores[2].y = -70
		
		
		pilas.actores.Actor.__init__(self, 'invisible.png')
		self.x = x
		self.y = y
		
		CategoriaSimulacion.total = CategoriaSimulacion.total + 1
		

	
	def definir_posicion(self, x, y):
		delta_x = x - self.x
		delta_y = y - self.y
		for actor in self.actores:
			actor.x += delta_x
			actor.y += delta_y

		pilas.actores.Actor.definir_posicion(self, x, y)
		
			
