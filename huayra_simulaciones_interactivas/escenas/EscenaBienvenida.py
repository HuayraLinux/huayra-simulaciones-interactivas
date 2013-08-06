# -*- encoding: utf-8 -*-
import pilas
from pilas.escena import Base
from EscenaCategorias import EscenaCategorias

class EscenaBienvenida(pilas.escena.Base):
	
	def __init__(self):
		Base.__init__(self)
	
	
	def iniciar(self):
		pilas.fondos.Color(pilas.colores.negro)
		self.texto = pilas.actores.Texto("Simulaciones Interactivas")
		pilas.eventos.click_de_mouse.conectar(self.texto_clickeado)
	
		
	def texto_clickeado(self, evento):
		# Obtengo la posicion del mouse.
		x, y = evento.x, evento.y
		# Esta colisionando con la pelota?                                                                           
		if self.texto.colisiona_con_un_punto(x, y):
			pilas.cambiar_escena(EscenaCategorias())

