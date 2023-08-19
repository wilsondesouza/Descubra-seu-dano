import customtkinter as ctk
from PIL import Image, ImageTk
import Dicionários

gui = ctk.CTk() 
ctk.set_appearance_mode("dark")
gui.geometry('1260x600')  
gui.title('Calculadora de Dano - DST')

class Calculadora():
    def __init__(self):
            self.personagem_jogado= ""
            self.arma_usada= ""
            self.dano_personagem = 1
            self.dano_arma = 1
            self.buff = 1

    def personagem(self, value):
        print("Botão de personagem pressionado:", value)
        self.personagem_jogado = value

    def arma(self,value):
        print("Botão de arma pressionado:", value)
        self.arma_usada = value

    def dano(self):
        for key in Dicionários.multiplicador.keys():
            if key.startswith(self.personagem_jogado):
                self.dano_personagem = (Dicionários.multiplicador[key])  
        for key in Dicionários.weapon.keys():
            if key.startswith(self.arma_usada):
                self.dano_arma = (Dicionários.weapon[key])
        self.dano_base = self.dano_personagem * self.dano_arma
calculadora = Calculadora()

def create_buttons(frame, data, command_function, image_size, buttons_per_row):
    coluna = 0
    linha = 0

    for i in data:
        j = Image.open(i["image_path"])
        resizeJ = j.resize(image_size)
        finalJ = ImageTk.PhotoImage(resizeJ)
        btn = ctk.CTkButton(frame, text="", command=lambda v=i["value"]: command_function(v), image=finalJ, bg_color="transparent", fg_color="transparent")
        btn.grid(row=linha, column=coluna % buttons_per_row, columnspan=1)
        
        coluna += 1
        if coluna % buttons_per_row == 0:  # Passar para a próxima linha após a quantidade desejada de botões por linha
            linha += 1

frame_personagens = ctk.CTkFrame(gui)
frame_personagens.grid(row=1, column=0)

frame_armas = ctk.CTkFrame(gui)
frame_armas.grid(row=2, column=0)

retorno = ctk.CTkLabel(gui, text=f'{calculadora.self.dano_base}')

multiplicador_data = [{"value": i, "image_path": f"DescubraSeuDano/media/chars/{i}.png"} for i in Dicionários.multiplicador]
weapon_data = [{"value": i, "image_path": f"DescubraSeuDano/media/weapon/{i}.png"} for i in Dicionários.weapon]

create_buttons(frame_personagens, multiplicador_data, calculadora.personagem, (100, 100), 9)
create_buttons(frame_armas, weapon_data, calculadora.arma, (54, 54), 5)

gui.mainloop()
