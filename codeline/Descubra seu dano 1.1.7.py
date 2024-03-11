# Programa feito com a intenção de calcular e  descobrir o dano causado por cada personagem do DST
import time
# Espaço dos Dicionários #
weapon = {'Spear': 34, 'Tentacle Spear': 51, 'Ham Bat': 59.5, 'Dart': 100, 'Boomerang': 27.2, 'Tail': 27.2, 'Morning Star': 43.35, 'Battle Spear': 42.5, 
'Slingshot': (17,34,51), 'Dark Sword': 68}
multiplicador = {'Wendy': 0.75, 'Wes': 0.75, 'Wigfrid': 1.25, 'Wolfgang': (1.00, 2.00), 'Wilson': 1.00, 'Willow': 1.00, 'Wx-78': 1.00, 'Wickerbottom': 1.00, 'Woodie': 1.00, 
'Maxwell': 1.00, 'Webber': 1.00, 'Winona': 1.00, 'Warly': 1.00, 'Wortox': 1.00, 'Wurt': 1.00, 'Walter': 1.00, 'Wanda': 1.00}
chefes = {'Ancient Guardian' : 2500, 'Antlion' : 6000, 'Bearger' : 6000, 'Bee Queen' : 22500, 'Celestial Champion' : (10000, 13000, 14000), 
'Crab King' : (20000, 23000, 32000, 47000, 68000, 95000), 'Deerclops' : 4000, 'Dragonfly' : 2750, 'Eye of Terror' : (5000, 10000), 'Grand Forge Boarrior' : 34000, 
'Infernal Swineclops' : 42500, 'Klaus' : (10000, 5000), 'Klaus Enraged' : (27440, 13720), 'Lord of the Fruit Flies' : 1500, 'Malbatross' : 5000, 'Moose' : 6000, 
'Reanimated Skeleton' : (4000, 4000, 16000), 'Spider Queen' : 2500, 'Toadstool' : (52500, 99999), 'Treeguard' : (2100, 3000, 3750), 'Shadow Pieces' : (900, 2700, 8100, 800, 2500, 7500, 1000, 4000, 10000)}
# Espaço dos Dicionários #
# Usuário informará se'u' personagem, o programa realizará a busca no dicionário "multiplicador" e passará para a próxima parte
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
            print(f'Sério que você escolheu {personagem_jogado}? Espero que saiba o que está fazendo.')
            if personagem_jogado == 'Wolfgang':
                time.sleep(1)
                print('O dia tem que tá pago pro Wolfão aumentar seu dano')
            elif personagem_jogado == 'Wx-78':
                time.sleep(1)
                print('O dano do robozinho vai ser o mesmo com ou sem o chip de Eletricidade')    
        else:
            time.sleep(1)
            print('Coloque um personagem jogável')
            while personagem_jogado not in multiplicador:
                tentativa = input('Quer tentar de novo?''\n').replace(' ', '').title()
                if tentativa == 'Sim':
                    personagem()
                    break
                else:
                    time.sleep(1)
                    print('Ok. Tchau')
                    quit()
        return str(personagem_jogado)
    personagem()
# O usuário informará sua arma, o programa buscará no dicionário "weapon" e passará para a próxima parte caso o resultado seja "True".
    time.sleep(1)
    def arma(personagem_jogado):
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
        else:        
            time.sleep (1)
            print('Essa arma não existe ou eu não a conheço. Tente alguma outra')
            while arma_usada not in weapon:
                tentativa = input('Quer tentar de novo?''\n').replace(' ', '').title()
                if tentativa == "Sim":
                    arma(personagem)
                    break
                else:
                    print('Ok. Tchau')
                    time.sleep (1)
                    quit()
        return arma_usada
    arma(personagem)
