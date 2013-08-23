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
		
		sim = Simulacion(
			titulo=main.simulacion_activa.titulo,
			screenshot=main.simulacion_activa.screenshot,
			descripcion=main.simulacion_activa.descripcion,
			archivo=main.simulacion_activa.archivo,
		)		
		# Título
		sim.actores[0].y = 200
		# Screenshot
		sim.actores[1].y = 60
		# Descripción
		sim.actores[2].magnitud = 12
		sim.actores[2].centro = ("izquierda", "arriba")
		sim.actores[2].transparencia = 100
		sim.actores[2].transparencia = [0]
		sim.actores[2].y = 150
		sim.actores[2].x = 160
		# Área de contacto
		sim.area_contacto.y = 30
		
		sim.x = pilas.interpolar(-250, tipo='desaceleracion_gradual', duracion=1)
		
		" Flecha volver "
		flecha_prev = pilas.imagenes.cargar_grilla("imagenes/DDR___Arrow_by_Blade_Genexis.png", 2)
		self.boton_volver = pilas.actores.Actor(flecha_prev)
		self.boton_volver.transparencia = 100
		self.boton_volver.x = 400
		self.boton_volver.y = -200
		self.boton_volver.transparencia = [0]
		
		
		
		
#subprocess.call(['java', '-jar', Simulacion.sims_dir + self.nav.actores[self.nav.actual].archivo])
#pilas.avisar(u"Lanzando simulación...", retraso=5)
#pilas.mundo.agregar_tarea(5, self.conectar_eventos)
			
			
		
