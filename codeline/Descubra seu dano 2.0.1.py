# Programa feito com a intenção de calcular e  descobrir o dano causado por cada personagem de Don't Starve Together

# Feito por Wilson Júnior.
import customtkinter as ctk
from PIL import Image, ImageTk
import Dicionário




# Confguração da Interface #
gui = ctk. CTk()  
ctk.set_appearance_mode("dark")
gui.geometry('980x500')  
gui.title('Calculadora de Dano - DST')


# Confguração da Interface #


def personagem():
    text = button.cget("text")
    print (text)

for i in range(9):
    j = Image.open (f"DescubraSeuDano/media/chars/{i}.png")
    resizeJ = j.resize((150,100))
    finalJ = ImageTk.PhotoImage (resizeJ)
    button = ctk.CTkButton(gui, command=personagem, image= finalJ, text=f"{i}")
    button.grid(row=3, column=i, columnspan=1)

    

gui.mainloop()