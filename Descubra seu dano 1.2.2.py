# Programa feito com a intenção de calcular e  descobrir o dano causado por cada personagem de Don't Starve Together

# Feito por Wilson Júnior.
import time
# Espaço dos Dicionários #
weapon = {
    'Spear': 34, 'Tentacle Spear': 51, 'Ham Bat': 59.5, 'Dart': 100, 'Boomerang': 27.2, 'Tail': 27.2, 'Morning Star': 43.35, 
    'Battle Spear': 42.5, 'Slingshot': (17,34,51), 'Dark Sword': 68
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

# Usuário informará se'u' personagem, o programa realizará a busca no dicionário "multiplicador" e passará para a próxima parte
# caso o resultado seja "True".
class Calculadora():
    print ('"Jogatina dos Putos" apresenta...')
    time.sleep(1)
    print ('Calculadora de Dano - Dont Starve Together')
    time.sleep(1)

    def __init__(self):
        self.personagem_jogado= ""
        self.arma_usada= ""
        self.municao = ""
        self.dano_personagem = 1
        self.dano_arma = 1
        self.buff = 1

    def personagem(self):
        
        time.sleep(1)
        self.personagem_jogado = input('Com qual personagem do capeta você está jogando?''\n').replace(' ', '').title()
        if self.personagem_jogado in multiplicador:
            time.sleep(1)
            print(f'Sério que você escolheu {self.personagem_jogado}? Espero que saiba o que está fazendo.')
            if self.personagem_jogado == 'Wolfgang':
                time.sleep(1)
                print('O dia tem que tá pago pro Wolfão aumentar seu dano')
            elif self.personagem_jogado == 'Wx-78':
                time.sleep(1)
                print('O dano do robozinho vai ser o mesmo com ou sem o chip de Eletricidade')    
        else:
            time.sleep(1)
            print('Coloque um personagem jogável')
            while self.personagem_jogado not in multiplicador:
                tentativa = input('Quer tentar de novo?''\n').replace(' ', '').title()
                if tentativa == 'Sim':
                    calculadora.personagem()
                    break
                else:
                    time.sleep(1)
                    print('Ok. Tchau')
                    quit()

# O usuário informará sua arma, o programa buscará no dicionário "weapon" e passará para a próxima parte caso o resultado seja "True".
    time.sleep(1)
    def arma(self):
        self.arma_usada = input('Qual arma você está usando?''\n').strip().title()
        if self.arma_usada in weapon:
            time.sleep(1)
            print(f'Logo a {self.arma_usada}? Tinha arma melhor não?')
            if self.arma_usada == 'Battle Spear' and self.personagem_jogado == 'Wigfrid':
                time.sleep(1)
                print('"All the wörlds a stage. För me!" ')
            elif self.arma_usada == 'Dark Sword' and self.personagem_jogado == 'Maxwell':
                time.sleep(1)
                print('"Freedom suits me."')
            elif self.arma_usada == 'Ham Bat' and self.personagem_jogado == 'Wolfgang':
                time.sleep(1)
                print('"I am mighty! No one is mightier!"')
            elif self.arma_usada == 'Slingshot':
                time.sleep(1)
                if self.personagem_jogado != 'Walter':
                    time.sleep(1)
                    print(f'Peraí.....{self.personagem_jogado} não consegue equipar a {self.arma_usada}. Só o Waltinho consegue usar ela')
                    while self.personagem_jogado != 'Walter':
                        calculadora.arma()
                        break 
                else:
                    time.sleep(1)
                    print('"A Pinetree Pioneer is always prepared!"')
        else:        
            time.sleep (1)
            print('Essa arma não existe ou eu não a conheço. Tente alguma outra')
            while self.arma_usada not in weapon:
                tentativa = input('Quer tentar de novo?''\n').replace(' ', '').title()
                if tentativa == "Sim":
                    calculadora.arma()
                    break
                else:
                    print('Ok. Tchau')
                    time.sleep (1)
                    quit()

# O programa usará os valores correspondentes às strings informadas pelo usuário para fazer uma simples operação de multiplicação
    def dano(self):
        for key in multiplicador.keys():
            if key.startswith(self.personagem_jogado):
                self.dano_personagem = (multiplicador[key])  
                if self.personagem_jogado == 'Wolfgang':
                    variação = input('Wolfão foi pra academia?"S/N"''\n').replace(' ', '').title()
                    time.sleep (1)
                    if variação == 'N':
                        self.dano_personagem = (multiplicador['Wolfgang'][0])
                    elif variação == 'S':
                        self.dano_personagem = (multiplicador['Wolfgang'][1])
        for key in weapon.keys():
            if key.startswith(self.arma_usada):
                self.dano_arma = (weapon[key])
                if self.arma_usada == 'Slingshot':
                    self.munição = input('Qual munição você usará?("Pedra", "Ouro" ou "Mármore")''\n').replace(' ', '').title()
                    time.sleep (1)
                    if self.munição == 'Pedra':
                        self.dano_arma = (weapon['Slingshot'][0])
                    elif self.munição == 'Ouro':
                        self.dano_arma = (weapon['Slingshot'][1])
                    elif self.munição == 'Mármore':
                        self.dano_arma = (weapon['Slingshot'][2])
        self.dano_base = self.dano_personagem * self.dano_arma
        time.sleep (1)
        #progress bar
        print (f'Seu dano base é {self.dano_base}.')
    time.sleep (1)
    
# Após essa operação, finalmente o programa será capaz de apontar quanto de dano o personagem causará com um ou mais buffs.
    def buffs(self):
        print('Existem dois buffs de comida que podem complementar o dano causado: Volt Goat Chaud-Froid e Chili Flakes')
        time.sleep(1)
        pergunta_buff = input('Qual buff você quer ver aplicado sobre o seu dano? ("volt", "chili" ou "ambos")?''\n').replace(' ', '').title()
        #progress bar
        if pergunta_buff == 'Volt':
            variação = input('O monstro estará seco ou "Wet"?"(1,2)"''\n').replace(' ', '')
            time.sleep (1)
            match variação:
                case '1':
                    volt = self.dano_base * 1.5
                    self.buff = volt
                    print(f'Seu dano com a Volt Goat Chaud-Froid é {self.buff:.2f}')
                case '2':
                    volt2 = self.dano_base * 2.5
                    self.buff = volt2
                    print(f'Seu dano com a Volt Goat Chaud-Froid  se o mob estiver "Wet" será {self.buff:.2f}')
            time.sleep(1)
        elif pergunta_buff == 'Chili':
            chili = self.dano_base * 1.2
            self.buff = chili
            time.sleep(1)
            print(f'Seu dano com o buff da Chili Flakes passa a ser de {self.buff:.2f}.')
        elif pergunta_buff == 'Ambos':
            variação = input('O monstro estará seco ou "Wet"?"(1,2)"''\n').replace(' ', '')
            time.sleep (1)
            match variação:
                case '1':
                    ambos = (self.dano_base * 1.5) * 1.2
                    self.buff = ambos
                    print(f'Seu dano com os dois buffs será de {self.buff:.2f}')
                case '2':
                    ambos2 = self.dano_base * 3.0
                    self.buff = ambos2
                    print(f'Seu dano com os dois buffs será de {self.buff:.2f} se o mob estiver "Wet"')
            time.sleep(1)  
        time.sleep(1)
        tentativa = input('Quer testar outro buff?''\n').replace(' ', '').title()
        if tentativa== 'Sim':
            time.sleep(1) 
            print('Entendido')

    time.sleep(1)
# O usuário será questinado se deseja reiniciar a calculadora. Se sim, o programa retornará ao início.
    def novamente():
        while True:
            time.sleep(1)
            tentativa = input('Quer reiniciar a calculadora?''\n').replace(' ', '').title()
            if tentativa == 'Sim':
                print ('Ok. Vamos lá!')
                calculadora()
            else:
                print('Ok. Obrigado por usar a calculadora de dano da "Jogatina dos Putos"!')
                time.sleep(1)
                quit()        
    time.sleep(1)
# Nesta função, o usuário poderá descobrir quantos hits eles precisará acertar para derrotar cada um dos boss monster do game
    def bosses(self):
        boss_usuario = input('Qual boss você irá enfrentar?''\n').strip().title()
        boss = boss_usuario
        while boss_usuario in chefes:
            time.sleep(1)
            print (f'{boss_usuario}? Boa sorte!') 
            for key in chefes.keys():
                if key.startswith(boss_usuario):
                    boss = (chefes[key])
                    time.sleep (1)
                    if boss_usuario == 'Celestial Champion':
                        variação = input (f'Qual fase do {boss_usuario} você irá enfrentar? "(1,2,3)"''\n').replace(' ', '')      
                        match variação:
                            case '1':
                                boss = (chefes['Celestial Champion'][0])
                                hit_boss = boss
                                hit_boss = hit_boss / self.buff
                                time.sleep (1)                       
                            case '2':
                                boss = (chefes['Celestial Champion'][1])
                                hit_boss = boss
                                hit_boss = hit_boss / self.buff
                                time.sleep (1)
                            case '3':
                                boss = (chefes['Celestial Champion'][2])
                                hit_boss = boss
                                hit_boss = hit_boss / self.buff
                                time.sleep (1)
                    if boss_usuario == 'Klaus':
                        variação = input (f'Qual fase do {boss_usuario} você irá enfrentar? "(1,2)"''\n').replace(' ', '') 
                        match variação:
                            case '1':
                                boss = (chefes['Klaus'][0])
                                hit_boss = boss
                                hit_boss = hit_boss / self.buff
                                time.sleep (1)                        
                            case '2':
                                boss = (chefes['Klaus'][1])
                                hit_boss = boss
                                hit_boss = hit_boss / self.buff
                                time.sleep (1)
                    if boss_usuario == 'Klaus Enraged':
                        variação = input (f'Qual fase do {boss_usuario} você irá enfrentar? "(1,2)"''\n').replace(' ', '') 
                        match variação:
                            case '1':
                                boss = (chefes['Klaus Enraged'][0])
                                hit_boss = boss
                                hit_boss = hit_boss / self.buff
                                time.sleep (1)                     
                            case '2':
                                boss = (chefes['Klaus Enraged'][1])
                                hit_boss = boss
                                hit_boss = hit_boss / self.buff
                                time.sleep (1)                           
                    if boss_usuario == 'Reanimated Skeleton':
                        variação = input (f'Qual fase do {boss_usuario} você irá enfrentar? "(1,2,3)"''\n').replace(' ', '')      
                        match variação:
                            case '1':
                                boss = (chefes['Reanimated Skeleton'][0])
                                hit_boss = boss
                                hit_boss = hit_boss / self.buff
                                time.sleep (1)                     
                            case '2':
                                boss = (chefes['Reanimated Skeleton'][1])
                                hit_boss = boss
                                hit_boss = hit_boss / self.buff
                                time.sleep (1)
                            case '3':
                                boss = (chefes['Reanimated Skeleton'][2])
                                hit_boss = boss
                                hit_boss = hit_boss / self.buff
                                time.sleep (1)     
                    if boss_usuario == 'Toadstool':
                        variação = input (f'Qual fase do {boss_usuario} você irá enfrentar? "(1,2)"''\n').replace(' ', '') 
                        match variação:
                            case '1':
                                boss = (chefes['Toadstool'][0])
                                hit_boss = boss
                                hit_boss = hit_boss / self.buff
                                time.sleep (1)                        
                            case '2':
                                boss = (chefes['Toadstool'][1])
                                hit_boss = boss
                                hit_boss = hit_boss / self.buff
                                time.sleep (1)         
                    if boss_usuario == 'Treeguard':
                        variação = input (f'Qual fase do {boss_usuario} você irá enfrentar? "(1,2,3)"''\n').replace(' ', '')      
                        match variação:
                            case '1':
                                boss = (chefes['Treeguard'][0])
                                hit_boss = boss
                                hit_boss = hit_boss / self.buff
                                time.sleep (1)                           
                            case '2':
                                boss = (chefes['Treeguard'][1])
                                hit_boss = boss
                                hit_boss = hit_boss / self.buff
                                time.sleep (1)
                            case '3':
                                boss = (chefes['Treeguard'][2])
                                hit_boss = boss
                                hit_boss = hit_boss / self.buff
                                time.sleep (1)
                    if boss_usuario == 'Shadow Pieces':
                        variação = input (f'Qual fase do {boss_usuario} você irá enfrentar? "(1,2,3)"''\n').replace(' ', '') 
                        match variação:
                            case '1':
                                boss = (chefes['Shadow Pieces'][0])
                                hit_boss = boss
                                boss2 = (chefes['Shadow Pieces'][3])
                                hit_boss2 = boss2
                                boss3 = (chefes['Shadow Pieces'][6])
                                hit_boss3 = boss3
                                hit_boss = hit_boss / self.buff
                                hit_boss2 = hit_boss2 / self.buff
                                hit_boss3 = hit_boss3 / self.buff
                                time.sleep (1)                           
                            case '2':
                                boss = (chefes['Shadow Pieces'][1])
                                hit_boss = boss
                                boss2 = (chefes['Shadow Pieces'][4])
                                hit_boss2 = boss2
                                boss3 = (chefes['Shadow Pieces'][7])
                                hit_boss3 = boss3
                                hit_boss = hit_boss / self.buff
                                hit_boss2 = hit_boss2 / self.buff
                                hit_boss3 = hit_boss3 / self.buff
                                time.sleep (1)         
                            case '3':
                                boss = (chefes['Shadow Pieces'][2])
                                hit_boss = boss
                                boss2 = (chefes['Shadow Pieces'][5])
                                hit_boss2 = boss2
                                boss3 = (chefes['Shadow Pieces'][8])
                                hit_boss3 = boss3
                                hit_boss = hit_boss / self.buff
                                hit_boss2 = hit_boss2 / self.buff
                                hit_boss3 = hit_boss3 / self.buff
                                time.sleep (1) 
                        print (f'Você precisará acertar {hit_boss:.2f} para derrotar o Shadow Knight, {hit_boss2:.2f} para derrotar o Shadow Bishop e {hit_boss:.2f} para derrotar o Shadow Rook.')
                    hit_boss = boss
                    hit_boss = hit_boss / self.buff
                    time.sleep (1)
                    if boss_usuario != 'Shadow Pieces':
                        print (f'Você precisará acertar {hit_boss:.2f} para derrotar {boss_usuario}')
                    tentativa_boss = input('Quer escolher outro boss?''\n').replace(' ', '').title()    
                    if tentativa_boss == 'Sim':
                        calculadora.bosses()
                    else:
                        calculadora.novamente()
        while boss_usuario not in chefes:
            time.sleep(1)
            tentativa_boss = input('Esse boss não existe. Quer tentar de novo?''\n').replace(' ', '').title()
            if tentativa_boss == 'Sim':
                calculadora.bosses()
            else:
                calculadora.novamente()
    bosses 


calculadora = Calculadora()
calculadora.personagem()
calculadora.arma()
calculadora.dano()
calculadora.buffs()
calculadora.bosses()
calculadora.novamente()
# Fim do programa. Houve um singelo agredecimento seguido do encerramento.    