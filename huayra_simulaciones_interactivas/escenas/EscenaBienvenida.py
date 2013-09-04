# -*- encoding: utf-8 -*-
import pilas
from pilas.escena import Base
from EscenaSimulaciones import EscenaSimulaciones

class EscenaBienvenida(pilas.escena.Base):
	
	def __init__(self):
		Base.__init__(self)
	
	
	def iniciar(self):
		pilas.fondos.Color(pilas.colores.negro)
		self.texto = pilas.actores.Texto("Simulaciones Interactivas")
		pilas.eventos.click_de_mouse.conectar(self.texto_clickeado)
	
	
	def cambiar_escena(self):
		pilas.cambiar_escena(EscenaSimulaciones())
		
		
	def texto_clickeado(self, evento):
		# Obtengo la posicion del mouse.
		x, y = evento.x, evento.y
		# Esta colisionando con el texto de bienvenida?                                                                         
		if self.texto.colisiona_con_un_punto(x, y):
			pilas.mundo.agregar_tarea(1, self.cambiar_escena)
