# -*- encoding: utf-8 -*-
import pilas
import pilas.evento
import main
from pilas.escena import Base
from ..CategoriaSimulacion import CategoriaSimulacion
from ..NavegacionCategorias import NavegacionCategorias

class EscenaCategorias(pilas.escena.Base):
	
	nav = None  # Navegación de categorías
	v = 0.15  # Escala de velocidad
	vx = 0
	
	def __init__(self):
		Base.__init__(self)
	
	
	def iniciar(self):
		pilas.fondos.Color(pilas.colores.gris)
		
		# Categorías
		self.nav = NavegacionCategorias()
		i = 0
		for categoria in main.sim.data['categorias']:
			# poner las categorías a partir de 0
			x_pos = (CategoriaSimulacion.ancho / 2) + i * (CategoriaSimulacion.ancho + CategoriaSimulacion.separacion)
			i += 1
			categoria['actor'] = CategoriaSimulacion(
				titulo=categoria['nombre'], 
				screenshot=categoria['screenshot'], 
				descripcion=categoria['descripcion'],
				x=x_pos
			)
			categoria['actor'].actores.transparencia = 100
			categoria['actor'].actores.transparencia = [100, 0]
			self.nav.actores.append(categoria['actor'])
		self.nav.actores.transparencia = [100, 0]
		self.nav.calcular_medidas()
		self.nav.centrar_categorias()
		self.nav.centro = ("centro", "arriba")
		self.nav.y = 0
		self.nav.x = 0
		print "Ancho navegación: ", self.nav.ancho
		print "Total categorías:", CategoriaSimulacion.total
		
		
		pilas.escena_actual().mueve_mouse.conectar(self.mover)
	
	
	def mover(self, evento):
		self.vx =  -(self.v * evento.x)
		if self.vx > 5: self.vx = 5
		if self.vx < -5: self.vx = -5
		#self.nav.x = pilas.interpolar(-(evento.x*2), 1)
		self.nav.x += self.vx
		#print "Dist x:", dx
		#print "V:", vx
		#print "Nav X:", self.nav.x
		#print "mouse X:", evento.x
		
