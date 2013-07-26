import pilas
print pilas.escena.Normal

class EscenaBienvenida(pilas.escena.Normal):
	
	def __init__(self):
		pilas.escena.Normal.__init__(self)
	
	def iniciar(self):
		pilas.fondo.Tarde()
		texto = pilas.actores.Texto("Simulaciones Interactivas")
