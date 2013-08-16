# -*- encoding: utf-8 -*-
import pilas
import pilas.evento
import main
from pilas.escena import Base
from ..Simulacion import Simulacion
from ..NavegacionSimulaciones import NavegacionSimulaciones

class EscenaSimulaciones(pilas.escena.Base):
	
	nav = None  # Navegación de categorías
	camara_x = 0.0
	
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

		flecha_prev = pilas.imagenes.cargar_grilla("imagenes/DDR___Arrow_by_Blade_Genexis.png", 2)
		self.prev = pilas.actores.Actor(flecha_prev)
		self.prev.fijo = True
		self.prev.x = -100
		self.prev.y = -200
		
		flecha_next = pilas.imagenes.cargar_grilla("imagenes/DDR___Arrow_by_Blade_Genexis.png", 2)
		self.next = pilas.actores.Actor(flecha_next)
		self.next.fijo = True
		self.next.x = 100
		self.next.y = -200
		self.next.espejado = True
		 
		pilas.escena_actual().mueve_rueda.conectar(self.mover_desde_rueda, id='mover_simulaciones_desde_rueda')
		pilas.escena_actual().click_de_mouse.conectar(self.mover_desde_botones, id='mover_simulaciones_desde_botones')
	
	
	def reconectar_mueve_rueda(self):
		pilas.escena_actual().mueve_rueda.conectar(self.mover_desde_rueda, id='mover_simulaciones_desde_rueda')
	
	
	def reconectar_click(self):
		pilas.escena_actual().click_de_mouse.conectar(self.mover_desde_botones, id='mover_simulaciones_desde_botones')
	
	
	def mover_desde_rueda(self, evento):
		# Desconectar la señal hasta que termine la animación de la cámara
		pilas.escena_actual().mueve_rueda.desconectar_por_id('mover_simulaciones_desde_rueda')
		
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
			
		self.camara_x = self.nav.paso * actual + 0.0
		print "camara_x:", self.camara_x, ", camara.x:", pilas.escena_actual().camara.x 

		if self.camara_x != pilas.escena_actual().camara.x:
			
			main.sim.sounds['navegacion_simulaciones_mover'].play()
			
			self.nav.setear_tamanios()
			pilas.escena_actual().camara.x = pilas.interpolar(self.camara_x, tipo='desaceleracion_gradual', duracion=.2)
			pilas.mundo.agregar_tarea(.2, self.reconectar_mueve_rueda)
		else:
			self.reconectar_mueve_rueda()
		
			
	def mover_desde_botones(self, evento):
		paso = 0
		print "X del botón izq:", self.prev.x
		print "Camara x:", pilas.escena_actual().camara.x
		print "Evento x:", evento.x
		x, y = evento.x - pilas.escena_actual().camara.x, evento.y  # X corregido
		
		# Esta colisionando con la pelota?                                                                           
		if self.prev.colisiona_con_un_punto(x, y):
			paso = -1
		elif self.next.colisiona_con_un_punto(x, y):
			paso = 1
			
		if paso != 0:
			# Desconectar la señal hasta que termine la animación de la cámara
			pilas.escena_actual().click_de_mouse.desconectar_por_id('mover_simulaciones_desde_botones')
		
		# Fijar límites
		actual = self.nav.actual + paso
		if actual <= 0:
			actual = 0
		elif actual >= self.nav.total-1:
			actual = self.nav.total-1
		
		self.nav.actual = actual
			
		self.camara_x = self.nav.paso * actual + 0.0
		print "camara_x:", self.camara_x, ", camara.x:", pilas.escena_actual().camara.x 

		if self.camara_x != pilas.escena_actual().camara.x:
			
			main.sim.sounds['navegacion_simulaciones_mover'].play()
			
			self.nav.setear_tamanios()
			pilas.escena_actual().camara.x = pilas.interpolar(self.camara_x, tipo='desaceleracion_gradual', duracion=.2)
			pilas.mundo.agregar_tarea(.2, self.reconectar_click)
		else:
			self.reconectar_click()
