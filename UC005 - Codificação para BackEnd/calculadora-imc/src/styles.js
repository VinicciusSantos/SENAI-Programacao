import styled from "styled-components";

export const Container = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  background-image: radial-gradient(
    circle at 50% -20.71%,
    #edf3ff 0,
    #b5c9f2 50%,
    #79a1e2 100%
  );

  width: 100vw;
  height: 100vh;
`;

export const ContCalculadora = styled.div`
  background-color: white;
  width: 500px;
  height: 390px;

  border-radius: 15px;
  box-shadow: 4px 4px 4px rgba(0, 0, 0, 0.05);

  padding: 20px 10px 30px;

  display: flex;
  flex-direction: column;
  align-items: center;
`;

export const Title = styled.h1`
  width: 100%;
  text-align: center;
  margin-bottom: 10px;
  color: rgba(0, 0, 0, 0.8);
`;

export const Form = styled.form`
  width: 100%;
  display: flex;
  align-items: center;
  flex-direction: column;

  > input {
    margin: 5px;
    width: 80%;
    border-radius: 20px;
    padding: 5px 10px;
    border: 1px solid rgba(0, 0, 0, 0.5);
  }
`;

export const Botao = styled.button`
    margin-top: 10px;
    border-radius: 20px;
    width: 80%;
    padding: 5px;
    background-color: #79a1e2;
    color: white;
    border: none;
    transition: .2s;

    &:hover {
        background-color: #5b87ce;
        transition: .2s;
    }
`;

export const Table = styled.table`
    margin-top: 20px;
    border-radius: 10px;
    width: 80%;
    height: 100px;
    border: 1px solid rgba(0, 0, 0, 0.8);

    >tbody {
        text-align: center;
        font-size: 15px;
        color: rgba(0, 0, 0, 0.8);
    }
`; 

export const Resultados = styled.div`
    margin-top: 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
`;

export const Top = styled.div`
    color: rgba(0, 0, 0, 0.8);
    display: flex;
    align-items: center;

    > h2 {
        font-size: 25px;
        font-weight: bold;
        margin-right: 10px;
    }

    > span {
        font-size: 25px;
        font-weight: bold;
        color: #79a1e2;
    }
`;

export const Bottom = styled.div`
    color: rgba(0, 0, 0, 0.8);
    display: flex;
    align-items: center;

    > p {
        margin-right: 10px;
    }
`;

export const Criador = styled.div`
    color: white;
    position: fixed;
    bottom: 5px;
`;