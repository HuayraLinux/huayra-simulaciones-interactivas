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
		 
		self.conectar_eventos()
		
		ayuda = pilas.actores.TextoInferior(
			"Se puede navegar con las flechas del teclado, la rueda del mouse o haciendo click sobre las flechas",
			magnitud=12,
			autoeliminar=True
		)
	
	
	def conectar_eventos(self):
		pilas.escena_actual().click_de_mouse.conectar(self.mover, id='mover_simulaciones_desde_botones')
		pilas.escena_actual().click_de_mouse.conectar(self.clickear_simulacion, id='clickear_simulacion')
		pilas.escena_actual().mueve_rueda.conectar(self.mover, id='mover_simulaciones_desde_rueda')
		pilas.escena_actual().suelta_tecla.conectar(self.mover, id='mover_simulaciones_desde_teclado')
		
	
	def desconectar_eventos(self):
		pilas.escena_actual().click_de_mouse.desconectar_por_id('mover_simulaciones_desde_botones')
		pilas.escena_actual().click_de_mouse.desconectar_por_id('clickear_simulacion')
		pilas.escena_actual().mueve_rueda.desconectar_por_id('mover_simulaciones_desde_rueda')
		pilas.escena_actual().suelta_tecla.desconectar_por_id('mover_simulaciones_desde_teclado')
	
	
	def mover(self, evento):
		self.desconectar_eventos()
		paso = 0
		
		#main.debug(evento)
		
		if evento.has_key("delta"):  # Rueda
			# Límites para que pase de a 1
			if evento.delta >= 1:
				paso = 1
			elif evento.delta <= -1:
				paso = -1
			else:
				paso = evento.delta
			
		elif evento.has_key("x"):  # click
			x, y = evento.x - pilas.escena_actual().camara.x, evento.y  # X corregido
			# Esta tocando la flecha?                                                                           
			if self.prev.colisiona_con_un_punto(x, y):
				paso = -1
			elif self.next.colisiona_con_un_punto(x, y):
				paso = 1
				
		elif evento.has_key("codigo"):  # teclado
			if evento.codigo == 1:  # left arrow
				paso = -1
			elif evento.codigo == 2:  # right arrow
				paso = 1
				
		" Sólo desconectar eventos si se toma acción "
		if paso == 0:
			self.conectar_eventos()
			return
		
		# Fijar límites
		actual = self.nav.actual + paso
		if actual <= 0:
			actual = 0
		elif actual >= self.nav.total-1:
			actual = self.nav.total-1
		
		self.nav.actual = actual
			
		self.camara_x = self.nav.paso * actual + 0.0
		
		txt = "camara_x:", self.camara_x, ", camara.x:", pilas.escena_actual().camara.x
		main.debug(paso)

		if self.camara_x != pilas.escena_actual().camara.x:
			main.debug("aca")
			main.sim.sounds['navegacion_simulaciones_mover'].play()
			self.nav.setear_tamanios()
			pilas.escena_actual().camara.x = pilas.interpolar(self.camara_x, tipo='desaceleracion_gradual', duracion=.2)
			pilas.mundo.agregar_tarea(.2, self.conectar_eventos)
		else:
			self.conectar_eventos()
			
			
	def clickear_simulacion(self, evento):
		x, y = evento.x, evento.y
		
		# Esta tocando la simulación?                                                                  
		if self.nav.actores[self.nav.actual].area_contacto.colisiona_con_un_punto(x, y):
			self.desconectar_eventos()
			pilas.avisar("Lanzar simulación", retraso=2)
			pilas.mundo.agregar_tarea(1, self.conectar_eventos)
