# -*- encoding: utf-8 -*-

import pilas
import main
from CategoriaSimulacion import CategoriaSimulacion

class NavegacionCategorias(pilas.actores.Actor):
	
	ancho = 0
	mitad = 0
	
	def __init__(self, x=0, y=0):
		self.actores = pilas.grupo.Grupo()		
		pilas.actores.Actor.__init__(self, 'invisible.png')
		self.x = x
		self.y = y
	

	def calcular_medidas(self):
		self.ancho = len(self.actores) + ((CategoriaSimulacion.ancho + CategoriaSimulacion.separacion) * CategoriaSimulacion.total)

		
	
	def definir_posicion(self, x, y):
		delta_x = x - self.x
		delta_y = y - self.y
		for actor in self.actores:
			actor.x += delta_x
			actor.y += delta_y

		pilas.actores.Actor.definir_posicion(self, x, y)
		
			
