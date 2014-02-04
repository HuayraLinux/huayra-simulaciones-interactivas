# -*- encoding: utf-8 -*-
import pilas
import subprocess  # Para lanzar la simulación
import main
from pilas.escena import Base
from huayra_simulaciones_interactivas.actores.Simulacion import Simulacion


class EscenaSimulacion(pilas.escena.Base):
	
	def __init__(self):
		Base.__init__(self)
	
	
	def iniciar(self):
		fondo = pilas.fondos.Fondo(main.data_dir + "imagenes/gui/fondo_item.png")
				
		self.sim = Simulacion(
			titulo=main.simulacion_activa.titulo,
			screenshot=main.simulacion_activa.screenshot,
			descripcion=main.simulacion_activa.descripcion,
			archivo=main.simulacion_activa.archivo,
		)
		
		# Screenshot
		screenshot = self.sim.actores[1]
		screenshot.x = main.simulacion_activa.actores[1].x
		screenshot.y = main.simulacion_activa.actores[1].y
		screenshot.centro = ("centro", "arriba")
				
		# Título
		titulo = self.sim.actores[0]
		
		titulo.x = 0
		titulo.y = main.simulacion_activa.actores[0].y
		titulo.ancho = 440
		titulo.centro = ('izquierda', 'arriba')
		
		# Descripción
		descripcion = self.sim.actores[2]
		descripcion.magnitud = 12
		descripcion.ancho = 440
		descripcion.centro = ('izquierda', 'arriba')
		
		# Área de contacto
		# self.sim.area_contacto.y = 30
		
		# 
		# las posiciones dependen del tamaño del screenshot
		ancho_screenshot_activo = main.simulacion_activa.actores[1].ancho
		posicion_final_screenshot = -380 + (ancho_screenshot_activo / 2)
		posicion_final_texto = -380 + (ancho_screenshot_activo) + 20
 		
 		titulo.x = pilas.interpolar(posicion_final_texto, tipo='desaceleracion_gradual', duracion=1)
 		titulo.y = pilas.interpolar(self.sim.actores[1].y - 10, tipo='desaceleracion_gradual', duracion=1)
		
		screenshot.x = pilas.interpolar(posicion_final_screenshot, tipo='desaceleracion_gradual', duracion=1)
 		
		descripcion.x = posicion_final_texto
		descripcion.y = titulo.y - titulo.alto - 60
		descripcion.transparencia = 100
		descripcion.transparencia = [0]
		
		" Flecha volver "
		self.boton_volver = pilas.actores.Boton(			
			ruta_normal=main.data_dir + 'imagenes/gui/flecha_volver.png',
			ruta_press=main.data_dir + 'imagenes/gui/flecha_volver_presionada.png',
			ruta_over=main.data_dir + 'imagenes/gui/flecha_volver_over.png',
		)
		self.boton_volver.fijo = True
		self.boton_volver.x = 250
		self.boton_volver.y = -170
		self.boton_volver.conectar_presionado(self.cuando_pulsan_el_boton, arg="boton_volver")
		self.boton_volver.conectar_sobre(self.cuando_pasa_sobre_el_boton, arg="boton_volver")
		self.boton_volver.conectar_normal(self.cuando_deja_de_pulsar, arg="boton_volver") 
		
		self.texto_volver = pilas.actores.Actor(main.data_dir + 'imagenes/gui/label_volver.png', x=170, y=-160)
		
		" Botón lanzar "
		self.boton_lanzar = pilas.actores.Boton(			
			ruta_normal=main.data_dir + 'imagenes/gui/simular_normal.png',
			ruta_press=main.data_dir + 'imagenes/gui/simular_presionada.png',
			ruta_over=main.data_dir + 'imagenes/gui/simular_over.png',
		)
		self.boton_lanzar.fijo = True
		self.boton_lanzar.x = 340
		self.boton_lanzar.y = -170
		self.boton_lanzar.conectar_presionado(self.cuando_pulsan_el_boton, arg="boton_lanzar")
		self.boton_lanzar.conectar_sobre(self.cuando_pasa_sobre_el_boton, arg="boton_lanzar")
		self.boton_lanzar.conectar_normal(self.cuando_deja_de_pulsar, arg="boton_lanzar") 
		
		self.texto_volver = pilas.actores.Actor(main.data_dir + 'imagenes/gui/label_volver.png', x=170, y=-160)
		
		
		" Lanzar "
		pilas.escena_actual().termina_click.conectar(self.clickear_flecha, id='clickear_flecha')
		pilas.escena_actual().mueve_mouse.conectar(self.mouse_sobre_lanzador, id='sobre_lanzador')
		pilas.escena_actual().click_de_mouse.conectar(self.clickear_lanzador, id='clickear_lanzador')
		
	
	def cuando_pulsan_el_boton(self, arg):
		try:
			getattr(self, arg).pintar_presionado()
		except Error:
			pass


	def cuando_pasa_sobre_el_boton(self, arg):
		try:
			getattr(self, arg).pintar_sobre()
		except Error:
			pass


	def cuando_deja_de_pulsar(self, arg):
		try:
			getattr(self, arg).pintar_normal()
		except Error:
			pass
			
				
	def volver(self):
		from EscenaSimulaciones import EscenaSimulaciones
		pilas.cambiar_escena(EscenaSimulaciones())

		
	def clickear_flecha(self, evento):
		x, y = evento.x, evento.y
		# Esta tocando la flecha para volver?                                                                  
		if self.boton_volver.colisiona_con_un_punto(x, y):
			self.sim.x = pilas.interpolar(-1500, tipo='desaceleracion_gradual', duracion=1)
			pilas.mundo.agregar_tarea(0.5, self.volver)

		
	def mouse_sobre_lanzador(self, evento):
		x, y = evento.x, evento.y
		# Esta tocando la simulación?                                                                  
		if self.sim.actores[1].colisiona_con_un_punto(x, y) or self.boton_lanzar.colisiona_con_un_punto(x, y):
			pilas.avisar(u"Click para lanzar simulación...", retraso=5)

		
	def clickear_lanzador(self, evento):
		x, y = evento.x, evento.y
		# Esta tocando la simulación?                             
		if self.sim.actores[1].colisiona_con_un_punto(x, y) or self.boton_lanzar.colisiona_con_un_punto(x, y):
			pilas.avisar(u"Lanzando simulación...", retraso=5)
			subprocess.call(['java', '-jar', main.data_dir + 'data/simulaciones/' + self.sim.archivo])
