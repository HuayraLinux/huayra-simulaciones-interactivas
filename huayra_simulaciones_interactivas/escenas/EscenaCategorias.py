# -*- encoding: utf-8 -*-
import pilas
import main
from pilas.escena import Base
from ..CategoriaSimulacion import CategoriaSimulacion
from ..NavegacionCategorias import NavegacionCategorias

class EscenaCategorias(pilas.escena.Base):
	
	def __init__(self):
		Base.__init__(self)
	
	def iniciar(self):
		pilas.fondos.Color(pilas.colores.gris)
		
		# Categorías
		nav = NavegacionCategorias()
		i = 0
		for categoria in main.sim.data['categorias']:
			categoria['actor'] = CategoriaSimulacion(
				titulo=categoria['nombre'], 
				screenshot=categoria['screenshot'], 
				descripcion=categoria['descripcion'],
				x=i* (CategoriaSimulacion.ancho + CategoriaSimulacion.separacion)
			)
			i += 1
			categoria['actor'].actores.transparencia = 100
			categoria['actor'].actores.transparencia = [100, 0]
			nav.actores.append(categoria['actor'])
		nav.actores.transparencia = [100, 0]
		nav.calcular_medidas()
		print "Ancho navegación: ", nav.ancho
			
		print "Total categorías:", CategoriaSimulacion.total
