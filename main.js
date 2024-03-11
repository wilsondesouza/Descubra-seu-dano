const weaponApp = {
    'Spear': { damage: 34, imagePath: 'media/weapon/Spear.png' }, 'Tentacle Spike': { damage: 51, imagePath: 'media/weapon/Tentacle Spike.png' }, 'Ham Bat': { damage: 59.5, imagePath: 'media/weapon/Ham Bat.png' }, 'Dart': { damage: 100, imagePath: 'media/weapon/Dart.png' }, 'Boomerang': { damage: 27.2, imagePath: 'media/weapon/Boomerang.png' }, 'Tail': { damage: 27.2, imagePath: 'media/weapon/Tail.png' }, 'Morning Star': { damage: 43.35, imagePath: 'media/weapon/Morning Star.png' }, 'Battle Spear': { damage: 42.5, imagePath: 'media/weapon/Battle Spear.png' }, 'Slingshot': { damage: 51, imagePath: 'media/weapon/Slingshot.png' }, 'Dark Sword': { damage: 68, imagePath: 'media/weapon/Dark Sword.png' },
}

const multiplicadorApp = {
    'Wendy': { multiplier: 0.75, imagePath: 'media/chars/Wendy.png' }, 'Wes': { multiplier: 0.75, imagePath: 'media/chars/Wes.png' },
    'Wigfrid': { multiplier: 1.25, imagePath: 'media/chars/Wigfrid.png' }, 'Wolfgang': { multiplier: 2.00, imagePath: 'media/chars/Wolfgang.png' },
    'Wilson': { multiplier: 1.00, imagePath: 'media/chars/Wilson.png' }, 'Willow': { multiplier: 1.00, imagePath: 'media/chars/Willow.png' },
    'Wx-78': { multiplier: 1.00, imagePath: 'media/chars/Wx-78.png' }, 'Wickerbottom': { multiplier: 1.00, imagePath: 'media/chars/Wickerbottom.png' },
    'Woodie': { multiplier: 1.00, imagePath: 'media/chars/Woodie.png' }, 'Maxwell': { multiplier: 1.00, imagePath: 'media/chars/Maxwell.png' },
    'Webber': { multiplier: 1.00, imagePath: 'media/chars/Webber.png' }, 'Winona': { multiplier: 1.00, imagePath: 'media/chars/Winona.png' },
    'Warly': { multiplier: 1.00, imagePath: 'media/chars/Warly.png' }, 'Wortox': { multiplier: 1.00, imagePath: 'media/chars/Wortox.png' },
    'Wurt': { multiplier: 1.00, imagePath: 'media/chars/Wurt.png' }, 'Walter': { multiplier: 1.00, imagePath: 'media/chars/Walter.png' },
    'Wanda': { multiplier: 1.00, imagePath: 'media/chars/Wanda.png' }, 'Wormwood': { multiplier: 1.00, imagePath: 'media/chars/Wormwood.png' },
}

const chefesApp = {
    'Toadstool': { hitPoints: 99999, imagePath: 'media/bosses/Toadstool.png' }, 'Klaus': { hitPoints: 10000, imagePath: 'media/bosses/Klaus.png' }, 'KlausRevived': { hitPoints: 5000, imagePath: 'media/bosses/Klaus2.png' }, 'Eye of Terror': { hitPoints: 5000, imagePath: 'media/bosses/Eye of Terror.png' }, 'Spazmatism': { hitPoints: 10000, imagePath: 'media/bosses/Spazmatism.png' }, 'Retinazor': { hitPoints: 10000, imagePath: 'media/bosses/Retinazor.png' }, 'Celestial Champion': { hitPoints: 22500, imagePath: 'media/bosses/Celestial Champion.png' }, 'Reanimated Skeleton': { hitPoints: 16000, imagePath: 'media/bosses/Reanimated Skeleton.png' }, 'Treeguard': { hitPoints: 3750, imagePath: 'media/bosses/Treeguard.png' }, 'Ancient Guardian': { hitPoints: 2500, imagePath: 'media/bosses/Ancient Guardian.png' }, 'Antlion': { hitPoints: 6000, imagePath: 'media/bosses/Antlion.png' }, 'Bearger': { hitPoints: 6000, imagePath: 'media/bosses/Bearger.png' }, 'Bee Queen': { hitPoints: 22500, imagePath: 'media/bosses/Bee Queen.png' }, 'Deerclops': { hitPoints: 4000, imagePath: 'media/bosses/Deerclops.png' }, 'Dragonfly': { hitPoints: 2750, imagePath: 'media/bosses/Dragonfly.png' }, 'Lord of the Fruit Flies': { hitPoints: 1500, imagePath: 'media/bosses/Lord of the Fruit Flies.png' }, 'Malbatross': { hitPoints: 5000, imagePath: 'media/bosses/Malbatross.png' }, 'Moose': { hitPoints: 6000, imagePath: 'media/bosses/Moose.png' }, 'Spider Queen': { hitPoints: 2500, imagePath: 'media/bosses/Spider Queen.png' }, 'Crab King': { hitPoints: 95000, imagePath: 'media/bosses/Crab King.png' }, 'Nightmare Werepig': { hitPoints: 10000, imagePath: 'media/bosses/Nightmare Werepig.png' }, 'Shadow Rook': { hitPoints: 10000, imagePath: 'media/bosses/Shadow Rook.png' }, 'Shadow Knight': { hitPoints: 8100, imagePath: 'media/bosses/Shadow Knight.png' }, 'Shadow Bishop': { hitPoints: 7500, imagePath: 'media/bosses/Shadow Bishop.png' },
}


