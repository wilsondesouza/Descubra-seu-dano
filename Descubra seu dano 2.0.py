# Programa feito com a intenção de calcular e  descobrir o dano causado por cada personagem de Don't Starve Together

# Feito por Wilson Júnior.
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk

# Espaço dos Dicionários #
weapon = {
    'Spear': 34, 'Tentacle Spear': 51, 'Ham Bat': 59.5, 'Dart': 100, 'Boomerang': 27.2, 'Tail': 27.2, 'Morning Star': 43.35, 
    'Battle Spear': 42.5, 'Slingshot': (17.0,34.0,51.0), 'Dark Sword': 68
    }
multiplicador = {
    'Wendy': 0.75, 'Wes': 0.75, 'Wigfrid': 1.25, 'Wolfgang': (1.00, 2.00), 'Wilson': 1.00, 'Willow': 1.00, 'Wx-78': 1.00, 
    'Wickerbottom': 1.00, 'Woodie': 1.00, 'Maxwell': 1.00, 'Webber': 1.00, 'Winona': 1.00, 'Warly': 1.00, 'Wortox': 1.00, 
    'Wurt': 1.00, 'Walter': 1.00, 'Wanda': 1.00
    }
chefes = {
    'Ancient Guardian' : 2500, 'Antlion' : 6000, 'Bearger' : 6000, 'Bee Queen' : 22500, 'Celestial Champion' : (10000, 13000, 14000), 
    'Crab King' : (20000, 23000, 32000, 47000, 68000, 95000), 'Deerclops' : 4000, 'Dragonfly' : 2750, 'Eye of Terror' : (5000, 10000), 
    'Grand Forge Boarrior' : 34000, 'Infernal Swineclops' : 42500, 'Klaus' : (10000, 5000), 'Klaus Enraged' : (27440, 13720), 
    'Lord of the Fruit Flies' : 1500, 'Malbatross' : 5000, 'Moose' : 6000, 'Reanimated Skeleton' : (4000, 4000, 16000), 
    'Spider Queen' : 2500, 'Toadstool' : (52500, 99999), 'Treeguard' : (2100, 3000, 3750), 'Shadow Pieces' : (900, 2700, 8100, 800, 2500, 7500, 1000, 4000, 10000)
    }
# Espaço dos Dicionários #

# Confguração da Interface #
gui = Tk()  
bg = PhotoImage(file = "dst2.png")
bgImg= Label(gui, i=bg)
bgImg.pack()
gui.geometry('800x600')  
gui.title('Calculadora de Dano - DST')
p1 = PhotoImage(file='media/imgs/reward.png')
gui.iconphoto(False, p1)
gui.resizable(0,0)
style = Style()
style.configure("Custom.TButton", foreground = 'black', background = 'black', font= "Verdana 10 underline")
# Confguração da Interface #

class Calculadora():
    Label(gui, text = '"Jogatina dos Putos" apresenta...').pack()
    Label(gui, text ='Calculadora de Dano - Dont Starve Together').pack()

    def __init__(self,gui):
        self.gui = gui
        self.personagem_jogado = ""
        self.arma_usada = ""
        self.municao = ""
        self.dano_personagem = 1
        self.dano_arma = 1

    def personagem(self):
        self.personagem_jogado = charEntry.get() 
        if self.personagem_jogado in multiplicador:
            desc2 = Label(self.gui, text = f'Sério que você escolheu {self.personagem_jogado}? Espero que saiba o que está fazendo.').pack()
            if self.personagem_jogado == 'Wolfgang':
                Label(self.gui, text = 'O dia tem que tá pago pro Wolfão aumentar seu dano').pack()
            elif self.personagem_jogado == 'Wx-78':
                Label(self.gui, text = 'O dano do robozinho vai ser o mesmo com ou sem o chip de Eletricidade').pack()

    def arma(self):
        self.arma_usada = weaponEntry.get()
        if self.arma_usada in weapon:
                Label(self.gui, text = f'Logo a {self.arma_usada}? Tinha arma melhor não?').pack()
        if self.arma_usada == 'Battle Spear' and self.personagem_jogado == 'Wigfrid':
                Label(self.gui, text = "All the wörlds a stage. För me!").pack()
        elif self.arma_usada == 'Dark Sword' and self.personagem_jogado == 'Maxwell':
                Label(self.gui, text = "Freedom suits me.").pack()
        elif self.arma_usada == 'Ham Bat' and self.personagem_jogado == 'Wolfgang':
                Label(self.gui, text = "I am mighty! No one is mightier!").pack()
        elif self.arma_usada == 'Slingshot':
            if self.personagem_jogado != 'Walter':
                Label(self.gui, text=f'Peraí.....{self.personagem_jogado} não consegue equipar a {self.arma_usada}. Só o Waltinho consegue usar ela').pack()
            else:
                Label(self.gui, text="A Pinetree Pioneer is always prepared!").pack()
                self.municao = ammoEntry.get()

    def dano(self):
        dano_personagem = multiplicador.get(self.personagem_jogado, 1)
        dano_arma = weapon.get(self.arma_usada, 1)
    
        if self.arma_usada == 'Slingshot':
            if self.municao == 'Pedra':
                dano_arma = weapon['Slingshot'][0]
            elif self.municao == 'Ouro':
                dano_arma = weapon['Slingshot'][1]
            elif self.municao == 'Mármore':
                dano_arma = weapon['Slingshot'][2]
            
        if isinstance(dano_arma, tuple):
            dano_arma = dano_arma[2]  # Seleciona o primeiro valor da tupla
        
        dano_base = dano_personagem * dano_arma
        Label(gui, text=f"Dano: {dano_base}").place(x=400, y=400)



def limparTela():
    Label.config(text = '')


for num,button_name in enumerate(multiplicador):
    button = Button(gui)
    photo = PhotoImage(file="dst2.png".format(button_name))
    button.config(image=photo)
    button.pack()

# Lista dinâmica de Botões # 
charString = StringVar()
charOptions = OptionMenu( gui, charString, *multiplicador )
charOptions.pack()
for j in range(17):
    Button(gui, text=j)
    Button.pack()
charString.set( "Personagens" )



weaponString = StringVar()
weaponOptions = OptionMenu( gui, weaponString, *weapon )
weaponOptions.pack()
for j in range(6):
    Button(gui, text=j)
    Button.pack()
weaponString.set( "Armas" )
# Lista dinâmica de Botões # 
  
# Interface #
calculadora = Calculadora(gui)
# drop = OptionMenu( gui , clicked , *personagens )
# drop.pack()
charEntry =  Entry(gui, width=60)
charEntry.pack()

charButton = Button( gui , text = "Escolher personagem" , command = calculadora.personagem, style= "Custom.TButton" ).pack()
# drop2 = OptionMenu( gui , clicked2 , *armas )
# drop2.pack()
weaponEntry = Entry(gui, width=60)
weaponEntry.pack()

weaponButton = Button( gui , text = "Escolher arma" , command = calculadora.arma, style= "Custom.TButton" ).pack()
# drop3 = OptionMenu( gui , clicked3 , *ammo )
# drop3.pack()
ammoEntry = Entry(gui, width=60)
ammoEntry.pack()

ammoButton = Button( gui , text = "Escolher munição", style= "Custom.TButton" ).pack()
mathButton = Button( gui , text = "Fazer cálculo", command = calculadora.dano, style= "Custom.TButton").pack()
resetButton = Button( gui , text = "Resetar", command = limparTela, style= "Custom.TButton").pack()
# Interface #

gui.mainloop()