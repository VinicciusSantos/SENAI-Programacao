var lampadas = [document.getElementById("l3"), document.getElementById("l2"), document.getElementById("l1")]
var aceso = 0
var automatico = false

function acender(lampada){
    if (lampada.style.opacity == '1')
    lampada.style.opacity = '.6'
    else
    lampada.style.opacity = '1'
}

function troca(){
    if (automatico) automatico = false
    else {
        automatico = true
        aceso = 0
    }

    // while (automatico) {
    //     // lampadas[aceso].style.opacity = '1'
    //     // lampadas[aceso].style.opacity = '.6'
    //     console.log(aceso)

    //     aceso++
    //     if (aceso === 3) aceso = 0
    // }
}
