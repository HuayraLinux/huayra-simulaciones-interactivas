# -*- encoding: utf-8 -*-

import pilas
import os
import Config
from xml_dict import ConvertXmlToDict
from pprint import pprint

class SimulacionesInteractivas:
	
	def __init__(self):
		self.xml_data = None
		self.data = {'categorias': []}
		#self.categorias = None
		
	
	def iniciar(self):		
		pilas.iniciar(ancho=800, alto=600, titulo='Huayra - Simulaciones Interactivas', usar_motor='qtgl', \
			rendimiento=60, modo='detectar', gravedad=(0, -90), pantalla_completa=False, \
			permitir_depuracion=True, audio='phonon', centrado=True)
		pilas.fondos.Color(pilas.colores.negro)
		#pilas.ejecutar()
	
	
	
	def leer_xml(self, xml_file):
		self.xml_data = ConvertXmlToDict(xml_file).simulaciones
		self._parse_data()

	"Transforma los datos del diccionario original a algo más 'legible'"
	def _parse_data(self):
		for cat in self.xml_data.categorias:
			self.data['categorias'].append([{
				'id': cat.id,
				'nombre': cat.nombre,
				'imagen': cat.imagen,
				'subcategorias': self._parse_subcategorias(cat.subcategorias),
			}])
		
	""" 
	Transforma las subcategorías en listas en caso de que sean diccionarios (cuando sólo hay una).
	Lo mismo con las simulaciones dentro de cada subcategoría
	"""
	def _parse_subcategorias(self, data):
		
		if isinstance(data, list):
			subcategorias = data
		else:
			subcategorias = [data]
			
		for subcat in subcategorias:
			if isinstance(subcat.sims, list):
				subcat.sims = subcat.sims
			else:
				subcat.sims = [subcat.sims]
				
		return subcategorias
			
				
