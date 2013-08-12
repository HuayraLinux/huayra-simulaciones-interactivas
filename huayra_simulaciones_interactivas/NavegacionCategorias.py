# -*- encoding: utf-8 -*-

import pilas
import main
from CategoriaSimulacion import CategoriaSimulacion

class NavegacionCategorias(pilas.actores.Actor):
	
	ancho = 0
	mitad = 0
	paso = 0
	actual = 0
	total = 0
	
	
	def __init__(self, x=0, y=0):
		self.actores = pilas.grupo.Grupo()		
		pilas.actores.Actor.__init__(self, 'invisible.png')
		self.x = x
		self.y = y
		

	def iniciar_valores(self):
		self.paso = CategoriaSimulacion.ancho + CategoriaSimulacion.separacion
		self.total = len(self.actores)
		self.ancho = self.paso * NavegacionCategorias.total
		self.mitad = self.ancho / 2
		

	def distribuir_categorias(self):
		i = 0
		for cat in self.actores:
			cat.x = i * (self.paso)
			i = i+1	
		self.setear_tamanios()


	def setear_tamanios(self):
		anteriores = self.actores[:self.actual]			
		for act in anteriores:
			act.escala = .7
			
		siguientes = self.actores[self.actual+1:]
		for act in siguientes:
			act.escala = .7
		
		self.actores[self.actual].escala = 1
		
			
	
	
		
			
