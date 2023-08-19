import customtkinter as ctk
from PIL import Image, ImageTk
import Dicionários

gui = ctk.CTk() 
ctk.set_appearance_mode("dark")
gui.geometry('1260x600')  
gui.title('Calculadora de Dano - DST')



def personagem(value):
    print("Botão pressionado:", value)
    personagem_jogado = value

def arma(value):
    print("Botão pressionado:", value)
    arma_usada = value


def multiplicador():
    botaoPorLinha = 9  
    coluna = 0
    linha = 1

    for i in Dicionários.multiplicador:
        j = Image.open(f"DescubraSeuDano/media/chars/{i}.png")
        resizeJ = j.resize((100, 100))
        finalJ = ImageTk.PhotoImage(resizeJ)
        btn = ctk.CTkButton(gui, text="", command=lambda v=i: personagem(v), image=finalJ, bg_color="white")
        btn.grid(row=linha, column=coluna % botaoPorLinha, columnspan=1)
        
        coluna += 1
        if coluna % botaoPorLinha == 0:  # Passar para a próxima linha após a quantidade desejada de botões por linha
            linha += 1

def weapon():
    botaoPorLinha = 5 
    coluna = 0
    linha = 1

    for i in Dicionários.weapon:
        j = Image.open(f"DescubraSeuDano/media/weapon/{i}.png")
        resizeJ = j.resize((54, 54))
        finalJ = ImageTk.PhotoImage(resizeJ)
        btn = ctk.CTkButton(gui, text="", command=lambda v=i: arma(v), image=finalJ, bg_color="white")
        btn.grid(row=linha, column=coluna % botaoPorLinha, columnspan=1)
        
        coluna += 1
        if coluna % botaoPorLinha == 0:  # Passar para a próxima linha após a quantidade desejada de botões por linha
            linha += 1
multiplicador()
weapon()

gui.mainloop()