# -*- encoding: utf-8 -*-

import pilas
import os
import Config
from xml_dict import ConvertXmlToDict

class SimulacionesInteractivas:
	
	def __init__(self):
		self.data = None
		#self.categorias = None
		
	
	def iniciar(self):		
		pilas.iniciar(ancho=800, alto=600, titulo='Huayra - Simulaciones Interactivas', usar_motor='qtgl', \
			rendimiento=60, modo='detectar', gravedad=(0, -90), pantalla_completa=False, \
			permitir_depuracion=True, audio='phonon', centrado=True)
		pilas.fondos.Color(pilas.colores.negro)
		#pilas.ejecutar()
		

	def leer_xml(self, xml_file):
		self.data = ConvertXmlToDict(xml_file).simulaciones
	
		

