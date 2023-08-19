# Programa feito com a intenção de calcular e  descobrir o dano causado por cada personagem do DST
import time
klaus = {'normal': (10000, 5000), 'enraged' : (27440, 13720)}
shadow_pieces = {'shadow knight': (900, 2700, 8100), 'shadow bishop' : (800, 2500, 7500), 'shadow rook' : (1000, 4000, 10000)}
# Espaço dos Dicionários #
weapon = {'Spear': 34, 'Tentacle Spear': 51, 'Ham Bat': 59.5, 'Dart': 100, 'Boomerang': 27.2, 'Tail': 27.2, 'Morning Star': 43.35, 'Battle Spear': 42.5, 
'Slingshot': (17,34,51), 'Dark Sword': 68}
multiplicador = {'Wendy': 0.75, 'Wes': 0.75, 'Wigfrid': 1.25, 'Wolfgang': 2.00, 'Wilson': 1.00, 'Willow': 1.00, 'Wx-78': 1.00, 'Wickerbottom': 1.00, 'Woodie': 1.00, 
'Maxwell': 1.00, 'Webber': 1.00, 'Winona': 1.00, 'Warly': 1.00, 'Wortox': 1.00, 'Wurt': 1.00, 'Walter': 1.00, 'Wanda': 1.00}
chefes = {'Ancient Guardian' : 2500, 'Antlion' : 6000, 'Bearger' : 6000, 'Bee Queen' : 22500, 'Celestial Champion' : (10000, 13000, 14000), 
'Crab King' : (20000, 23000, 32000, 47000, 68000, 95000), 'Deerclops' : 4000, 'Dragonfly' : 2750, 'Eye of Terror' : (5000, 10000), 'Grand Forge Boarrior' : 34000, 
'Infernal Swineclops' : 42500, 'Klaus' : (10000, 5000), 'Klaus Enraged' : (27440, 13720), 'Lord of the Fruit Flies' : 1500, 'Malbatross' : 5000, 'Moose' : 6000, 
'Reanimated Skeleton' : (4000, 4000, 16000), 'Spider Queen' : 2500, 'Toadstool' : (52500, 99999), 'Treeguard' : (2100, 3000, 3750)}
# Espaço dos Dicionários #

# Usuário informará seu personagem, o programa realizará a busca no dicionário "multiplicador" e passará para a próxima parte
# caso o resultado seja "True".
def calculadora():
    print ('"Jogatina dos Putos" apresenta...')
    time.sleep(1)
    print ('Calculadora de Dano - Dont Starve Together')
    time.sleep(1)
    def personagem():
        global personagem_jogado
        time.sleep(1)
        personagem_jogado = input('Com qual personagem do capeta você está jogando?''\n').replace(' ', '').title()
        if personagem_jogado in multiplicador:
            time.sleep(1)
            print('Sério que você escolheu %s? Espero que saiba o que está fazendo.' %personagem_jogado)
            if personagem_jogado == 'Wolfgang':
             time.sleep(1)
             print('Lembrando que o Wolfão tem que tá bem alimentado pra ficar grandão e bater mais')
            elif personagem_jogado == 'Wx-78':
                time.sleep(1)
                print('O dano do robozinho vai ser o mesmo com ou sem o chip de Eletricidade')    
        else:
            time.sleep(1)
            print('Coloque um personagem jogável')
    while True:
        personagem()
        if personagem_jogado in multiplicador:
            break
        elif personagem_jogado not in multiplicador:
            tentativa = input('Quer tentar de novo?''\n').replace(' ', '').title()
            if tentativa == 'Não':
                time.sleep(1)
                print('Ok. Tchau')
                quit()

# O usuário informará sua arma, o programa buscará no dicionário "weapon" e passará para a próxima parte caso o resultado seja "True".
    time.sleep(1)
    def arma():
        global munição
        global arma_usada
        arma_usada = input('Qual arma você está usando?''\n').strip().title()
        if arma_usada in weapon:
            time.sleep(1)
            print('Logo a %s? Tinha arma melhor não?' %arma_usada)
            if arma_usada == 'Battle Spear' and personagem_jogado == 'Wigfrid':
                time.sleep(1)
                print('"All the wörlds a stage. För me!" ')
            elif arma_usada == 'Dark Sword' and personagem_jogado == 'Maxwell':
                time.sleep(1)
                print('"Freedom suits me."')
            elif arma_usada == 'Ham Bat' and personagem_jogado == 'Wolfgang':
                time.sleep(1)
                print('"I am mighty! No one is mightier!"')
            elif arma_usada == 'Slingshot':
                time.sleep(1)
                if personagem_jogado != 'Walter':
                    time.sleep(1)
                    print(f'Peraí.....{personagem_jogado} não consegue equipar a {arma_usada}. Só o Waltinho consegue usar ela')
                    while personagem_jogado != 'Walter':
                        arma()
                        break 
                else:
                    time.sleep(1)
                    print('"A Pinetree Pioneer is always prepared!"')
                    munição = input('Qual munição você usará?("Pedra", "Ouro" ou "Mármore")''\n').replace(' ', '').title()
        else:        
            time.sleep (1)
            print('Essa arma não existe ou eu não a conheço. Tente alguma outra')
    while True:
        arma()
        if arma_usada in weapon:
            break
        elif arma_usada not in weapon:
            tentativa = input('Quer tentar de novo?''\n').replace(' ', '').title()
            if tentativa == 'Não':
                print('Ok. Tchau')
                time.sleep (1)
                quit()

