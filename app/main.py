# -*- encoding: utf-8 -*-
" Archivo para iniciar las variables globales de la aplicación "
import os

DEBUG = False
pantalla_ancho = 900
pantalla_alto = 500
data_dir = os.path.dirname(os.path.abspath(__file__)) + '/'
navegacion_camara_x = 0.0
simulacion_actual = 0
categoria_actual = u'Todas las simulaciones'

def init():
	sims = None
	simulacion_activa = None
	categorias = None


def debug(msg, categoria='DEBUG'):
	if DEBUG:
		print "DEBUG:", msg
