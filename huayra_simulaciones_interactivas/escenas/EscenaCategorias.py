# -*- encoding: utf-8 -*-
import pilas
import pilas.evento
import main
from pilas.escena import Base
from ..CategoriaSimulacion import CategoriaSimulacion
from ..NavegacionCategorias import NavegacionCategorias

class EscenaCategorias(pilas.escena.Base):
	
	nav = None  # Navegación de categorías
	
	def __init__(self):
		Base.__init__(self)
			
	
	def iniciar(self):
		pilas.fondos.Color(pilas.colores.gris)
		
		# Categorías
		self.nav = NavegacionCategorias()
		
		for categoria in main.sim.data['categorias']:				
			self.nav.actores.append(
				CategoriaSimulacion(
					titulo=categoria['nombre'], 
					screenshot=categoria['screenshot'], 
					descripcion=categoria['descripcion'],
				)
			)
		
		self.nav.iniciar_valores()
		self.nav.distribuir_categorias()
		self.nav.definir_centro(("izquierda", "arriba"))
		
		pilas.escena_actual().mueve_rueda.conectar(self.mover)
	
	
	def mover(self, evento):
		paso = 0
		# Límites para que pase de a 1
		if evento.delta > 1:
			paso = 1
		elif evento.delta < -1:
			paso = -1
		else:
			paso = evento.delta
		
		
		self.nav.actual = self.nav.actual + paso
		
		print "Actual:", self.nav.actual
		
		if self.nav.actual < 0:
			self.nav.actual = 0
		elif self.nav.actual > self.nav.total:
			self.nav.actual = self.nav.total
		#print "Actual:", self.nav.actual
		
		#self.nav.setear_tamanios()
		
		camara_x = pilas.escena_actual().camara.x + (paso * self.nav.paso)
		#print "Camara x:", camara_x
		pilas.escena_actual().camara.x = pilas.interpolar(camara_x, duracion=.1)
			
		
		
		
