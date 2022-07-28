import React, { useState } from 'react';
import Linha from './Linha';

import { Container, ContCalculadora, Title, Form, Botao, Table, Resultados, Top, Bottom, Criador } from './styles';

function App() {
  const [altura, setAltura] = useState()
  const [peso, setPeso] = useState()
  const [imc, setImc] = useState()

  const calcular = (e) => {
    if (!peso || !altura) {
      alert("Dados Não Fornecidos corretamente!")
      return
    }
    setImc((peso / (altura * altura)).toFixed(2))
  }

  return (
    <Container>
      <ContCalculadora>
        <Title>Calculadora de IMC</Title>

        <Form>
          <input required onChange={e => setAltura(e.target.value)} min="0" type="number" placeholder='Altura (m)'/>
          <input required onChange={e => setPeso(e.target.value)} min="0" type="number" placeholder='Peso (kg)'/>
        </Form>
        <Botao onClick={calcular}>Calcular</Botao>

        {imc
        ?<Resultados>
            <Top>
              <h2>Seu IMC é: </h2>
              <span>{imc}</span>
            </Top>
            <Bottom>
              <p>Sua Classificação é:</p> 
              <span>{
                imc < 18.5 ? "Abaixo do Peso" : imc < 24.9 ? "Peso Normal" : imc < 29.9 ? "Acima do Peso (Sobrepeso)" : imc < 34.9 ? "Obesidade I" : imc < 39.9 ? "Obesidade II" : "Obesidade III"
              }</span>
            </Bottom>
        </Resultados>

        :<Table>
        <thead>
          <tr>
            <th>IMC</th>
            <th>Classificação</th>
          </tr>
        </thead>
        <tbody>
          <Linha elements={["Menor do que 18,5", "Abaixo do peso"]}/>
          <Linha elements={["Entre 18,5 e 24,9", 	"Peso normal"]}/>
          <Linha elements={["Entre 25 e 29,9", 	"Acima do peso (sobrepeso)"]}/>
          <Linha elements={["Entre 30 e 34,9", 	"Obesidade I"]}/>
          <Linha elements={["Entre 35 e 39,9", 	"Obesidade II"]}/>
          <Linha elements={["Maior do que 40", 	"Obesidade III"]}/>
        </tbody>
      </Table>
        }
      </ContCalculadora>
      <Criador>Vinicius Guedes</Criador>
    </Container>
  );
}

export default App;
