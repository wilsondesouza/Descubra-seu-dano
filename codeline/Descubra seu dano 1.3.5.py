# Programa feito com a intenção de calcular e  descobrir o dano causado por cada personagem de Don't Starve Together
# Feito por Wilson Júnior.

from time import sleep as s
import Dicionário
import os

# Método construtor #
class Calculadora:
    def __init__(self):
        self.personagem_jogado = ""
        self.arma_usada = ""
        self.municao = ""
        self.dano_personagem = 1
        self.dano_arma = 1
        self.buff = 1
        self.hit_boss = 0

#Funções Genéricas #           
    def try_again(self, item, dictionary):
        choice = input(f"Quer tentar escolher outro(a) {item}? (Sim/Não)\n").strip().title()
        if choice == "Sim":
            self.clear_screen()
            if item == "personagem":
                self.personagem(dictionary)
            else:
                self.arma(dictionary)
        else:
            print("Ok. Obrigado por usar a calculadora de dano!")
            quit()

# Limpar Tela #
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')


# Usuário informará seu personagem, o programa realizará a busca no dicionário "multiplicador" e passará para a próxima parte
    def personagem(self, dicionario):
        print("Personagens disponíveis:")
        for personagem in dicionario.keys():
            s(.5)
            print(personagem)
        self.personagem_jogado = input("\nCom qual personagem você está do capeta jogando?\n").replace(" ", "").title()
        if self.personagem_jogado not in dicionario:
            print("Personagem inválido")
            self.try_again("personagem", Dicionário.multiplicador)
        else:
            s(.5)
            print(f"Personagem escolhido: {self.personagem_jogado}")
            s(1)
            self.clear_screen()

# O usuário informará sua arma, o programa buscará no dicionário "weapon" e passará para a próxima parte
    def arma(self, dicionario):
        print("Armas disponíveis:")
        for arma in dicionario.keys():
            s(.5)
            print(arma)
        self.arma_usada = input("\nQual arma você está usando?\n").strip().title()
        if self.arma_usada not in dicionario:
            print("Arma inválida")
            self.try_again("arma", Dicionário.weapon)
        else:
            s(.5)
            print(f"Arma escolhida: {self.arma_usada}")
            s(1)
            self.clear_screen()

# O programa usará os valores correspondentes às strings informadas pelo usuário para fazer uma simples operação de multiplicação
    def dano(self):
        for key in Dicionário.multiplicador.keys():
            if key.startswith(self.personagem_jogado):
                self.dano_personagem = (Dicionário.multiplicador[key])  
                if self.personagem_jogado == 'Wolfgang':
                    variation = input('Wolfão foi pra academia?"S/N"''\n').replace(' ', '').title()
                    s(1)
                    match variation:
                        case "N":
                            self.dano_personagem = (Dicionário.multiplicador['Wolfgang'][0])
                        case "S":
                            self.dano_personagem = (Dicionário.multiplicador['Wolfgang'][1])
        for key in Dicionário.weapon.keys():
            if key.startswith(self.arma_usada):
                self.dano_arma = (Dicionário.weapon[key])
                if self.arma_usada == 'Slingshot':
                    self.munição = input('Qual munição você usará?("Pedra", "Ouro" ou "Mármore")''\n').replace(' ', '').title()
                    s(1)
                    match self.munição: 
                        case "Pedra":
                            self.dano_arma = (Dicionário.weapon['Slingshot'][0])
                        case 'Ouro':
                            self.dano_arma = (Dicionário.weapon['Slingshot'][1])
                        case 'Mármore':
                            self.dano_arma = (Dicionário.weapon['Slingshot'][2])
        self.dano_base = self.dano_personagem * self.dano_arma
        s(1)
        #progress bar
        print (f'Seu dano base é {self.dano_base}.')
    
# Após essa operação, finalmente o programa será capaz de apontar quanto de dano o personagem causará com um ou mais buffs.
    def buffs(self):
        print('Existem dois buffs de comida que podem complementar o dano causado: Volt Goat Chaud-Froid e Chili Flakes')
        s(1)
        pergunta_buff = input('Qual buff você quer ver aplicado sobre o seu dano? ("volt", "chili" ou "ambos")?''\n').replace(' ', '').title()
        #progress bar
        if pergunta_buff == 'Volt' or pergunta_buff == 'Ambos':
            s(1)
            variação = input('O monstro estará seco ou "Wet"?"(1,2)"''\n').replace(' ', '')
            s(1)          
            match variação:   
                case '1':
                    if pergunta_buff == 'Volt':
                        buff = self.dano_base * 1.5
                        self.buff = buff
                        print(f'Seu dano com Volt Goat Chaud-Froid é {self.buff:.2f}')
                    else:
                        buff = (self.dano_base * 1.5) * 1.2
                        self.buff = buff
                        print(f'Seu dano com os dois buffs será de {self.buff:.2f}')                
                case '2':
                    if pergunta_buff == "Ambos":
                        buff = self.dano_base * 3.0
                        self.buff = buff
                        print(f'Seu dano com os dois buffs será de {self.buff:.2f} se o mob estiver "Wet"')  
                    else:
                        buff = self.dano_base * 2.5
                        self.buff = buff
                        print(f'Seu dano com a Volt Goat Chaud-Froid  se o mob estiver "Wet" será {self.buff:.2f}')                         
            s(1)
        elif pergunta_buff == 'Chili':
            buff = self.dano_base * 1.2
            self.buff = buff
            s(1)
            print(f'Seu dano com o buff da Chili Flakes passa a ser de {self.buff:.2f}.') 
        s(1)
        tentativa = input('Quer testar outro buff?''\n').replace(' ', '').title()
        if tentativa == "Sim":
                s(1) 
                print('Entendido')
                self.buffs()
        s(1)

