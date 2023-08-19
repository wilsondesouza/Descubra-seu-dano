import customtkinter as ctk
from PIL import Image, ImageTk
import Dicionários
import webbrowser


# Feito por Wilson Júnior. GitHub: https://github.com/wilsondesouza #

# Confguração da Interface #
gui = ctk.CTk() 
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")
gui.geometry('1600x900')  
gui.title('Calculadora de Dano - DST')
w, h = gui.winfo_screenwidth(), gui.winfo_screenheight()
gui.geometry("%dx%d-8-0" % (w, h))
icon = Image.open("media/imgs/dst.png")
finalIcon = ImageTk.PhotoImage(icon)
gui.iconphoto(False, finalIcon)
gui.iconbitmap("media/imgs/dst.ico")

# Confguração da Interface #

# Classes e Funções "Backend" #
class Calculadora():
    def __init__(self):
        self.personagem_jogado= ""
        self.arma_usada= ""
        self.boss_usuario = ""
        self.dano_personagem = 1
        self.dano_arma = 1
        self.buff = 1
        self.dano_buff = 1
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
        for key in Dicionários.buffsApp.keys():
            if key.startswith(self.buff):
                self.dano_buff = (Dicionários.buffsApp[key])  
        if self.buff == 'Volt':
            print(f'Volt Goat Chaud-Froid Buff (Mob "Wet"): {self.dano_base * self.dano_buff:.2f}')              
        elif self.buff == "Ambos":
            print(f'Dois Buffs (Mob "Wet"): {self.dano_base * self.dano_buff:.2f}')  
        elif self.buff == 'Chili':
            print(f'Chili Flakes Buff: {self.dano_base * self.dano_buff:.2f}.') 
        self.dano_buff = self.dano_base * self.dano_buff

    def bosses(self,value):
        self.boss_usuario = value 
        for key in Dicionários.chefesApp.keys():
                if key.startswith(self.boss_usuario):
                    print("Boss escolhido:", self.boss_usuario)
                    self.hit_boss = (Dicionários.chefesApp[key])
                    self.hit_boss = self.hit_boss / self.dano_buff
                    print (f'Você precisará acertar {self.hit_boss:.2f} para derrotar {self.boss_usuario}')

    def dano(self):
        if not self.personagem_jogado or not self.arma_usada:
            print("Escolha um personagem e uma arma antes de calcular o dano.")
            return
        for key in Dicionários.multiplicadorApp.keys():
            if key.startswith(self.personagem_jogado):
                self.dano_personagem = (Dicionários.multiplicadorApp[key])  
        for key in Dicionários.weaponApp.keys():
            if key.startswith(self.arma_usada):
                self.dano_arma = (Dicionários.weaponApp[key])
        self.dano_base = self.dano_personagem * self.dano_arma
        print("Dano base:", self.dano_base)
# Classes e Funções "Backend" #

# Instância de classes e objetos #
calculadora = Calculadora()
# Instância de classes e objetos #

# Funções Visuais #
def atualizarLabel():
    calculoBase.configure(text=f'Dano Base: {calculadora.dano_base:.2f}')
    calculoBuff.configure(text=f'Dano com Buff: {calculadora.dano_buff:.2f}')
    calculoBoss.configure(text=f'Hit to Kill: {calculadora.hit_boss:.2f}')

def buffs_function(value):
    calculadora.buffs(value)
    atualizarLabel()

def create_buttons(frame, data, command_function, image_size, buttons_per_row, hover_color):
    coluna = 0
    linha = 0
    for i in data:
        img = Image.open(i["image_path"])
        resizeImg = img.resize(image_size)
        finalImg = ImageTk.PhotoImage(resizeImg)
        btn = ctk.CTkButton(frame, hover_color=hover_color,text="", command=lambda v=i["value"]: command_function(v), image=finalImg,bg_color="transparent", fg_color="transparent", )
        btn.grid(row=linha, column=coluna % buttons_per_row, columnspan=1)
        
        coluna += 1
        if coluna % buttons_per_row == 0:
            linha += 1

def callback():
    webbrowser.open_new_tab("https://github.com/wilsondesouza")
# Funções Visuais #

