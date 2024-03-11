# Programa feito com a intenção de calcular e  descobrir o dano causado por cada personagem do DST
import time
print ('"Jogatina dos Puto" apresenta...')
time.sleep (0.6)

# Espaço dos Dicionários #
chars = {'Wendy', 'Wes','Wigfrid', 'Wolfgang', 'Wilson', 'Willow', 'Wx-78', 'Wickerbottom', 'Woodie', 'Maxwell', 'Webber', 'Winona', 'Warly', 'Wortox', 'Wormwood', 'Wurt', 'Walter', 'Wanda'}
weapon = {'Spear': 34, 'Tentacle Spear': 51, 'Ham Bat': 59.5, 'Dart': 100, 'Boomerang': 27.2, 'Tail Three Cats': 27.2, 'Morning Star': 43.35, 'Battle Spear': 42.5, 'Trusty Slingshot': (17,34,51)}
multiplicador = {'Wendy': 0.75, 'Wes': .75, 'Wigfrid': 1.25, 'Wolfgang': 2.00, 'Wilson': 1.00, 'Willow': 1.00, 'Wx-78': 1.00, 'Wickerbottom': 1.00, 'Woodie': 1.00, 'Maxwell': 1.00, 'Webber': 1.00, 'Winona': 1.00, 'Warly': 1.00, 'Wortox': 1.00, 'Wurt': 1.00, 'Walter': 1.00, 'Wanda': 1.00}
pt_br = {'Lança': 'Spear', 'Lança De Tentáculo': 'Tentacle Spear', 'Dardo': 'Dart', 'Bumerangue': 'Boomerang', 'Cauda': 'Tail Three Cats', 'Estrela Da Manhã': 'Morning Star', 'Lança De Batalha': 'Battle Spear', 'Estilingue': 'Trusty Slingshot'}
# Espaço dos Dicionários #

print ('Quanto de dano cada personagem do capeta causaria nos mobs - Dont Starve Together')
time.sleep (0.6)

def personagem():
    global personagem_jogado
    personagem_jogado = input('Com qual personagem do capeta você está jogando?''\n').replace(' ', '').title()
    time.sleep(0.6)
    if personagem_jogado in chars:
        print('Sério que você escolheu o %s? Espero que saiba o que está fazendo.' %personagem_jogado)
    else:
        print('Coloque um personagem jogável')
        time.sleep (0.6)
while True:
    personagem()
    if personagem_jogado in chars:
        break
    elif personagem_jogado not in chars:
        tentativa = input('Quer tentar de novo?''\n').replace(' ', '').title()
        if tentativa == 'Não':
            print('Ok. Tchau')
            time.sleep (0.6)
            quit()

time.sleep(0.6)
def arma():
    global arma_usada
    arma_usada = input('Qual arma você está usando?''\n').replace(' ', '').title()
    time.sleep(0.6)
    if arma_usada in pt_br:
        print('Logo  a %s? Tinha arma melhor não?' %arma_usada)
    else:
        print('Essa arma não existe ou eu não a conheço. Tente alguma outra')
        time.sleep (0.6)
while True:
    arma()
    arma_usada not in pt_br
    tentativa = input('Quer tentar de novo?''\n').replace(' ', '').title()
    if tentativa == 'Não':
        print('Ok. Tchau')
        time.sleep (0.6)
        break
        quit()

dano_base = weapon * multiplicador
print ('Seu dano base é %d.' %dano_base)
time.sleep (0.6)

def buffs():
    print('Existem dois buffs de comida que podem complementar o dano causado: Volt Goat Chaud-Froid e Chili Flakes')
    time.sleep(0.6)
    global pergunta_buff
    pergunta_buff = input('Qual buff você quer ver aplicado sobre o seu dano? (void, chili ou ambos)?').replace(' ', '').title()
    if pergunta_buff == 'Void':
        void = dano_base * 1.5
        void2 = dano_base * 2.5
        print('Seu dano com a Volt Goat Chaud-Froid é {0}, e se o mob estiver "Wet", você causará {1}'.format(void, void2))
    elif pergunta_buff == 'Chili':
        chili = dano_base * 1.2
        print('Seu dano com o buff da Chili Flakes passa a ser de %d.' %chili)
    elif pergunta_buff == "Ambos":
        ambos = (dano_base * 1.5) * 1.2
        ambos2 = dano_base * 3.0
        print('Seu dano com os dois buffs será de {0}, e {1} se o mob estiver "Wet'.format(ambos, ambos2))

print('Obrigado por usar a calculadora de dano da "Jogatina dos Puto"')