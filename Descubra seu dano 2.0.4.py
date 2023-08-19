import customtkinter as ctk
from PIL import Image, ImageTk
import Dicionários

# Confguração da Interface #
gui = ctk.CTk() 
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")
gui.geometry('1260x600')  
gui.title('Calculadora de Dano - DST')
# Confguração da Interface #

# Classes e Funções "Background" #
class Calculadora():
    def __init__(self):
        self.personagem_jogado= ""
        self.arma_usada= ""
        self.dano_personagem = 1
        self.dano_arma = 1
        #self.buff = 1
        self.dano_base = 1  

    def personagem(self, value):
        print("Personagem escolhido:", value)
        self.personagem_jogado = value

    def arma(self,value):
        print("Arma escolhida:", value)
        self.arma_usada = value

    def dano(self):
        for key in Dicionários.multiplicadorApp.keys():
            if key.startswith(self.personagem_jogado):
                self.dano_personagem = (Dicionários.multiplicadorApp[key])  
        for key in Dicionários.weaponApp.keys():
            if key.startswith(self.arma_usada):
                self.dano_arma = (Dicionários.weaponApp[key])
        self.dano_base = self.dano_personagem * self.dano_arma
        print("Dano base:", self.dano_base)
# Classes e Funções "Background" #

# Instâncias da classe e objetos #
calculadora = Calculadora()
# Instâncias da classe e objetos #

# Funções Visuais #
def atualizarLabel():
    calculo.configure(text=f'Dano Base: {calculadora.dano_base}')

def criarBotoes(frame, data, command_function, image_size, buttons_per_row):
    coluna = 0
    linha = 0
    for i in data:
        img = Image.open(i["image_path"])
        resizeImg = img.resize(image_size)
        finalImg = ImageTk.PhotoImage(resizeImg)
        btn = ctk.CTkButton(frame, text="", command=lambda v=i["value"]: command_function(v), image=finalImg, bg_color="transparent", fg_color="transparent")
        btn.grid(row=linha, column=coluna % buttons_per_row, columnspan=1)
        
        coluna += 1
        if coluna % buttons_per_row == 0:  # Passar para a próxima linha após a quantidade desejada de botões por linha
            linha += 1
# Funções Visuais #

# Interface #
personagens = ctk.CTkLabel(gui, text="Personagens")
personagens.grid(row=1, column=0)
frame_personagens = ctk.CTkFrame(gui)
frame_personagens.grid(row=2, column=0)

armas = ctk.CTkLabel(gui, text="Armas")
armas.grid(row=3, column=0)
frame_armas = ctk.CTkFrame(gui)
frame_armas.grid(row=4, column=0)

calculo = ctk.CTkLabel(gui, text=f'Dano Base: {calculadora.dano_base}', text_color="green")
calculo.grid(row=6, column=0)  
botaoCalculo = ctk.CTkButton(gui, text="Calcular Dano", fg_color="darkblue", hover_color=("#DB3E39", "#821D1A"), command=lambda: (calculadora.dano(), atualizarLabel())) # type: ignore
botaoCalculo.grid(row=5, column=0, pady=10)  

multiplicador_data = [{"value": i, "image_path": f"DescubraSeuDano/media/chars/{i}.png"} for i in Dicionários.multiplicadorApp]
weapon_data = [{"value": i, "image_path": f"DescubraSeuDano/media/weapon/{i}.png"} for i in Dicionários.weaponApp]

criarBotoes(frame_personagens, multiplicador_data, calculadora.personagem, (100, 100), 9)
criarBotoes(frame_armas, weapon_data, calculadora.arma, (54, 54), 5)
# Interface #

gui.mainloop()
