# -*- encoding: utf-8 -*-

import pilas
import os
import random
import Config
from escenas import EscenaBienvenida

class SimulacionesInteractivas:
	
	data = None
	categorias = []
	simulaciones = []
	pantalla_ancho = 1000
	pantalla_alto = 600
			
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
		
		pilas.fondos.Color(pilas.colores.gris)
		pilas.cambiar_escena(EscenaBienvenida())
		
		# Categorías
		for categoria in self.data['categorias']:
			self.categorias.append(categoria)
						
		pilas.ejecutar()

	" Cargar desde un archivo con formato dict de python "
	def cargar_simulaciones_desde_archivo(self, simulaciones_file):
		"El archivo es relativo a donde se ejecuta el script principal, y debe reemplazarse las barras por puntos"
		exec "from " + simulaciones_file + " import simulaciones"
		self.data = simulaciones

