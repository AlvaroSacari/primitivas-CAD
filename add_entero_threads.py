#encoding:utf-8
__author__ = 'alvaro'

#from add_entero import add_entero

import thread
import time
from turtle import *
import random
from pixel import ejes, pintar

def intercambiar_puntos(a, b):
	aux = a
	a = b
	b = aux
	return a, b

def Salir():
	salir = raw_input('\n¿continuar graficando? (s,n) : ')
	if salir == 's':
		main()
	else:
		print '\nGracias ..'

def main():
	print('Bienvenidos al metodo ADD entero para el trazado de líneas')

	#PRIMER CASO
	#add_entero(-50, -50, 30, 24)
	#SEGUDO CASO
	#add_entero(2,8,4,12)
	#TERCER CASO
	#add_entero(2,7,-5,11)
	#CUARTO CASO
	#add_entero(20,-8,2,15)

	#thread.start_new_thread(add_entero, (2,8,4,12,))

	print('\n Ingrese los puntos (xi,yi) y (xf, yf) de la recta')
	xi = int(raw_input('\n\txi : '))
	yi = int(raw_input('\n\tyi : '))
	xf = int(raw_input('\n\txf : '))
	yf = int(raw_input('\n\tyf : '))

	if yi > yf:
		xi, xf = intercambiar_puntos(xi, xf)
		yi, yf = intercambiar_puntos(yi, yf)
	#hilo1(-50, -50, 30, 24)
	# Valores iniciales del hilo 1
	"""
	xi1 = -50
	yi1 = -50
	xf1 = 30
	yf1 = 24
	"""
	xi1 = xi
	yi1 = yi
	xf1 = (xi + xf) / 2
	yf1 = (yi + yf) / 2

	Dx1 = xf1 - xi1
	Dy1 = yf1 - yi1
	m1 = float(Dy1) / float(Dx1)

	error1 = 0

	pintar(xi1, yi1)

	xant1 = xi1
	yant1 = yi1

	###########################################
	# Valores iniciales del hilo 2 (20,-8,2,15)
	xi2 = xf1
	yi2 = yf1
	xf2 = xf
	yf2 = yf

	Dx2 = xf2 - xi2
	Dy2 = yf2 - yi2
	m2 = float(Dy2) / float(Dx2)

	error2 = 0

	pintar(xi2, yi2)

	xant2 = xi2
	yant2 = yi2

	while xant1 != xf1 or xant2 != xf2:
		x = random.randrange(0, 2)
		print('Hilo {}'.format(x+1))
		#time.sleep(1)
		if x == 0 and xant1 != xf1:

			#PRIMER CASO
			if 0 < m1 < 1 and (Dx1 > 0 and Dy1 > 0):
				if error1 < 0:
					xsig1 = xant1 + 1
					ysig1 = yant1
					error1 = error1 + Dy1
				else:
					xsig1 = xant1 + 1
					ysig1 = yant1 + 1
					error1 = error1 + (Dy1 - Dx1)
				pintar(xsig1, ysig1)
				xant1 = xsig1
				yant1 = ysig1

			#SEGUNDO CASO
			elif m1 > 1 and (Dx1 >= 0 and Dy1 >= 0):
				if error1 < 0:
					xsig1 = xant1 + 1
					ysig1 = yant1 + 1
					error1 = error1 + (Dy1 - Dx1)
				else:
					xsig1 = xant1
					ysig1 = yant1 + 1
					error1 = error1 - Dx1
				pintar(xsig1, ysig1)
				xant1 = xsig1
				yant1 = ysig1

			#TERCER CASO
			elif -1 < m1 < 0 and (Dx1 < 0 and Dy1 >= 0):
				if error1 < 0:
					xsig1 = xant1 - 1
					ysig1 = yant1
					error1 = error1 + Dy1
				else:
					xsig1 = xant1 - 1
					ysig1 = yant1 + 1
					error1 = error1 + (Dx1 + Dy1)
				pintar(xsig1, ysig1)
				xant1 = xsig1
				yant1 = ysig1

			#CUARTO CASO
			elif m1 < -1 and (Dx1 < 0 and Dy1 >= 0):
				if error1 < 0:
					xsig1 = xant1 - 1
					ysig1 = yant1 + 1
					error1 = error1 + (Dx1 + Dy1)
				else:
					xsig1 = xant1
					ysig1 = yant1 + 1
					error1 = error1 + Dx1
				pintar(xsig1, ysig1)
				xant1 = xsig1
				yant1 = ysig1

		# hilo 2
		elif x == 1 and xant2 != xf2:

			#PRIMER CASO
			if 0 < m2 < 1 and (Dx2 > 0 and Dy2 > 0):
				if error2 < 0:
					xsig2 = xant2 + 1
					ysig2 = yant2
					error2 = error2 + Dy2
				else:
					xsig2 = xant2 + 1
					ysig2 = yant2 + 1
					error2 = error2 + (Dy2 - Dx2)
				pintar(xsig2, ysig2)
				xant2 = xsig2
				yant2 = ysig2

			#SEGUNDO CASO
			elif m2 > 1 and (Dx2 >= 0 and Dy2 >= 0):
				if error2 < 0:
					xsig2 = xant2 + 1
					ysig2 = yant2 + 1
					error2 = error2 + (Dy2 - Dx2)
				else:
					xsig2 = xant2
					ysig2 = yant2 + 1
					error2 = error2 - Dx2
				pintar(xsig2, ysig2)
				xant2 = xsig2
				yant2 = ysig2

			#TERCER CASO
			elif -1 < m2 < 0 and (Dx2 < 0 and Dy2 >= 0):
				if error2 < 0:
					xsig2 = xant2 - 1
					ysig2 = yant2
					error2 = error2 + Dy2
				else:
					xsig2 = xant2 - 1
					ysig2 = yant2 + 1
					error2 = error2 + (Dx2 + Dy2)
				pintar(xsig2, ysig2)
				xant2 = xsig2
				yant2 = ysig2

			#CUARTO CASO
			elif m2 < -1 and (Dx2 < 0 and Dy2 >= 0):
				if error2 < 0:
					xsig2 = xant2 - 1
					ysig2 = yant2 + 1
					error2 = error2 + (Dx2 + Dy2)
				else:
					xsig2 = xant2
					ysig2 = yant2 + 1
					error2 = error2 + Dx2
				pintar(xsig2, ysig2)
				xant2 = xsig2
				yant2 = ysig2
	Salir()


ejes()
main()