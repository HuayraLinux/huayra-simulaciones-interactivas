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
		pilas.escena_actual().camara.x = 0
		
		descripcion = main.texto_a_lineas(main.simulacion_activa.descripcion, 50)
		descripcion = '\n'.join(descripcion)

		self.sim = Simulacion(
			titulo=main.simulacion_activa.titulo,
			screenshot=main.simulacion_activa.screenshot,
			descripcion=descripcion,
			archivo=main.simulacion_activa.archivo,
		)		
		# Título
		self.sim.actores[0].y = 200
		# Screenshot
		self.sim.actores[1].y = 60
		# Descripción
		self.sim.actores[2].magnitud = 12
		self.sim.actores[2].centro = ("izquierda", "arriba")
		self.sim.actores[2].transparencia = 100
		self.sim.actores[2].transparencia = [0]
		self.sim.actores[2].y = 150
		self.sim.actores[2].x = 170
		# Área de contacto
		self.sim.area_contacto.y = 30
		
		self.sim.x = pilas.interpolar(-250, tipo='desaceleracion_gradual', duracion=1)
		
		" Flecha volver "
		flecha_prev = pilas.imagenes.cargar_grilla("imagenes/DDR___Arrow_by_Blade_Genexis.png", 2)
		self.boton_volver = pilas.actores.Actor(flecha_prev)
		self.boton_volver.transparencia = 100
		self.boton_volver.x = 400
		self.boton_volver.y = -200
		self.boton_volver.transparencia = [0]
		
		pilas.escena_actual().click_de_mouse.conectar(self.clickear_flecha, id='clickear_flecha')
		
	
	def volver(self):
		from EscenaSimulaciones import EscenaSimulaciones
		pilas.cambiar_escena(EscenaSimulaciones())

		
	def clickear_flecha(self, evento):
		x, y = evento.x, evento.y
		# Esta tocando la simulación?                                                                  
		if self.boton_volver.colisiona_con_un_punto(x, y):
			self.sim.x = pilas.interpolar(-1500, tipo='desaceleracion_gradual', duracion=1.5)
			pilas.mundo.agregar_tarea(1, self.volver)
		
		
		
		
#subprocess.call(['java', '-jar', Simulacion.sims_dir + self.nav.actores[self.nav.actual].archivo])
#pilas.avisar(u"Lanzando simulación...", retraso=5)
#pilas.mundo.agregar_tarea(5, self.conectar_eventos)
			
			
		
