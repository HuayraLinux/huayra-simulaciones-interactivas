# -*- encoding: utf-8 -*-

import pilas, main
import os.path

class Simulacion(pilas.actores.Actor):
	
	ancho = 300
	separacion = -30
	
	
	def __init__(self, x=0, y=0, titulo="", screenshot="", descripcion="", archivo=""):
		# Área de contacto
		superficie = pilas.imagenes.cargar_superficie(300, 300)
		superficie.rectangulo(0, 0, 300, 300, color=pilas.colores.rojo, relleno=True)
		
		_screenshot = main.data_dir + "data/screenshots/" + screenshot 
		if not os.path.isfile(_screenshot):
			_screenshot = main.data_dir + 'imagenes/gui/sin_imagen.png'
		
		self.actores = pilas.grupo.Grupo([
			pilas.actores.Texto(titulo, magnitud=15, fijo=False),
			pilas.actores.Actor(_screenshot),
			pilas.actores.Texto(descripcion, magnitud=10, fijo=False),
			pilas.actores.Actor(superficie)
		])
		
		self.titulo = titulo
		self.descripcion = descripcion
		self.screenshot = screenshot
		self.area_contacto = self.actores[3]
		self.archivo = archivo

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

	
	def definir_escala(self, escala):
		for actor in self.actores:
			actor.escala = escala
		pilas.actores.Actor.definir_escala(self, escala)

	
	def definir_transparencia(self, transparencia):
		for actor in self.actores:
			actor.transparencia = transparencia
		self.area_contacto.transparencia = 100
		pilas.actores.Actor.definir_transparencia(self, transparencia)
		
			
