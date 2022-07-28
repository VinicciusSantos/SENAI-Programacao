let display = document.getElementById("displayNums")

// Nessas listas serão armazenados os valores passados pelo usuário
let nums = []
let operadores = []

let completeString = ""     // Aqui ficará a string completa que vai aparecer no display
let tempNum = ""            // Aqui eu guardo os números temporariamente pra trasformar eles de string para float


// Para cada botão númerico apertado, essa função grava em tempNUm os numeros até vir um operador
// Quando um operador chega, sabemos que o numero acabou
function addNum(num) {
    tempNum += num
    completeString += num

    display.innerText = completeString
}


// Essa função grava o numero que estava guardado em tempNum e grava o operador em operadores[]
function operador(op) {
    // Primeiro ele finaliza o numero digitado
    if (tempNum != "") {
        nums.push(parseFloat(tempNum)) 
        tempNum = ""
    }

    operadores.push(op)
    completeString += op
    display.innerText = completeString
}


// Função cham
function calcular() {
    // verificando se tem algum numero pra calcular
    if (nums.length == 0 || nums.length != operadores.length) {
        display.innerText = "Erro!";
        completeString = ""
        tempNum = ""
        return;
    }

    // Primeiro ele finaliza o numero digitado
    nums.push(parseFloat(tempNum)) 
    tempNum = ""

    // Percorrendo as listas e fazendo os calculos
    let resultado = nums[0]
    for (let i = 0; i < nums.length; i++) {
        switch (operadores[i]) {
            case '+': resultado += nums[i+1]; break;
            case '-': resultado -= nums[i+1]; break;
            case '/': resultado /= nums[i+1]; break;
            case 'x': resultado *= nums[i+1]; break;
        }
    }

    // Limpando as listas
    nums = []
    operadores = []

    nums.push(resultado)
    completeString += `=${resultado}`
    display.innerText = completeString
}

// Reseta tudo
function apagar() {
    completeString = ""
    tempNum = ""   
    nums = []
    operadores = []

    display.innerText = "Calculadora"
}