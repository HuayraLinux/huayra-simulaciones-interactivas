# -*- encoding: utf-8 -*-

import pilas
import os
import Config
from xml_dict import ConvertXmlToDict
from pprint import pprint

class SimulacionesInteractivas:
	
	data = None
	categorias = []
	simulaciones = []
			
	
	def iniciar(self):		
		pilas.iniciar(ancho=800, alto=600, titulo='Huayra - Simulaciones Interactivas', usar_motor='qtgl', \
			rendimiento=60, modo='detectar', gravedad=(0, -90), pantalla_completa=False, \
			permitir_depuracion=True, audio='phonon', centrado=True)
		pilas.fondos.Color(pilas.colores.negro)
		#pilas.ejecutar()
	

	" Cargar desde un archivo con formato dict de python "
	def cargar_simulaciones_desde_archivo(self, simulaciones_file):
		"El archivo es relativo a donde se ejecuta el script principal, y debe reemplazarse las barras por puntos"
		exec "from " + simulaciones_file + " import simulaciones"
		self.data = simulaciones
		self.categorias = self.data['categorias']
