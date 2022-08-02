var semaforo = document.getElementById("semaforo")

var corSemaforo = 1

function setCor(cor) {
    corSemaforo = cor
    switch (cor) {
        case 1: semaforo.style.backgroundImage = "url('/assets/vermelho.png')"; break;
        case 2: semaforo.style.backgroundImage = "url('/assets/amarelo.png')"; break;
        case 3: semaforo.style.backgroundImage = "url('/assets/verde.png')"; break;
        default: semaforo.style.backgroundImage = "url('/assets/desligado.png')"; break;
    }
}

function setAuto() {
    if (corSemaforo === 4) corSemaforo = 1
    setCor(corSemaforo)
    corSemaforo++
}