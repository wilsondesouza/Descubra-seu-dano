# Programa feito com a intenção de calcular e  descobrir o dano causado por cada personagem de Don't Starve Together

# Feito por Wilson Júnior.
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
import Dicionário


# Confguração da Interface #
gui = Tk()  
bg = PhotoImage(file = "media/imgs/dst2.png")
icon = PhotoImage(file = "media/imgs/dst.png")
bgImg= Label(gui, i=bg)
bgImg.pack()
gui.geometry('982x505')  
gui.title('Calculadora de Dano - DST')
gui.iconphoto(False, icon)
gui.resizable(0,0)

# Confguração da Interface #



gui.mainloop()