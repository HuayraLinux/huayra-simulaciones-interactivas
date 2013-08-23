# -*- encoding: utf-8 -*-

import pilas
import main
from Simulacion import Simulacion
import pygame.mixer


class NavegacionSimulaciones(pilas.actores.Actor):
	
	ancho = 0
	mitad = 0
	paso = 0
	actual = 0
	total = 0
	sonido_mover = None
	
	
	def __init__(self, x=0, y=0):
		self.actores = pilas.grupo.Grupo()		
		pilas.actores.Actor.__init__(self, 'invisible.png')
		self.x = x
		self.y = y
		

	def iniciar_valores(self):
		self.paso = Simulacion.ancho + Simulacion.separacion
		self.total = len(self.actores)
		self.ancho = self.paso * NavegacionSimulaciones.total
		self.mitad = self.ancho / 2
		

	def distribuir_simulaciones(self):
		i = 0
		for sim in self.actores:
			sim.x = i * (self.paso)
			i = i+1


	def setear_tamanios(self):

		anteriores = self.actores[:self.actual]
		for act in anteriores:
			act.escala = .7
			act.transparencia = 50
			
		siguientes = self.actores[self.actual+1:]
		for act in siguientes:
			act.escala = .7
			act.transparencia = 50			
		
		self.actores[self.actual].escala = 1
		self.actores[self.actual].transparencia = 0
		
	
	def desaparecer_restantes(self):
		anteriores = self.actores[:self.actual]
		for act in anteriores:
			act.transparencia = [100]
			
		siguientes = self.actores[self.actual+1:]
		for act in siguientes:
			act.transparencia = [100]
		
		self.actores[self.actual].escala = 1
		self.actores[self.actual].transparencia = 0
		
