#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import urllib2, json, os
from BeautifulSoup import BeautifulSoup
 
HOST='phet.colorado.edu'
PROTOCOL='http'
INDEX_URL='/es/simulations/index'
SIM_URL='/es/simulation/'
 
index_page = urllib2.urlopen('%s://%s%s' % (PROTOCOL,HOST,INDEX_URL))
index_soup = BeautifulSoup(index_page)
 
div_sims = index_soup.body.find('div', attrs={'class' : 'simulation-index'})
 
cnt = 0
simulaciones = []

if not os.path.exists('data/screenshots'):
	os.makedirs('data/screenshots')
if not os.path.exists('data/simulaciones'): 
	os.makedirs('data/simulaciones')

for div_letter in div_sims.findAll('div'):
	link_sims = div_letter.findAll('a', href=True)
	for sims in link_sims:
		cnt = cnt+1
		url = sims['href']
 
		sim_id = url.replace(SIM_URL, '')
		
		print 'Procesando (%d): %s' % (cnt, sim_id)
		sim_page = urllib2.urlopen('%s://%s%s' % (PROTOCOL, HOST, url))
		sim_soup = BeautifulSoup(sim_page)
		contenedor = sim_soup.find('table', attrs={'class': 'simulation-main-table'})
		screenshot_url = contenedor.find('img', attrs={'class': 'simulation-main-screenshot'}).get('src'),
		screenshot_url = screenshot_url[0]
		screenshot = screenshot_url.split('/')[-1]
		archivo_url = contenedor.find('a', attrs={'class': 'sim-download sim-button'}).get('href')
		archivo = archivo_url.split('/')[-1]
		sim = {
			'id': sim_id,
			'titulo': sim_soup.find('h1', attrs={'class': 'simulation-main-title'}).contents[0],
			'descripcion': contenedor.find('span', attrs={'itemprop': 'description about'}).contents[0],
			'screenshot': screenshot,
			'archivo': archivo,
			'categorias': []
		}
		simulaciones.append(sim)
		
		# Imagen
		imgData = urllib2.urlopen("%s://%s%s" % (PROTOCOL, HOST, screenshot_url)).read()
		output = open('data/screenshots/' + screenshot, 'wb')
		output.write(imgData)
		output.close()
		
		# Jar
		jarData = urllib2.urlopen("%s://%s%s" % (PROTOCOL, HOST, archivo_url)).read()
		out = open('data/simulaciones/' + archivo, 'wb')
		out.write(jarData)
		out.close()

print "Total %d simulaciones" % (cnt)
 
#with open ('simulaciones.json', 'wb') as sims_file:
#	json.dump(simulaciones, sims_file, indent=4)

# http://stackoverflow.com/a/14870531
# http://docs.python.org/2/library/json.html#basic-usage
import io
with io.open('simulaciones.py', 'w', encoding='utf-8') as f:
	f.write(unicode("# -*- encoding: utf-8 -*-\n\n"))
	f.write(unicode("simulaciones = "))
	f.write(unicode(json.dumps(simulaciones, ensure_ascii=False, indent=4)))

