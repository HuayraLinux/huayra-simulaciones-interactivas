# -*- encoding: utf-8 -*-
import pilas
import pilas.evento
import main
from pilas.escena import Base
from ..Simulacion import Simulacion
from ..NavegacionSimulaciones import NavegacionSimulaciones

class EscenaSimulaciones(pilas.escena.Base):
	
	nav = None  # Navegación de categorías
	camara_x = 0
	
	def __init__(self):
		Base.__init__(self)
			
	
	def iniciar(self):
		pilas.fondos.Color(pilas.colores.gris)
		
		# Categorías
		self.nav = NavegacionSimulaciones()
		i = 0
		for sim in main.sim.simulaciones:				
			self.nav.actores.append(
				Simulacion(
					titulo=sim['nombre'], 
					screenshot=sim['screenshot'], 
					descripcion=sim['descripcion'],
				)
			)
			i = i+1
		
		self.nav.iniciar_valores()
		self.nav.distribuir_simulaciones()
		self.nav.definir_centro(("izquierda", "arriba"))
		self.nav.setear_tamanios()
		
		pilas.escena_actual().mueve_rueda.conectar(self.mover, id='mover_simulaciones')
	
	
	def reconectar_mueve_rueda(self):
		pilas.escena_actual().mueve_rueda.conectar(self.mover, id='mover_simulaciones')
		
	
	def mover(self, evento):
		self.nav.sonido_mover.reproducir()
		# Desconectar la señal hasta que termine la animación de la cámara
		pilas.escena_actual().mueve_rueda.desconectar_por_id('mover_simulaciones')
		
		paso = 0
		
		# Límites para que pase de a 1
		if evento.delta >= 1:
			paso = 1
		elif evento.delta <= -1:
			paso = -1
		else:
			paso = evento.delta

		# Fijar límites
		actual = self.nav.actual + paso
		if actual <= 0:
			actual = 0
		elif actual >= self.nav.total-1:
			actual = self.nav.total-1
		
		self.nav.actual = actual
			
		#print "Actual:", actual, 'Paso', paso
		
		self.nav.setear_tamanios()		
		self.camara_x = self.nav.paso * actual
		pilas.escena_actual().camara.x = pilas.interpolar(self.camara_x, tipo='desaceleracion_gradual', duracion=.2)
		pilas.mundo.agregar_tarea(.2, self.reconectar_mueve_rueda)
		
		
