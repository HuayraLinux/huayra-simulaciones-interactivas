# -*- encoding: utf-8 -*-

simulaciones = {
	'categorias': [
		{
			'id': 'fisica', 
			'nombre': 'Física',
			'screenshot': 'imagenes/screenshots/fisica.png',
			'descripcion': 'Lorem ipsum blah blah',
			'subcategorias': [
				{
					'id': 'movimiento',
					'nombre': 'Movimiento',
					'screenshot': 'imagenes/screenshots/movimiento.png',
					'simulaciones': [
						{
							'id': 'fuerzas-movimiento-fundamentos',
							'nombre': 'Fuerzas y Movimiento: Fundamentos',
							'screenshot': 'imagenes/screenshots/forces-and-motion-basics-screenshot.png',
							'descripcion': 'Explora las fuerzas que actúan en un tira y afloja o empuje un refrigerador, caja, o una persona. Crea una fuerza aplicada y ver cómo se hace mover objetos. Cambia la fricción y observa cómo afecta el movimiento de los objetos.',
							'file': '---'
						},
					]
				},
				{
					'id': 'sonido_ondas',
					'nombre': 'Sonido &amp; ondas',
					'screenshot': 'imagenes/screenshots/sonido_ondas.png',
					'simulaciones': [
						{
							'id': 'frecuencias-resonantes',
							'nombre': 'Frecuencias resonantes',
							'screenshot': 'imagenes/screenshots/normal-modes-screenshot.png',
							'descripcion': 'Juega con un sistema de 1D o 2D de resortes osciladores acoplados. Varía el número de masas, ajusta las condiciones iniciales, y observa que el sistema evolucione. Ve todo el espectro de frecuencias resonantes del movimiento arbitrario. Véase las frecuencias longitudinales y transversales en el sistema 1D.',
							'file': '---'
						},
						{
							'id': 'interferencia-onda',
							'nombre': 'Interferencia De la Onda',
							'screenshot': 'imagenes/screenshots/wave-interference-screenshot.png',
							'descripcion': 'Haz ondas con un grifo que gotea, altavoces de audio, o láser! Añade una segunda fuente o un par de rendijas para crear un patrón de interferencia.',
							'file': '---'
						},
					]
				},
			],
		}, # fin categoría Física
		{
			'id': 'biologia', 
			'nombre': 'Biología',
			'screenshot': 'imagenes/screenshots/forces-and-motion-basics-screenshot.png',
			'descripcion': 'Lorem ipsum blah blah',
			'subcategorias': [
				{
					'id': None,
					'nombre': None,
					'screenshot': 'imagenes/screenshots/movimiento.png',
					'simulaciones': [
						{
							'id': 'fuerzas-movimiento-fundamentos',
							'nombre': 'Fuerzas y Movimiento: Fundamentos',
							'screenshot': 'imagenes/screenshots/forces-and-motion-basics-screenshot.png',
							'descripcion': 'Explora las fuerzas que actúan en un tira y afloja o empuje un refrigerador, caja, o una persona. Crea una fuerza aplicada y ver cómo se hace mover objetos. Cambia la fricción y observa cómo afecta el movimiento de los objetos.',
							'file': '---'
						},
					]
				},
			],
		}, # fin categoría Biología
	], # fin categorías
}
