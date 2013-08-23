# -*- encoding: utf-8 -*-
" Archivo para iniciar las variables globales de la aplicación "

DEBUG = True

def init():
	global sims
	sims = None
	simulacion_activa = None

def debug(msg, categoria='DEBUG'):
	if DEBUG:
		print "DEBUG:", msg
