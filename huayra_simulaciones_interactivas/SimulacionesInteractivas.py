# -*- encoding: utf-8 -*-

import pilas
import os
import random
from escenas import EscenaBienvenida
import pprint
import pygame.mixer
import main

class SimulacionesInteractivas:
	
	simulaciones = []
	sounds = []
			
	" Inicializa pilas y propiedades de las simulaciones "
	def iniciar(self):
		pilas.iniciar(
			ancho=main.pantalla_ancho, 
			alto=main.pantalla_alto, 
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
			'navegacion_simulaciones_mover': pygame.mixer.Sound(main.data_dir + 'sonidos/Arcade_S-wwwbeat-8529_hifi.ogg'),
			'navegacion_simulaciones_aceptar': pygame.mixer.Sound(main.data_dir + 'sonidos/RewardSo-Mark_E_B-8078_hifi.ogg'),
		}
					
		
		pilas.fondos.Color(pilas.colores.gris)
		pilas.cambiar_escena(EscenaBienvenida())	
		pilas.ejecutar()

	" Cargar desde un archivo con formato dict de python "
	def cargar_simulaciones_desde_archivo(self, simulaciones_file):
		"El archivo es relativo a donde se ejecuta el script principal, y debe reemplazarse las barras por puntos"
		exec "from " + simulaciones_file + " import simulaciones"
		self.simulaciones = simulaciones