# Nesta função, o usuário poderá descobrir quantos hits eles precisará acertar para derrotar cada um dos boss monster do game
    def bosses(self):
        boss_usuario = input('Qual boss você irá enfrentar?''\n').strip().title()
        while boss_usuario not in Dicionário.chefes:
            s(1)
            tentativa_boss = input('Esse boss não existe. Quer tentar de novo?''\n').strip().title()
            if tentativa_boss != 'Sim':
                self.try_again("boss", Dicionário.chefes)
            boss_usuario = input('Qual boss você irá enfrentar?''\n').strip().title()

        s(1)
        if boss_usuario == "Celestial Champion":
            print(f'{boss_usuario}? Impossível! Desista de seus sonhos e sucumba')
        else:
            print (f'{boss_usuario}? Boa sorte!')

        boss_key = boss_usuario if boss_usuario != 'Shadow Pieces' else 'Shadow Pieces'
        boss_info = Dicionário.chefes[boss_key]
        fase_boss = self.fase_boss(boss_usuario)

        self.hit_boss = self.dano_boss(boss_info, fase_boss, boss_usuario)
        self.print_dano_boss(boss_usuario, self.hit_boss)

        tentativa = input('Quer escolher outro boss?''\n').replace(' ', '').title()   
        match tentativa:
            case "Sim":
                self.bosses()
            case _:  
                self.reiniciar()

    def fase_boss(self, boss_usuario):
        if boss_usuario == 'Crab King':
            variação = input(f'Qual fase do {boss_usuario} você irá enfrentar? "(1,2,3,4,5,6)"''\n').strip().replace(' ', '')
            while variação not in ['1', '2', '3', '4', '5', '6']:
                variação = input(f'Qual fase do {boss_usuario} você irá enfrentar? "(1,2,3,4,5,6)"''\n').strip().replace(' ', '')
            return int(variação)
        elif boss_usuario == 'Shadow Pieces' or boss_usuario == 'Reanimated Skeleton' or boss_usuario == 'Treeguard' or boss_usuario == 'Celestial Champion':
            variação = input(f'Qual fase do {boss_usuario} você irá enfrentar? "(1,2,3)"''\n').strip().replace(' ', '')
            while variação not in ['1', '2', '3']:
                variação = input(f'Qual fase do {boss_usuario} você irá enfrentar? "(1,2,3)"''\n').strip().replace(' ', '')
            return int(variação)
        elif boss_usuario == 'Toadstool' or boss_usuario == 'Klaus' or boss_usuario == 'Klaus Enraged' or boss_usuario == 'Eye of Terror':
            variação = input(f'Qual fase do {boss_usuario} você irá enfrentar? "(1,2)"''\n').strip().replace(' ', '')
            while variação not in ['1', '2']:
                variação = input(f'Qual fase do {boss_usuario} você irá enfrentar? "(1,2)"''\n').strip().replace(' ', '')
            return int(variação)

    def dano_boss(self, boss_info, fase_boss, boss_usuario):
        if boss_usuario == 'Toadstool' or boss_usuario == 'Klaus' or boss_usuario == 'Klaus Enraged' or boss_usuario == 'Eye of Terror' or boss_usuario == 'Shadow Pieces' or boss_usuario == 'Reanimated Skeleton' or boss_usuario == 'Treeguard' or boss_usuario == 'Celestial Champion' or boss_usuario == 'Crab King':
            dano_boss = boss_info[fase_boss - 1] / self.buff
            return dano_boss
        else: 
            dano_boss = boss_info / self.buff
            return dano_boss

    def print_dano_boss(self, boss_usuario, hit_boss):
        if boss_usuario == 'Shadow Pieces':
            print(f'Você precisará acertar {hit_boss[0]:.2f} para derrotar o Shadow Knight, {hit_boss[1]:.2f} para derrotar o Shadow Bishop e {hit_boss[2]:.2f} para derrotar o Shadow Rook.')
        else:
            print(f'Você precisará acertar {hit_boss:.2f} para derrotar {boss_usuario}')

# O usuário será questinado se deseja reiniciar a calculadora. Se sim, o programa retornará ao início.

    def reiniciar(self):
        while True:     
            s(1)
            tentativa = input('Quer reiniciar a calculadora?''\n').replace(' ', '').title()
            match tentativa:
                case "Sim":
                    print ('Ok. Vamos lá!')
                    s(2)
                    self.clear_screen()
                    main()
                case _:
                    print('Ok. Obrigado por usar a calculadora de dano da "Jogatina dos Putos"!')
                    s(1)
                    quit()   
# Fim do programa. Houve um singelo agredecimento seguido do encerramento.  

# Instâncias da classe e objetos #
def main():
    print('"Jogatina dos Putos" apresenta...')
    s(1)
    print('Calculadora de Dano - Don\'t Starve Together')
    s(1)
    calculadora = Calculadora()
    calculadora.personagem(Dicionário.multiplicador)
    calculadora.arma(Dicionário.weapon)
    calculadora.dano()
    s(2)
    calculadora.buffs()
    calculadora.bosses()

if __name__ == "__main__":
    main()
# Instâncias da classe e objetos #  