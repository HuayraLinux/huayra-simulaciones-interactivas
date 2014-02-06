# -*- encoding: utf-8 -*-
import pilas
from pilas.escena import Base
from EscenaSimulacion import EscenaSimulacion
import main
import subprocess

class EscenaSimulacionEnCurso(pilas.escena.Base):
	
	def __init__(self, archivo):
		Base.__init__(self)
		
		self.archivo = archivo
	
	
	def iniciar(self):
		fondo = pilas.fondos.Fondo(main.data_dir + "imagenes/gui/fondo_lista.png")
		pilas.mundo.agregar_tarea(.5, self.lanzar_simulacion)
		pilas.mundo.agregar_tarea(3, self.conectar_click)
		
		grilla = pilas.imagenes.cargar_grilla(main.data_dir + "imagenes/gui/grilla-engranajes.png", 3)
		self.engranajes = pilas.actores.Animacion(grilla, ciclica=True)
		
		
		

	def lanzar_simulacion(self):
		subprocess.Popen(['java', '-jar', main.data_dir + 'data/simulaciones/' + self.archivo])
		
		
	def conectar_click(self):		
		pilas.eventos.click_de_mouse.conectar(self.clickeado)
		pilas.actores.TextoInferior("Click en la pantalla para volver")


	def clickeado(self, evento):
		pilas.recuperar_escena()