# O programa usará os valores correspondentes às strings informadas pelo usuário para fazer uma simples operação de multiplicação
    def dano():
        for key in multiplicador.keys():
            if key.startswith(personagem_jogado):
                global dano_personagem
                dano_personagem = (multiplicador[key])   
        for key in weapon.keys():
            if key.startswith(arma_usada):
                global dano_arma
                dano_arma = (weapon[key])
                if arma_usada == 'Slingshot':
                    if munição == 'Pedra':
                        dano_arma = (weapon['Slingshot'][0])
                    elif munição == 'Ouro':
                        dano_arma = (weapon['Slingshot'][1])
                    elif munição == 'Mármore':
                        dano_arma = (weapon['Slingshot'][2])
        global dano_base
        dano_base = dano_personagem * dano_arma
        time.sleep (1)
        #progress bar
        print ('Seu dano base é %d.' %dano_base)
    dano()

    time.sleep (1)
    print('Existem dois buffs de comida que podem complementar o dano causado: Volt Goat Chaud-Froid e Chili Flakes')

# Após essa operação, finalmente o programa será capaz de apontar quanto de dano o personagem causará com um ou mais buffs.
    def buffs():
        time.sleep(1)
        global pergunta_buff
        pergunta_buff = input('Qual buff você quer ver aplicado sobre o seu dano? ("volt", "chili" ou "ambos")?''\n').replace(' ', '').title()
        #progress bar
        if pergunta_buff == 'Volt':
            global volt
            volt = dano_base * 1.5
            global volt2
            volt2 = dano_base * 2.5
            time.sleep(1)
            print('Seu dano com a Volt Goat Chaud-Froid é {0:.2f}, e se o mob estiver "Wet", você causará {1:.2f}'.format(volt, volt2))
        elif pergunta_buff == 'Chili':
            global chili
            chili = dano_base * 1.2
            time.sleep(1)
            print('Seu dano com o buff da Chili Flakes passa a ser de %d.' %chili)
        elif pergunta_buff == "Ambos":
            global ambos
            ambos = (dano_base * 1.5) * 1.2
            global ambos2
            ambos2 = dano_base * 3.0
            time.sleep(1)
            print('Seu dano com os dois buffs será de {0:.2f}, e {1:.2f} se o mob estiver "Wet"'.format(ambos, ambos2))       
    time.sleep(1)
    while True:
        buffs()
        outro_buff = input('Quer testar outro buff?''\n').replace(' ', '').title()
        if outro_buff== 'Sim':
            time.sleep(1) 
            print('Entendido')
        else:
            time.sleep(1)
            break
    
    time.sleep(1)
# O usuário será questinado se deseja reiniciar a calculadora. Se sim, o programa retornará ao início.
    def novamente():
        while True:
            time.sleep(1)
            tentar_novamente = input('Quer reiniciar a calculadora?''\n').replace(' ', '').title()
            if tentar_novamente == 'Sim':
                print ('Ok. Vamos lá!')
                calculadora()
            else:
                print('Ok. Obrigado por usar a calculadora de dano da "Jogatina dos Putos"!')
                time.sleep(1)
                quit()

# Nesta função, o usuário poderá descobrir quantos hits eles precisará acertar para derrotar cada um dos boss monster do game
    def bosses():
        global boss_usuario
        global boss
        boss_usuario = input ('Qual boss você irá enfrentar?''\n').strip().title()
        if boss_usuario in chefes:
            time.sleep(1)
            print (f'{boss_usuario}? Boa sorte!')       
        while boss_usuario not in chefes:
            time.sleep(1)
            tentativa_boss = input('Esse boss não existe. Quer tentar de novo?''\n').replace(' ', '').title()
            if tentativa_boss == 'Sim':
                bosses()
            else:
                novamente()
        for key in chefes.keys():
            if key.startswith(boss_usuario):
                boss = (chefes[key]) 
                if boss_usuario == 'Celestial Champion':
                    time.sleep(1)
                    fase = input (f'Qual fase do {boss_usuario} você irá enfrentar? "(1,2,3)"''\n').replace(' ', '')
                    if fase == '1':
                        boss = (chefes['Celestial Champion'][0])
                    if fase == '2':
                        boss = (chefes['Celestial Champion'][1])
                    if fase == '3':
                        boss = (chefes['Celestial Champion'][2])
                hit_boss = boss / ambos2
                time.sleep (1)
                print (f'Você precisará acertar {hit_boss:.2f} para derrotar o {boss_usuario}') 
                #progress bar   
    bosses() 
calculadora()
# Fim do programa. Houve um singelo agredecimento seguido do encerramento.    