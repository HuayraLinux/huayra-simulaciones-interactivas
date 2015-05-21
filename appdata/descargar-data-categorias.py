#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import urllib2, json, os, shutil
import pprint
from BeautifulSoup import BeautifulSoup
import io
import sys

if os.path.exists('data'):
	shutil.rmtree('data/')
os.makedirs('data/')
os.makedirs('data/screenshots')
os.makedirs('data/screenshots/thumbs')
os.makedirs('data/simulaciones')
io.open('data/__init__.py', 'w')

HOST = 'phet.colorado.edu'
PROTOCOL = 'http'
INDEX_URL = '/es/simulations/category/new'
INDEX_URL = '/es/simulations/index'
SIM_URL = '/es/simulation/'

NO_PARSEAR = [u'Todas las simulaciones', u'Simulaciones traducidas', u'Según el grado escolar',
              u'Nuevas Simulaciones', u'By Device']







def pseudo_slug(path):
        return path.split('/')[::-1][0]

def parsear_simulacion(sim_id, thumb_url):
	sim_page = urllib2.urlopen('%s://%s%s%s' % (PROTOCOL, HOST, SIM_URL, sim_id))
	sim_soup = BeautifulSoup(sim_page)

	contenedor = sim_soup.find('table', attrs={'class': 'simulation-main-table'})

	screenshot_url = contenedor.find('img', attrs={'class': 'simulation-main-screenshot'}).get('src'),
	screenshot_url = screenshot_url[0]
	screenshot = screenshot_url.split('/')[-1]

	archivo_url = contenedor.find('a', attrs={'class': 'sim-download sim-button'}).get('href')
	if archivo_url.endswith('?download'):
		archivo_url = archivo_url[:-9]
	archivo = archivo_url.split('/')[-1]
	
	thumb = thumb_url.split('/')[-1]
	
	sim_data = {
		'titulo': sim_soup.find('h1', attrs={'class': 'simulation-main-title'}).contents[0],
		'descripcion': contenedor.find('span', attrs={'itemprop': 'description about'}).contents[0],
		'screenshot': screenshot,
		'thumb': thumb,
		'archivo': archivo,
		'categorias': []
	}
	
	guardar_archivos(thumb_url, thumb, screenshot_url, screenshot, archivo_url, archivo)

	return sim_data


def guardar_archivos(thumb_url, thumb, screenshot_url, screenshot, archivo_url, archivo):

	# thumb
        print "%s" % thumb_url
	# thumbData = urllib2.urlopen("%s" % thumb_url).read()
	# output = open('data/screenshots/thumbs/' + thumb, 'wb')
	# output.write(thumbData)
	# output.close()

	# imagen
	print "%s://%s%s" % (PROTOCOL, HOST, screenshot_url)
	# imgData = urllib2.urlopen("%s://%s%s" % (PROTOCOL, HOST, screenshot_url)).read()
	# output = open('data/screenshots/' + screenshot, 'wb')
	# output.write(imgData)
	# output.close()

	# Jar
        print "%s://%s%s" % (PROTOCOL, HOST, archivo_url)
	# jarData = urllib2.urlopen("%s://%s%s" % (PROTOCOL, HOST, archivo_url)).read()
	# out = open('data/simulaciones/' + archivo, 'wb')
	# out.write(jarData)
	# out.close()





index_page = urllib2.urlopen('%s://%s%s' % (PROTOCOL, HOST, INDEX_URL))
index_soup = BeautifulSoup(index_page)

lcategorias = index_soup.body.find('div', attrs={'class' : 'side-nav'}).findAll('a', attrs={'class' : 'nml-link nav1'})
links_categorias = dict([(pseudo_slug(l['href']),
                          {'categoria': l.contents[1].contents[0],
                           'url': l['href'].rstrip('/')+'/index',
                           'simulaciones': []})
                         for l in filter(lambda l: l.text not in NO_PARSEAR, lcategorias)])


lsimulaciones = index_soup.body.find('div', attrs={'class' : 'simulation-index'}).findAll('a')
links_simulaciones = dict([(pseudo_slug(l['href']),
                            {'url': l['href']})
                           for l in lsimulaciones])

cnt = 0
simulaciones = {}
categorias = {u'Todas las simulaciones': []}


for categoria in links_categorias:
        print categoria #, links_categorias[categoria]['categoria'], links_categorias[categoria]['url']

	cat_page = urllib2.urlopen('%s://%s%s' % (PROTOCOL, HOST, links_categorias[categoria]['url']))
	cat_soup = BeautifulSoup(cat_page) # or ketchup
        links_sim_cat = cat_soup.body.find('div', attrs={'class' : 'simulation-index'}).findAll('a')
        links_categorias[categoria]['simulaciones'] = [pseudo_slug(l['href']) for l in links_sim_cat]


print links_categorias

sys.exit()
	


for link in links_categorias:
	
	pagina_categoria = urllib2.urlopen('%s://%s%s' % (PROTOCOL, HOST, link['url']))
	pagina_sopeada = BeautifulSoup(pagina_categoria)
	categoria = pagina_sopeada.body.find('h1', attrs={'class': 'main-breadcrumb'}).parent()[-1].contents[0]
	sims = pagina_sopeada.findAll('td', attrs={'class': 'simulation-list-item'})
	
	categorias[categoria] = []
	
	#print "Sims en la categoría:", sims
	
	for sim in sims:
		sim_url = sim.a['href']
		sim_id = sim_url.split('/')[-1]
		

		
		if sim_id not in simulaciones:
			cnt = cnt + 1
			thumb_url = sim.a.img['src']
			# entrar a la simulacion y parsearla simulacion
			sim_data = parsear_simulacion(sim_id, thumb_url)
			simulaciones[sim_id] = sim_data
			categorias['Todas las simulaciones'].append(sim_id) # agregando la simulación a la categoría principal
			print "Sim (" + str(cnt) + "):", sim_id
			
		simulaciones[sim_id]['categorias'].append(categoria) # agrego la categoría a la simulación en sí
		try:
			categorias[categoria].append(sim_id) # agrego la simulación a otra categoría
		except:
			pass
		#pprint.pprint(categorias[categoria])


print "Total %d simulaciones" % (cnt)

for cat, sim_list in categorias.iteritems():
	sim_list.sort()

with io.open('data/simulaciones_categorias.py', 'w', encoding='utf-8') as f:
	f.write(unicode("# -*- encoding: utf-8 -*-\n\n"))
	f.write(unicode("\n\n"))
	f.write(unicode("categorias = "))
	f.write(unicode(json.dumps(categorias, ensure_ascii=False, indent=4)))
	f.write(unicode("\n\n"))
	f.write(unicode("simulaciones = "))
	f.write(unicode(json.dumps(simulaciones, ensure_ascii=False, indent=4)))
	
	
