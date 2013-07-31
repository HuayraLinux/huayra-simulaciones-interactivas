# -*- encoding: utf-8 -*-

import pilas
import os
import Config
from escenas import EscenaBienvenida
from CategoriaSimulacion import CategoriaSimulacion
from pprint import pprint

class SimulacionesInteractivas:
	
	data = None
	categorias = []
	simulaciones = []
			
	" Inicializa pilas y propiedades de las simulaciones "
	def iniciar(self):
		pilas.iniciar(ancho=1000, alto=600, titulo='Huayra - Simulaciones Interactivas', usar_motor='qtgl', \
			rendimiento=60, modo='detectar', gravedad=(0, 0), pantalla_completa=False, \
			permitir_depuracion=True, audio='phonon', centrado=True)
		
		pilas.fondos.Color(pilas.colores.negro)
		pilas.cambiar_escena(EscenaBienvenida())
		
		# Categorías		
		for categoria in self.data.categorias:
			self.categorias.append(categoria)
			categoria['actor'] = CategoriaSimulacion(categoria['screenshot'])
			categoria['actor'].x = 1000
			# Subcategorías
			#for subcat in categoria:
				#categoria['actor'] = pilas.actores.Actor(categoria['screenshot'])
		self.categorias[0]['actor'].x = 0
		pilas.ejecutar()

	" Cargar desde un archivo con formato dict de python "
	def cargar_simulaciones_desde_archivo(self, simulaciones_file):
		"El archivo es relativo a donde se ejecuta el script principal, y debe reemplazarse las barras por puntos"
		exec "from " + simulaciones_file + " import simulaciones"
		self.data = simulaciones

