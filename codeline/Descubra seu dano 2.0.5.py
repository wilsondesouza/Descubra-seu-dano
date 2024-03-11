import customtkinter as ctk
import tkinter
from PIL import Image, ImageTk
import Dicionário

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
        self.boss_usuario = ""
        self.dano_personagem = 1
        self.dano_arma = 1
        self.buff = 1
        self.dano_base = 1  
        self.hit_boss= 1

    def personagem(self, value):
        print("Personagem escolhido:", value)
        self.personagem_jogado = value

    def arma(self,value):
        print("Arma escolhida:", value)
        self.arma_usada = value

    def buffs(self, value):
        print("Buff escolhido:", value)
        self.buff = value
        if self.buff == 'Volt':
            print(f'Volt Goat Chaud-Froid Buff (Mob "Wet"): {self.buff:.2f}')              
        elif self.buff == "Ambos":
            print(f'Dois Buffs (Mob "Wet"): {self.buff:.2f}')  
        elif self.buff == 'Chili':
            print(f'Chili Flakes Buff: {self.buff:.2f}.') 

    def boss(self,value):
        print("Boss escolhido:", value)
        self.boss_usuario = float(value) / self.buff

    def dano(self):
        for key in Dicionário.multiplicadorApp.keys():
            if key.startswith(self.personagem_jogado):
                self.dano_personagem = (Dicionário.multiplicadorApp[key])  
        for key in Dicionário.weaponApp.keys():
            if key.startswith(self.arma_usada):
                self.dano_arma = (Dicionário.weaponApp[key])
        self.dano_base = self.dano_personagem * self.dano_arma
        print("Dano base:", self.dano_base)
# Classes e Funções "Background" #

# Instâncias da classe e objetos #
calculadora = Calculadora()
# Instâncias da classe e objetos #

# Funções Visuais #
def buffs_function(value):
    calculadora.buffs(value)
    atualizarLabel()

def atualizarLabel():
    calculoBase.configure(text=f'Dano Base: {calculadora.dano_base:.2f}')
    calculoBuff.configure(text=f'Dano com Buff: {calculadora.buff:.2f}')
    calculoBoss.configure(text=f'Hit to Kill: {calculadora.hit_boss:.2f}')

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
bosses = ctk.CTkLabel(gui, text="Bosses")
bosses.grid(row=1, column=0)
frame_bosses = ctk.CTkFrame(gui)
frame_bosses.grid(row=2, column=0)

personagens = ctk.CTkLabel(gui, text="Personagens")
personagens.grid(row=3, column=0)
frame_personagens = ctk.CTkFrame(gui)
frame_personagens.grid(row=4, column=0)

armas = ctk.CTkLabel(gui, text="Armas")
armas.grid(row=5, column=0)
frame_armas = ctk.CTkFrame(gui)
frame_armas.grid(row=6, column=0)

buffs = ctk.CTkLabel(gui, text="Buffs")
buffs.grid(row=8, column=0)
frame_buffs = ctk.CTkFrame(gui)
frame_buffs.grid(row=9, column=0)

calculoBase = ctk.CTkLabel(gui, text=f'Dano Base: ', text_color="green")
calculoBase.place(relx=0.335, rely=0.95)
botaoCalculoBase = ctk.CTkButton(gui, text="Calcular Dano", fg_color="darkblue", hover_color=("#DB3E39", "#821D1A"), command=lambda: (calculadora.dano(), atualizarLabel())) #type: ignore
botaoCalculoBase.place(relx=0.335, rely=0.9)
calculoBuff = ctk.CTkLabel(gui, text=f'Dano com Buff: ', text_color="green")
calculoBuff.place(relx=0.435, rely=0.95) 
botaoCalculoBuff = ctk.CTkButton(gui, text="Calcular Buff", fg_color="darkblue", hover_color=("#DB3E39", "#821D1A"), command=lambda: (calculadora.buffs(), atualizarLabel())) # type: ignore
botaoCalculoBuff.place(relx=0.435, rely=0.9)
calculoBoss = ctk.CTkLabel(gui, text=f'Hit to Kill: ', text_color="green")
calculoBoss.place(relx=0.535, rely=0.95)
botaoCalculoBoss = ctk.CTkButton(gui, text="Calcular Boss", fg_color="darkblue", hover_color=("#DB3E39", "#821D1A"), command=lambda: (calculadora.boss(), atualizarLabel())) # type: ignore
botaoCalculoBoss.place(relx=0.535, rely=0.9)

chefes_data = [{"value": i, "image_path": f"DescubraSeuDano/media/bosses/{i}.png"} for i in Dicionário.chefesApp]
multiplicador_data = [{"value": i, "image_path": f"DescubraSeuDano/media/chars/{i}.png"} for i in Dicionário.multiplicadorApp]
weapon_data = [{"value": i, "image_path": f"DescubraSeuDano/media/weapon/{i}.png"} for i in Dicionário.weaponApp]
buffs_data = [{"value": i, "image_path": f"DescubraSeuDano/media/buffs/{i}.png"} for i in Dicionário.buffsApp]


criarBotoes(frame_bosses, chefes_data, calculadora.boss, (100, 100), 11)
criarBotoes(frame_personagens, multiplicador_data, calculadora.personagem, (100, 100), 9)
criarBotoes(frame_armas, weapon_data, calculadora.arma, (54, 54), 5)
criarBotoes(frame_buffs, buffs_data, buffs_function, (54, 54), 5)
# Interface #

gui.mainloop()
