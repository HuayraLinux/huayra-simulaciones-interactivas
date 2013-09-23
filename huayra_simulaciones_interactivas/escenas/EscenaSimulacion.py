# -*- encoding: utf-8 -*-
import pilas
import subprocess  # Para lanzar la simulación
import main
from pilas.escena import Base
from ..Simulacion import Simulacion


class EscenaSimulacion(pilas.escena.Base):
	
	def __init__(self):
		Base.__init__(self)
	
	
	def iniciar(self):
		fondo = pilas.fondos.Fondo("imagenes/gui/fondo_item.png")
		
		# posiciones corregidas
		x_titulo_corregida = pilas.escena_actual().camara.x - main.simulacion_activa.actores[0].x		
		x_screenshot_corregida = pilas.escena_actual().camara.x - main.simulacion_activa.actores[1].x		
		
		pilas.escena_actual().camara.x = 0
		
		descripcion = main.texto_a_lineas(main.simulacion_activa.descripcion, 45)
		descripcion = '\n'.join(descripcion)
		
		self.sim = Simulacion(
			titulo=main.simulacion_activa.titulo,
			screenshot=main.simulacion_activa.screenshot,
			descripcion=descripcion,
			archivo=main.simulacion_activa.archivo,
		)
		
		# Título
		titulo = self.sim.actores[0]
		titulo.x = x_titulo_corregida
		titulo.y = main.simulacion_activa.actores[0].y
		# Screenshot
		screenshot = self.sim.actores[1]
		screenshot.centro = ("centro", "arriba")
		screenshot.x = x_screenshot_corregida
		screenshot.y = main.simulacion_activa.actores[1].y
		# Descripción
		descripcion = self.sim.actores[2]
		descripcion.magnitud = 12
		descripcion.centro = ("izquierda", "arriba")
		# Área de contacto
		self.sim.area_contacto.y = 30
		
		# 
		# las posiciones dependen del tamaño del screenshot
		ancho_texto_activo = main.simulacion_activa.actores[0].ancho
		ancho_screenshot_activo = main.simulacion_activa.actores[1].ancho
		posicion_final_screenshot = -(main.pantalla_ancho / 2) + (ancho_screenshot_activo / 2) + 120
		posicion_final_titulo = posicion_final_screenshot + (ancho_screenshot_activo / 2) + (ancho_texto_activo / 2) + 20
 		titulo.x = pilas.interpolar(posicion_final_titulo, tipo='desaceleracion_gradual', duracion=1)
		screenshot.x = pilas.interpolar(posicion_final_screenshot, tipo='desaceleracion_gradual', duracion=1)
 		titulo.y = pilas.interpolar(self.sim.actores[1].y - 10, tipo='desaceleracion_gradual', duracion=1)
		descripcion.x = posicion_final_screenshot + (ancho_screenshot_activo/2) + 20
		descripcion.y = titulo.y - 80
		descripcion.transparencia = 100
		descripcion.transparencia = [0]
		
		" Flecha volver "
		self.boton_volver = pilas.actores.Boton(			
			ruta_normal='imagenes/gui/flecha_volver.png',
			ruta_press='imagenes/gui/flecha_volver_presionada.png',
			ruta_over='imagenes/gui/flecha_volver_over.png',
		)
		self.boton_volver.fijo = True
		self.boton_volver.x = 250
		self.boton_volver.y = -170
		self.boton_volver.conectar_presionado(self.cuando_pulsan_el_boton, arg="prev")
		self.boton_volver.conectar_sobre(self.cuando_pasa_sobre_el_boton, arg="prev")
		self.boton_volver.conectar_normal(self.cuando_deja_de_pulsar, arg="prev") 
		
		self.texto_volver = pilas.actores.Actor('imagenes/gui/label_volver.png', x=170, y=-160)
		
		
		" Lanzar "		
		pilas.escena_actual().termina_click.conectar(self.clickear_flecha, id='clickear_flecha')
		pilas.escena_actual().click_de_mouse.conectar(self.clickear_lanzador, id='clickear_lanzador')
		
	
	def cuando_pulsan_el_boton(self, arg):
		if arg == "next":
			self.next.pintar_presionado()
		else:
			self.boton_volver.pintar_presionado()

	def cuando_pasa_sobre_el_boton(self, arg):
		if arg == "next":
			self.next.pintar_sobre()
		else:
			self.boton_volver.pintar_sobre()

	def cuando_deja_de_pulsar(self, arg):
		if arg == "next":
			self.next.pintar_normal()
		else:
			self.boton_volver.pintar_normal()
			
				
	def volver(self):
		from EscenaSimulaciones import EscenaSimulaciones
		pilas.cambiar_escena(EscenaSimulaciones())

		
	def clickear_flecha(self, evento):
		x, y = evento.x, evento.y
		# Esta tocando la simulación?                                                                  
		if self.boton_volver.colisiona_con_un_punto(x, y):
			self.sim.x = pilas.interpolar(-1500, tipo='desaceleracion_gradual', duracion=1)
			pilas.mundo.agregar_tarea(1, self.volver)

		
	def clickear_lanzador(self, evento):
		x, y = evento.x, evento.y
		# Esta tocando la simulación?                                                                  
		if self.sim.actores[1].colisiona_con_un_punto(x, y):
			subprocess.call(['java', '-jar', Simulacion.sims_dir + self.sim.archivo])
			pilas.avisar(u"Lanzando simulación...", retraso=5)
		
		
		
		
#subprocess.call(['java', '-jar', Simulacion.sims_dir + self.nav.actores[self.nav.actual].archivo])
#pilas.avisar(u"Lanzando simulación...", retraso=5)
#pilas.mundo.agregar_tarea(5, self.conectar_eventos)
			
			
		