const buffsApp = {
    'Volt': { buffValue: 2.5, imagePath: 'media/buffs/Volt.png' }, 'Ambos': { buffValue: 3, imagePath: 'media/buffs/Ambos.png' },
    'Chili': { buffValue: 1.2, imagePath: 'media/buffs/Chili.png' }
}

const fecharDialog = document.getElementById("fecharDialog");
fecharDialog.addEventListener("click", function () {
    const resultadoDialog = document.getElementById("resultadoDialog");
    resultadoDialog.style.display = "none";
});

class Calculadora {
    constructor() {
        this.personagem_jogado = "";
        this.arma_usada = "";
        this.buff = "";
        this.dano_personagem = 1;
        this.dano_arma = 1;
        this.dano_buff = 1;
        this.dano_base = 1;
        this.hit_boss = 1;
    }

    resetarValores() {
        this.personagem_jogado = "";
        this.arma_usada = "";
        this.buff = "";
        this.dano_personagem = 1;
        this.dano_arma = 1;
        this.dano_buff = 1;
        this.dano_base = 1;
        this.hit_boss = 1;
    }

    personagem(value) {
        this.personagem_jogado = value;
    }

    arma(value) {
        this.arma_usada = value;
    }

    dano() {
        if (!this.personagem_jogado || !this.arma_usada || !this.buff || !this.boss_usuario) {
            // Mostrar uma mensagem de erro ou tomar outra ação apropriada
            alert("Escolha  personagem, arma, buff e boss antes de calcular o dano.");
            return;
        }

        for (let key in multiplicadorApp) {
            if (key.startsWith(this.personagem_jogado)) {
                this.dano_personagem = multiplicadorApp[key].multiplier;
            }
        }

        for (let key in weaponApp) {
            if (key.startsWith(this.arma_usada)) {
                this.dano_arma = weaponApp[key].damage;
            }
        }
        this.dano_base = this.dano_personagem * this.dano_arma;
        this.buffs(this.buff);
        this.bosses(this.boss_usuario);
        this.atualizarResultados(this.dano_base, this.dano_buff, this.hit_boss);
    }

    buffs(value) {
        this.buff = value;
        for (let key in buffsApp) {
            if (key.startsWith(this.buff)) {
                this.dano_buff = this.dano_base * buffsApp[key].buffValue;
            }
        }
    }

    bosses(value) {
        this.boss_usuario = value;
        for (let key in chefesApp) {
            if (key.startsWith(this.boss_usuario)) {
                this.hit_boss = chefesApp[key].hitPoints / this.dano_buff;
            }
        }
    }

    atualizarResultados(dano_base, dano_buff, hit_boss) {
        const resultadoTexto = document.getElementById("resultadoTexto");
        resultadoTexto.innerHTML = `Personagem: ${this.personagem_jogado}<br>Arma: ${this.arma_usada}<br>Buff: ${this.buff}<br>Boss: ${this.boss_usuario}<br>Dano Base: ${dano_base.toFixed(2)}<br>Dano com Buff: ${dano_buff.toFixed(2)}<br>Hit to Kill: ${hit_boss.toFixed(2)}`;

        const resultadoDialog = document.getElementById("resultadoDialog");
        resultadoDialog.style.display = "block";
        calculadora.resetarValores();
    }

}

const calculadora = new Calculadora();

// Função para gerar botões para cada opção
function criarBotoes(containerId, data, clickFunction, buttonClass, imgClass) {
    const container = document.getElementById(containerId);


    for (let key in data) {
        const button = document.createElement("button");
        const img = document.createElement("img");
        img.src = data[key].imagePath;
        button.classList.add(buttonClass, 'botao-hover');
        button.appendChild(img);
        img.classList.add(imgClass);
        button.addEventListener("click", function () {
            clickFunction(key);
        });
        container.appendChild(button);
    }
}

// Configurar os botões
criarBotoes("personagemButtons", multiplicadorApp, function (value) {
    calculadora.personagem(value);
}, "personagens-button", "personagens-img");
criarBotoes("armaButtons", weaponApp, function (value) {
    calculadora.arma(value);
}, "armas-button", "armas-img");
criarBotoes("buffButtons", buffsApp, function (value) {
    calculadora.buffs(value);
}, "buffs-button", "buffs-img");
criarBotoes("bossesButtons", chefesApp, function (value) {
    calculadora.bosses(value);
}, "bosses-button", "bosses-img");


// Configurar os botões
const personagemButtons = document.querySelectorAll('.personagens-button button');
const armaButtons = document.querySelectorAll('.armas-button button');
const buffsButtons = document.querySelectorAll('.buffs-button button');
const bossesButtons = document.querySelectorAll('.bosses-button button');

// Adicione um evento de clique a cada botão 
function adicionarEventoClique(botaoLista) {
    botaoLista.forEach(button => {
        button.addEventListener('click', function() {
            botaoLista.forEach(btn => {
                btn.classList.remove('ativo-hover');
            });
            this.classList.add('ativo-hover');
        });
    });
}
adicionarEventoClique(personagemButtons);
adicionarEventoClique(armaButtons);
adicionarEventoClique(buffsButtons);
adicionarEventoClique(bossesButtons);

// Função para resetar o evento de clique dos botões
function limparAtivoHover() {
    personagemButtons.forEach(btn => {
        btn.classList.remove('ativo-hover');
    });
    armaButtons.forEach(btn => {
        btn.classList.remove('ativo-hover');
    });
    buffsButtons.forEach(btn => {
        btn.classList.remove('ativo-hover');
    });
    bossesButtons.forEach(btn => {
        btn.classList.remove('ativo-hover');
    });
}

// Configurar o botão de calcular
const calcularDanoButton = document.getElementById("calcularDano");
calcularDanoButton.addEventListener("click", function () {
    limparAtivoHover();
    calculadora.dano();
});