# Interface Gráfica #
personagens = ctk.CTkLabel(gui, text="Personagens")
personagens.place(relx=0.422, rely=0)
frame_personagens = ctk.CTkFrame(gui)
frame_personagens.place(relx=0.05, rely=0.03)

armas = ctk.CTkLabel(gui, text="Armas")
armas.place(relx=0.90, rely=0)
frame_armas = ctk.CTkFrame(gui)
frame_armas.place(relx=0.865, rely=0.03)

buffs = ctk.CTkLabel(gui, text="Buffs")
buffs.place(relx=0.898, rely=0.69)
frame_buffs = ctk.CTkFrame(gui)
frame_buffs.place(relx=0.865, rely=0.72)

bosses = ctk.CTkLabel(gui, text="Bosses")
bosses.place(relx=0.432, rely=0.275)
frame_bosses = ctk.CTkFrame(gui)
frame_bosses.place(relx=0.08, rely=0.315)

calculoBase = ctk.CTkLabel(gui, font=(None, 16), text='Dano Base:', text_color="green")
calculoBase.place(relx=0.255, rely=0.828)
calculoBuff = ctk.CTkLabel(gui, font=(None, 16), text='Dano com Buff:', text_color="green")
calculoBuff.place(relx=0.395, rely=0.828) 
calculoBoss = ctk.CTkLabel(gui, font=(None, 16), text='Hit to Kill:', text_color="green")
calculoBoss.place(relx=0.535, rely=0.828)

botaoCalculoBase = ctk.CTkButton(gui,text="Calcular Dano", fg_color="darkblue", hover_color="green", command=lambda: (calculadora.dano(), atualizarLabel())) #type: ignore
botaoCalculoBuff = ctk.CTkButton(gui, text="Calcular Buff", fg_color="darkblue", hover_color="green", command=lambda: (buffs_function(calculadora.buff), atualizarLabel())) #type: ignore
botaoCalculoBoss = ctk.CTkButton(gui, text="Calcular Boss", fg_color="darkblue", hover_color=("#DB3E39", "#821D1A"), command=lambda: (calculadora.bosses(calculadora.buff), atualizarLabel())) #type: ignore

botaoCalculoBase.place(relx=0.255, rely=0.8)
botaoCalculoBuff.place(relx=0.395, rely=0.8)
botaoCalculoBoss.place(relx=0.535, rely=0.8)

chefes_data = [{"value": i, "image_path": f"media/bosses/{i}.png"} for i in Dicionários.chefesApp]
multiplicador_data = [{"value": i, "image_path": f"media/chars/{i}.png"} for i in Dicionários.multiplicadorApp]
weapon_data = [{"value": i, "image_path": f"media/weapon/{i}.png"} for i in Dicionários.weaponApp]
buffs_data = [{"value": i, "image_path": f"media/buffs/{i}.png"} for i in Dicionários.buffsApp]


create_buttons(frame_personagens, multiplicador_data, calculadora.personagem, (100, 100), 9, hover_color="darkblue")
create_buttons(frame_armas, weapon_data, calculadora.arma, (50, 50), 1, hover_color="green")
create_buttons(frame_buffs, buffs_data, buffs_function, (50, 50), 1, hover_color="green")
create_buttons(frame_bosses, chefes_data, calculadora.bosses, (130, 130), 8, hover_color="red")
github = Image.open("media/imgs/github.png")

img = Image.open("media/imgs/musica.png")
resizeImg = img.resize((30,30))
finalImg = ImageTk.PhotoImage(resizeImg)
homenagemBotao = ctk. CTkButton(gui, text="Silo viado, cachorro de fogo. Silo de fogo, cachorro viado", font=(None, 16), image=finalImg, bg_color="transparent", fg_color="transparent", state="disabled", width=1, height=10)
homenagemBotao.place(relx=0.02, rely=0.88,)

resizeGitHub = github.resize((30,30))
finalGitHub = ImageTk.PhotoImage(resizeGitHub)
link1 = ctk.CTkButton(gui, text=" ", cursor="hand2",image=finalGitHub, bg_color="transparent", hover=False ,fg_color="transparent", width=1, command=callback)
link1.place(relx=0.785, rely=0.875,)
# Interface Gráfica #

gui.mainloop()
