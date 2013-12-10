# -*- encoding: utf-8 -*-
" Archivo para iniciar las variables globales de la aplicación "
import os

DEBUG = False
pantalla_ancho = 900
pantalla_alto = 500
data_dir = os.path.dirname(os.path.abspath(__file__)) + '/'

def init():
	sims = None
	simulacion_activa = None


def debug(msg, categoria='DEBUG'):
	if DEBUG:
		print "DEBUG:", msg


def texto_a_lineas(texto, caracteres_por_linea, separador=' '):
	lineas = []
	texto = texto
	longitud = len(texto)	
	desde = 0
	hasta = 0
	
	while longitud > 0:
		
		if longitud <= caracteres_por_linea:
			lineas.append(texto)
			break

		hasta = texto.find(separador, caracteres_por_linea)  # la posición del próximo separador a partir de caracteres_por_linea
		porcion = texto[desde:hasta]
		lineas.append(porcion.strip())
		texto = texto[len(porcion):]
		longitud = len(texto)
		
	return lineas
