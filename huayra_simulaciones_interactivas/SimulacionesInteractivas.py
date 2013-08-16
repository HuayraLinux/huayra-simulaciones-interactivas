# -*- encoding: utf-8 -*-

import pilas
import os
import random
import Config
from escenas import EscenaBienvenida
import pprint
import pygame.mixer

class SimulacionesInteractivas:
	
	simulaciones = []
	pantalla_ancho = 900
	pantalla_alto = 500
	sounds = []
			
	" Inicializa pilas y propiedades de las simulaciones "
	def iniciar(self):
		pilas.iniciar(
			ancho=SimulacionesInteractivas.pantalla_ancho, 
			alto=SimulacionesInteractivas.pantalla_alto, 
			titulo='Huayra - Simulaciones Interactivas', 
			usar_motor='qtgl',
			rendimiento=60, 
			modo='detectar', 
			gravedad=(0, 0), 
			pantalla_completa=False,
			permitir_depuracion=True, 
			audio='phonon', 
			centrado=True
		)
		
		pygame.mixer.init()	
		self.sounds = {
			'navegacion_simulaciones_mover': pygame.mixer.Sound('sounds/Arcade_S-wwwbeat-8529_hifi.ogg'),
			'navegacion_simulaciones_aceptar': pygame.mixer.Sound('sounds/RewardSo-Mark_E_B-8078_hifi.ogg'),
		}
					
		
		pilas.fondos.Color(pilas.colores.gris)
		pilas.cambiar_escena(EscenaBienvenida())	
		pilas.ejecutar()

	" Cargar desde un archivo con formato dict de python "
	def cargar_simulaciones_desde_archivo(self, simulaciones_file):
		"El archivo es relativo a donde se ejecuta el script principal, y debe reemplazarse las barras por puntos"
		exec "from " + simulaciones_file + " import simulaciones"
		self.simulaciones = simulaciones

