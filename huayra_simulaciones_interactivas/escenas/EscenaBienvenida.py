# -*- encoding: utf-8 -*-
import pilas
from pilas.escena import Base
from EscenaSimulaciones import EscenaSimulaciones
import main

class EscenaBienvenida(pilas.escena.Base):
	
	def __init__(self):
		Base.__init__(self)
	
	
	def iniciar(self):
		fondo = pilas.fondos.Fondo(main.data_dir + "imagenes/gui/portada.png")
		pilas.avisar("Click en la pantalla para empezar")
		pilas.eventos.click_de_mouse.conectar(self.clickeado)

	
	def cambiar_escena(self):
		pilas.cambiar_escena(EscenaSimulaciones())
		
		
	def clickeado(self, evento):
		pilas.mundo.agregar_tarea(1, self.cambiar_escena)