# O programa usará os valores correspondentes às strings informadas pelo usuário para fazer uma simples operação de multiplicação
    def dano(personagem_jogado, arma_usada):
        for key in multiplicador.keys():
            if key.startswith(personagem_jogado):
                dano_personagem = (multiplicador[key])  
                if personagem_jogado == 'Wolfgang':
                    variação = input('Wolfão foi pra academia?"S/N"''\n').replace(' ', '').title()
                    time.sleep (1)
                    if variação == 'N':
                        dano_personagem = (multiplicador['Wolfgang'][0])
                    elif variação == 'S':
                        dano_personagem = (multiplicador['Wolfgang'][1])
        for key in weapon.keys():
            if key.startswith(arma_usada):
                dano_arma = (weapon[key])
                if arma_usada == 'Slingshot':
                    munição = input('Qual munição você usará?("Pedra", "Ouro" ou "Mármore")''\n').replace(' ', '').title()
                    time.sleep (1)
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
    dano(personagem_jogado, arma_usada)
    time.sleep (1)
    print('Existem dois buffs de comida que podem complementar o dano causado: Volt Goat Chaud-Froid e Chili Flakes')
# Após essa operação, finalmente o programa será capaz de apontar quanto de dano o personagem causará com um ou mais buffs.
    def buffs(dano_base):
        global buff
        time.sleep(1)
        pergunta_buff = input('Qual buff você quer ver aplicado sobre o seu dano? ("volt", "chili" ou "ambos")?''\n').replace(' ', '').title()
        #progress bar
        if pergunta_buff == 'Volt':
            variação = input('O monstro estará seco ou "Wet"?"(1,2)"''\n').replace(' ', '')
            time.sleep (1)
            match variação:
                case '1':
                    volt = dano_base * 1.5
                    buff = volt
                    print(f'Seu dano com a Volt Goat Chaud-Froid é {buff:.2f}')
                case '2':
                    volt2 = dano_base * 2.5
                    buff = volt2
                    print(f'Seu dano com a Volt Goat Chaud-Froid  se o mob estiver "Wet" será {buff:.2f}')
            time.sleep(1)
        elif pergunta_buff == 'Chili':
            chili = dano_base * 1.2
            buff = chili
            time.sleep(1)
            print(f'Seu dano com o buff da Chili Flakes passa a ser de {buff:.2f}.')
        elif pergunta_buff == 'Ambos':
            variação = input('O monstro estará seco ou "Wet"?"(1,2)"''\n').replace(' ', '')
            time.sleep (1)
            match variação:
                case '1':
                    ambos = (dano_base * 1.5) * 1.2
                    buff = ambos
                    print(f'Seu dano com os dois buffs será de {buff:.2f}')
                case '2':
                    ambos2 = dano_base * 3.0
                    buff = ambos2
                    print(f'Seu dano com os dois buffs será de {buff:.2f} se o mob estiver "Wet"')
            time.sleep(1)  
        time.sleep(1)
        tentativa = input('Quer testar outro buff?''\n').replace(' ', '').title()
        if tentativa== 'Sim':
            time.sleep(1) 
            print('Entendido')
            buffs(dano_base)
        return buff
    buffs(dano_base)   
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
    def bosses(buff):
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
                                hit_boss = hit_boss / buff
                                time.sleep (1)                       
                            case '2':
                                boss = (chefes['Celestial Champion'][1])
                                hit_boss = boss
                                hit_boss = hit_boss / buff
                                time.sleep (1)
                            case '3':
                                boss = (chefes['Celestial Champion'][2])
                                hit_boss = boss
                                hit_boss = hit_boss / buff
                                time.sleep (1)
                    if boss_usuario == 'Klaus':
                        variação = input (f'Qual fase do {boss_usuario} você irá enfrentar? "(1,2)"''\n').replace(' ', '') 
                        match variação:
                            case '1':
                                boss = (chefes['Klaus'][0])
                                hit_boss = boss
                                hit_boss = hit_boss / buff
                                time.sleep (1)                        
                            case '2':
                                boss = (chefes['Klaus'][1])
                                hit_boss = boss
                                hit_boss = hit_boss / buff
                                time.sleep (1)
                    if boss_usuario == 'Klaus Enraged':
                        variação = input (f'Qual fase do {boss_usuario} você irá enfrentar? "(1,2)"''\n').replace(' ', '') 
                        match variação:
                            case '1':
                                boss = (chefes['Klaus Enraged'][0])
                                hit_boss = boss
                                hit_boss = hit_boss / buff
                                time.sleep (1)                     
                            case '2':
                                boss = (chefes['Klaus Enraged'][1])
                                hit_boss = boss
                                hit_boss = hit_boss / buff
                                time.sleep (1)                           
                    if boss_usuario == 'Reanimated Skeleton':
                        variação = input (f'Qual fase do {boss_usuario} você irá enfrentar? "(1,2,3)"''\n').replace(' ', '')      
                        match variação:
                            case '1':
                                boss = (chefes['Reanimated Skeleton'][0])
                                hit_boss = boss
                                hit_boss = hit_boss / buff
                                time.sleep (1)                     
                            case '2':
                                boss = (chefes['Reanimated Skeleton'][1])
                                hit_boss = boss
                                hit_boss = hit_boss / buff
                                time.sleep (1)
                            case '3':
                                boss = (chefes['Reanimated Skeleton'][2])
                                hit_boss = boss
                                hit_boss = hit_boss / buff
                                time.sleep (1)     
                    if boss_usuario == 'Toadstool':
                        variação = input (f'Qual fase do {boss_usuario} você irá enfrentar? "(1,2)"''\n').replace(' ', '') 
                        match variação:
                            case '1':
                                boss = (chefes['Toadstool'][0])
                                hit_boss = boss
                                hit_boss = hit_boss / buff
                                time.sleep (1)                        
                            case '2':
                                boss = (chefes['Toadstool'][1])
                                hit_boss = boss
                                hit_boss = hit_boss / buff
                                time.sleep (1)         
                    if boss_usuario == 'Treeguard':
                        variação = input (f'Qual fase do {boss_usuario} você irá enfrentar? "(1,2,3)"''\n').replace(' ', '')      
                        match variação:
                            case '1':
                                boss = (chefes['Treeguard'][0])
                                hit_boss = boss
                                hit_boss = hit_boss / buff
                                time.sleep (1)                           
                            case '2':
                                boss = (chefes['Treeguard'][1])
                                hit_boss = boss
                                hit_boss = hit_boss / buff
                                time.sleep (1)
                            case '3':
                                boss = (chefes['Treeguard'][2])
                                hit_boss = boss
                                hit_boss = hit_boss / buff
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
                                hit_boss = hit_boss / buff
                                hit_boss2 = hit_boss2 / buff
                                hit_boss3 = hit_boss3 / buff
                                time.sleep (1)                           
                            case '2':
                                boss = (chefes['Shadow Pieces'][1])
                                hit_boss = boss
                                boss2 = (chefes['Shadow Pieces'][4])
                                hit_boss2 = boss2
                                boss3 = (chefes['Shadow Pieces'][7])
                                hit_boss3 = boss3
                                hit_boss = hit_boss / buff
                                hit_boss2 = hit_boss2 / buff
                                hit_boss3 = hit_boss3 / buff
                                time.sleep (1)         
                            case '3':
                                boss = (chefes['Shadow Pieces'][2])
                                hit_boss = boss
                                boss2 = (chefes['Shadow Pieces'][5])
                                hit_boss2 = boss2
                                boss3 = (chefes['Shadow Pieces'][8])
                                hit_boss3 = boss3
                                hit_boss = hit_boss / buff
                                hit_boss2 = hit_boss2 / buff
                                hit_boss3 = hit_boss3 / buff
                                time.sleep (1) 
                        print (f'Você precisará acertar {hit_boss:.2f} para derrotar o Shadow Knight, {hit_boss2:.2f} para derrotar o Shadow Bishop e {hit_boss:.2f} para derrotar o Shadow Rook.')
                    hit_boss = boss
                    hit_boss = hit_boss / buff
                    time.sleep (1)
                    if boss_usuario != 'Shadow Pieces':
                        print (f'Você precisará acertar {hit_boss:.2f} para derrotar {boss_usuario}')
                    tentativa_boss = input('Quer escolher outro boss?''\n').replace(' ', '').title()    
                    if tentativa_boss == 'Sim':
                        bosses(buff)
                    else:
                        novamente()
        while boss_usuario not in chefes:
            time.sleep(1)
            tentativa_boss = input('Esse boss não existe. Quer tentar de novo?''\n').replace(' ', '').title()
            if tentativa_boss == 'Sim':
                bosses(buff)
            else:
                novamente()
    bosses(buff) 
calculadora()
# Fim do programa. Houve um singelo agredecimento seguido do encerramento.    