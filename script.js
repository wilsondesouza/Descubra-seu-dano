document.addEventListener("DOMContentLoaded", function () {
    // Função para atualizar os resultados
    function atualizarLabel() {
        document.getElementById("calculoBase").textContent = calculadora.dano_base.toFixed(2);
        document.getElementById("calculoBuff").textContent = calculadora.dano_buff.toFixed(2);
        document.getElementById("calculoBoss").textContent = calculadora.hit_boss.toFixed(2);
    }

    // Função para lidar com cliques nos botões de buffs
    function buffs_function(value) {
        calculadora.buffs(value);
        atualizarLabel();
    }

    // Função para lidar com cliques nos botões de bosses
    function bosses_function(value) {
        calculadora.bosses(value);
        atualizarLabel();
    }

    // Configuração dos botões de buffs
    const buffButtons = document.querySelectorAll("#buffs .button-group button");
    buffButtons.forEach(button => {
        button.addEventListener("click", () => buffs_function(button.dataset.value));
    });

    // Configuração dos botões de bosses
    const bossButtons = document.querySelectorAll("#bosses .button-group button");
    bossButtons.forEach(button => {
        button.addEventListener("click", () => bosses_function(button.dataset.value));
    });

    // Configuração do botão de calcular dano
    const calcularDanoButton = document.getElementById("calcularDano");
    calcularDanoButton.addEventListener("click", function () {
        calculadora.dano();
        atualizarLabel();
    });

    // Configuração do botão de visitar GitHub
    const githubLink = document.getElementById("githubLink");
    githubLink.addEventListener("click", function () {
        window.open("https://github.com/wilsondesouza");
    });

    // Outras configurações e funcionalidades podem ser adicionadas aqui
});
