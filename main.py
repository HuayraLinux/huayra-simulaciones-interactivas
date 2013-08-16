# -*- encoding: utf-8 -*-
" Archivo para iniciar las variables globales de la aplicación "

DEBUG = True

def init():
	global sim
	sim = None

def debug(msg, categoria='DEBUG'):
	if DEBUG:
		print "DEBUG:", msg
