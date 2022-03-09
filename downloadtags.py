from bs4 import *
import os
from urllib.request import Request, urlopen
import shutil

with open("file.txt") as fp:
    soup = BeautifulSoup(fp, 'lxml')

links = soup.findAll('a')

for i, element in enumerate(links):
	liga=element["href"]
	print(liga)
	nombre_local_imagen=liga.split('/')
	print(nombre_local_imagen[-1])
	try:
		req = Request(liga, headers={'User-Agent': 'Mozilla/5.0'})
		webpage = urlopen(req)
		with open("uno/"+nombre_local_imagen[-1], 'wb') as salida:
			shutil.copyfileobj(webpage, salida)
			print(salida)
	except:
		print("not found")
