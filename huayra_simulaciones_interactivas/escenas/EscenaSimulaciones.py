# -*- encoding: utf-8 -*-

import pilas
import pilas.evento
import main
from pilas.escena import Base
from ..Simulacion import Simulacion
from ..NavegacionSimulaciones import NavegacionSimulaciones
from EscenaSimulacion import EscenaSimulacion


class EscenaSimulaciones(pilas.escena.Base):
	
	nav = None  # Navegación de categorías
	camara_x = 0.0
	
	def __init__(self):
		Base.__init__(self)
			
	
	def iniciar(self):
		
		fondo = pilas.fondos.Fondo("imagenes/gui/fondo_lista.png")
		fondo.fijo = True
		
		# Categorías
		self.nav = NavegacionSimulaciones()
		i = 0
		for sim in main.sims.simulaciones:
			self.nav.actores.append(
				Simulacion(
					titulo=sim['titulo'].decode('utf8'), 
					screenshot=sim['screenshot'], 
					descripcion=sim['descripcion'].decode('utf8'),
					archivo=sim['archivo']
				)
			)
			# Título
			self.nav.actores[i].actores[0].y = 170
			#self.nav.actores[i].actores[0].color = pilas.colores.Color(155, 237, 79)
			# Screenshot
			self.nav.actores[i].actores[1].centro = ("centro", "arriba")
			self.nav.actores[i].actores[1].y = 130
			# Descripción
			self.nav.actores[i].actores[2].eliminar()
			# Área de contacto
			self.nav.actores[i].area_contacto.y = 30

			i = i+1


		self.nav.aparecer()
				
		# Flechas
		self.prev = pilas.actores.Boton(			
			ruta_normal='imagenes/gui/flecha_volver.png',
			ruta_press='imagenes/gui/flecha_volver_presionada.png',
			ruta_over='imagenes/gui/flecha_volver_over.png',
		)
		self.prev.fijo = True
		self.prev.x = -250
		self.prev.y = -170
		self.prev.conectar_presionado(self.cuando_pulsan_el_boton, arg="prev")
		self.prev.conectar_sobre(self.cuando_pasa_sobre_el_boton, arg="prev")
		self.prev.conectar_normal(self.cuando_deja_de_pulsar, arg="prev") 
				
		self.next = pilas.actores.Boton(			
			ruta_normal='imagenes/gui/flecha_proximo.png',
			ruta_press='imagenes/gui/flecha_proximo_presionada.png',
			ruta_over='imagenes/gui/flecha_proximo_over.png',
		)
		self.next.fijo = True
		self.next.x = 250
		self.next.y = -170
		self.next.conectar_presionado(self.cuando_pulsan_el_boton, arg="next")
		self.next.conectar_sobre(self.cuando_pasa_sobre_el_boton, arg="next")
		self.next.conectar_normal(self.cuando_deja_de_pulsar, arg="next") 
				
		
		self.conectar_eventos()
		
		ayuda = pilas.actores.TextoInferior(
			"Se puede navegar con las flechas del teclado, la rueda del mouse o haciendo click sobre las flechas",
			magnitud=12,
			autoeliminar=True
		)
		
		 
		 
	def cuando_pulsan_el_boton(self, arg):
		if arg == "next":
			self.next.pintar_presionado()
		else:
			self.prev.pintar_presionado()
		pilas.avisar("Han pulsado el boton")

	def cuando_pasa_sobre_el_boton(self, arg):
		if arg == "next":
			self.next.pintar_sobre()
		else:
			self.prev.pintar_sobre()
		pilas.avisar("Pasa el mouse sobre el boton")

	def cuando_deja_de_pulsar(self, arg):
		if arg == "next":
			self.next.pintar_normal()
		else:
			self.prev.pintar_normal()
	
	
	
	def conectar_eventos(self):
		pilas.escena_actual().click_de_mouse.conectar(self.mover, id='clickear_flechas')
		pilas.escena_actual().termina_click.conectar(self.clickear_simulacion, id='clickear_simulacion')
		pilas.escena_actual().mueve_rueda.conectar(self.mover, id='mover_simulaciones_desde_rueda')
		pilas.escena_actual().suelta_tecla.conectar(self.mover, id='mover_simulaciones_desde_teclado')
		
	
	def desconectar_eventos(self):
		pilas.escena_actual().click_de_mouse.desconectar_por_id('clickear_flechas')
		pilas.escena_actual().termina_click.desconectar_por_id('clickear_simulacion')
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
		
		if self.camara_x != pilas.escena_actual().camara.x:
			main.sims.sounds['navegacion_simulaciones_mover'].play()
			self.nav.setear_tamanios()
			pilas.escena_actual().camara.x = pilas.interpolar(self.camara_x, tipo='desaceleracion_gradual', duracion=.2)
			pilas.mundo.agregar_tarea(.2, self.conectar_eventos)
		else:
			self.conectar_eventos()
	
	
	def cambiar_escena(self):
		pilas.cambiar_escena(EscenaSimulacion())
		
			
	def clickear_simulacion(self, evento):
		x, y = evento.x, evento.y
		# Esta tocando la simulación?                                                                  
		if self.nav.actores[self.nav.actual].area_contacto.colisiona_con_un_punto(x, y):
			main.simulacion_activa = self.nav.actores[self.nav.actual]
			self.desconectar_eventos()
			
			self.nav.desaparecer_restantes()
			self.prev.transparencia = [100]
			self.next.transparencia = [100]
			
			pilas.mundo.agregar_tarea(1, self.cambiar_escena)

			
