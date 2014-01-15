# -*- encoding: utf-8 -*-

import pilas

class ListaSeleccion(pilas.interfaz.ListaSeleccion):
    
    def __init__(self, opciones, funcion_a_ejecutar=None, x=0, y=0, indice_opcion_seleccionada=None):
        self.indice_opcion_seleccionada = indice_opcion_seleccionada
        pilas.interfaz.ListaSeleccion.__init__(self, opciones=opciones, funcion_a_ejecutar=funcion_a_ejecutar, x=x, y=y)
        self._pintar_opciones(self.indice_opcion_seleccionada)
        
        
    def _pintar_opciones(self, pinta_indice_opcion=None):
        self.imagen.pintar(pilas.colores.blanco)
        self.imagen.rectangulo(0, self.indice_opcion_seleccionada * (self.alto_opcion + (self.separacion_entre_opciones * 2)), self.imagen.ancho(), self.alto_opcion + (self.separacion_entre_opciones * 2), relleno=True, color=pilas.colores.Color(162, 226, 93))
        
        if pinta_indice_opcion != None and pinta_indice_opcion != self.indice_opcion_seleccionada:
            self.imagen.rectangulo(0, pinta_indice_opcion * (self.alto_opcion + (self.separacion_entre_opciones * 2)), self.imagen.ancho(), self.alto_opcion + (self.separacion_entre_opciones * 2), relleno=True, color=pilas.colores.naranja)

        for indice, opcion in enumerate(self.opciones):
            self.imagen.texto(opcion, 15, y=self.alto_opcion * indice + 1 +(self.separacion_entre_opciones * 2 * indice), color=pilas.colores.negro)
