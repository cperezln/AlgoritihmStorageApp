
"""
AUTOR : JUAN ANTONIO GORDILLO
"""

from appAlgoritmos import Algoritmos
from tkinter import *
if __name__ == '__main__':

    root =Tk() #ventana principal
    app = Algoritmos(root)
    root.mainloop()#Con esto mantenemos la
    # ventana si no se cerraria tras un milisegundo.Esta accion abre un hilo
