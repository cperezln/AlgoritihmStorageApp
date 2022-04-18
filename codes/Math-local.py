#Autor##Admin
##GDC
'''

    Algorithm to find the greatest common divisor betweent two numbers
'''
def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x
#Autor##Admin
##Cribe
'''
    
    Eratostene's cribe, to check the primes between 1 and N
'''
def cribe(n):
	primes = []
	isPrime = [1 for i in range(n)]
	isPrime[0] = isPrime[1] = 0

	for i in range(n):
		if isPrime[i]:
			primes.append(i)
			h = 2
			while i*h < n:
				isPrime[i*h] = 0
				h += 1

	return primes, isPrime
#Autor##Juan Antonio
##1
##public
'''
AAAAA
AA
A
A
'''
from appAlgoritmos import Algoritmos
from tkinter import ttk
from tkinter import *
from sqlalchemy import create_engine
if __name__ == '__main__':

    root =Tk() #ventana principal
    app = Algoritmos(root)
    root.mainloop()#Con esto mantenemos la
    # ventana si no se cerraria tras un milisegundo.Esta accion abre un hilo
#Autor##Juan Antonio
##2
##private
'''
BB

BB
'''
from appAlgoritmos import Algoritmos
from tkinter import ttk
from tkinter import *
from sqlalchemy import create_engine
if __name__ == '__main__':

    root =Tk() #ventana principal
    app = Algoritmos(root)
    root.mainloop()#Con esto mantenemos la
    # ventana si no se cerraria tras un milisegundo.Esta accion abre un hilo
