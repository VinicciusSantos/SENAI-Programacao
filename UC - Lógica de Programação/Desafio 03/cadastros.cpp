#include <LiquidCrystal.h>
#include <PS2Keyboard.h>
#include <string.h>
#include <stdlib.h>
LiquidCrystal lcd(12, 11, 5, 4, 13, 10);

const int DataPin = 2;
const int IRQpin = 3;

PS2Keyboard keyboard;

int mostrando = 0;
int listar = 0;
int participantes = 0;

char nomes[15][16];
char idades[15][2];
char buscar[16];

char orig[7];
char mod[7];
char evento_data[8];
char idade_char[2];

char menu[4][10] = {"Evento", "Novo Part", "Listar", "Buscar"};

int dia_hoje = 02;
int mes_hoje = 04;
int ano_hoje = 2022;
int data_evento[3];

// Definindo os pinos digitais que serão usados:
int bt_voltar = 6;
int bt_menos = 7;
int bt_mais = 8;
int bt_enter = 9;

void setup() // Tela de Boot
{  
    keyboard.begin(DataPin, IRQpin);
    Serial.begin(9600);
    Serial.println("Teste de teclado");
   
    pinMode(bt_mais, INPUT);
    pinMode(bt_menos, INPUT);
    pinMode(bt_enter, INPUT);
    pinMode(bt_voltar, INPUT);
 
    lcd.begin(16, 2);
    lcd.print("-- Desafio 01 --");
    lcd.setCursor(0, 1);
    lcd.print("Iniciando");
    for (int i = 0; i < 3; i++)
    {
      lcd.print(".");
      delay(300);
    }
    delay(200);
    lcd.clear();
}

int mostrarMenu()
{
  mostrando = 0;
  while (1) // Mostrando o MENU
  {
      delay(200);
      lcd.clear();
      lcd.setCursor(0,0);

      // Lendo os Inputs dos botões

      int bmais = 0;
      int bmenos = 0;
      int bvoltar = 0;
      int benter = 0;
      char c = keyboard.read();
      
      if (c == PS2_DOWNARROW) bmenos = 1;
      else if (c == PS2_UPARROW) bmais = 1;
      else if (c == PS2_LEFTARROW) bvoltar = 1;
      else if (c == PS2_ENTER) benter = 1; 
      
      if (bmais == 1 && mostrando != 0) mostrando--;
      if (bmenos == 1 && mostrando != 3) mostrando++;
      if (benter == 1)
      {
        if (mostrando == 0) return 1;       // Cadastrar eventos
        else if (mostrando == 1) return 2;  // Cadastrar participantes
        else if (mostrando == 2) return 3;  // Listar participantes
        else if (mostrando == 3) return 4;  // Buscar
        }
    
        // Imprimindo o Menu
        for (int i = mostrando; i <= mostrando+1; i++)
        {         
            // Se Caso o próximo indice não exista, encerre
            if (i >= sizeof(menu)/10) break;
            
            if (mostrando == 0) // Imprimindo o cabeçalho do menu
            {
            lcd.print("  -=- MENU -=-");
            lcd.setCursor(0,1); 
            }
          
            // Mostrando os < > quando elemento selecionado e imprimindo o numero do menu
            if (mostrando == i) lcd.print("<"); else lcd.print(" ");
            lcd.print(i+1);
            if (mostrando == i) lcd.print("> - "); else lcd.print("  - ");
                    
            // Imprimindo a opção do menu (Ex: Listar, Novo Part...)
            for (int j = 0; j < strlen(menu[i]); j++)
            {
              lcd.print(menu[i][j]); 
            }
          
            // Se mostrando for 0, ele só vai imprimir uma opção, por causa do cabeçalho
            if(mostrando == 0) break;
            lcd.setCursor(0,1);
        }
    } 
}

void recebeData(int dat[3]) // Recebe um vetor para fazer o retorno por parâmetros
{
    int editando = 0;
    int dia_evento = dia_hoje;
    int mes_evento = mes_hoje;
    int ano_evento = ano_hoje;
    char molde[] = "__________";

    int cont = 0;
    while(1) // Recebendo a data do evento
    {
        char c = keyboard.read();
        if (c == PS2_ESC) return;
        delay(100);
        lcd.clear();
        if (cont == 8) break;
        
        lcd.setCursor(0,0);
        lcd.print("Digite a data:");
        lcd.setCursor(0,1);

        lcd.print("   ");
        for (int i = 0; i < cont; i++)
        {
          if (i == 2 || i == 4) lcd.print("/");
          lcd.print(evento_data[i]);            
        }

        for (int i = cont; i < 8; i++)
        {
          lcd.print(molde[i]);
        }

          
        // Lendo os Imputs dos botões
        int bmais = 0;
        int bmenos = 0;
        int bvoltar = 0;
        int benter = 0;
        if (keyboard.available())
        {
          char c = keyboard.read();
          if (c == PS2_LEFTARROW) bvoltar = 1;
          else if (c == PS2_ENTER) benter = 1;
          
          if (c == '0' || c == '1' || c == '2' || c == '3' || c == '4' || c == '5' || c == '6' || c == '7' || c == '8' || c == '9')
          {
            evento_data[cont] = c;
            cont++;
          }
        }    
    } 
}

int validaData(int data[3])
{
    // data[0] == dia do evento
    // data[1] == mes do evento
    // data[2] == ano do evento
    lcd.clear();
  
    // Verificando se o evento é em uma data posterior ou não
    if ((data[2] > ano_hoje) || (data[2] == ano_hoje && data[1] > mes_hoje) || (data[2] == ano_hoje && data[1] == mes_hoje && data[0] > dia_hoje))
    {
      lcd.print("CADASTRO FEITO!");
      delay(1000);
        return 0;
    }
    else
    {
        lcd.print("DATA INVALIDA!");
        delay(1000);
        return 1;
    }
}

int validaIdade(char idade[2]) // valida se for 18+    return 0 == legal   1 == ruim
{
    lcd.clear();
    if (idade[0] == '0') return 1;

    if (idade[0] == '1' && (idade[1] == '8' || idade[1] == '9')) return 0;
    if (idade[0] == '1') return 1;

    return 0;
}

void cadastraParticipante()
{
    delay(250);
    lcd.clear();
    int idade = 18;

    int quant_digit = 1;
    while(1) // Recebendo a idade da pessoa
    {  
        delay(250);
        char c = keyboard.read();
        lcd.setCursor(0, 0);
        lcd.print("Idade:");

        // Recebendo os inputs
        int bmais = 0;
        int bmenos = 0;
        int bvoltar = 0;
        int benter = 0;
        if (keyboard.available())
        {
          if (c == PS2_DOWNARROW) bmenos = 1;
          else if (c == PS2_UPARROW) bmais = 1;
          else if (c == PS2_ENTER) benter = 1; 
          else if (c == PS2_ESC) return;
        }

        if (bmais == 1) idade++;
        else if (bmenos == 1 && idade != 1) idade--;

        lcd.setCursor(0, 1);
        lcd.print("   <");
        for (int i = 0; i < quant_digit-1; i++) lcd.print(idade_char[i]); // imprimindo os armazenados
        if (isdigit(c))
        {
          lcd.print(c);
          idade_char[quant_digit-1] = c; // armazenando em idade_char[]
          if (quant_digit == 2)
          {
            delay(500);
            int valida = validaIdade(idade_char);
            if (valida == 1)
            {
              lcd.print("Idade Invalida");
              delay(1000);
              return;
            }
            else
            {
              lcd.print("Idade Valida");
              delay(1000);
              break;
            }
          }
          quant_digit++;
        }
        lcd.print("  anos>");
    }
  
    int quant = 0;
    while (1) // Recebendo o nome da pessoa
    {
        delay(100);
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Digite seu Nome:");

        // Recebendo os inputs
        int bmais = 0;
        int bmenos = 0;
        int bvoltar = 0;
        int benter = 0;
        
        char c = keyboard.read();
        if (c == PS2_ENTER) benter = 1;
        if (c == PS2_ESC) break; 
        if (c == PS2_BACKSPACE && quant!=0)
        {
          quant--;
        }

        // Configurando os botões

        if (bvoltar == 1) return; // Se apertar ESC

        lcd.setCursor(0, 1);

        for (int i = 0; i < quant; i++)
        {
          lcd.print(nomes[participantes][i]);
        }
        
        if (isalpha(c) || c == ' ')
        {
          lcd.print(c);
          nomes[participantes][quant] = c;
          quant++;
        }
          
        else if (benter == 1) // Se apertar enter é pq finalizou
        {   
            for (int j = 0; j < 2; j++)
              idades[participantes][j] = idade_char[j];             
            lcd.clear();
            participantes++;
            delay(100);
            return;
        }
    } 
}

void listarParticipantes()
{
  while (1) // Listando os participantes
    {
        delay(350);
        lcd.clear();
      
        // Se não tiver nenhum dado na matriz
        if (participantes == 0)
        {
            lcd.print("Sem Cadastros!");
            delay(1500);
            return;
        }

        int bmais = 0;
        int bmenos = 0;
        int bvoltar = 0;
        int benter = 0;
        if (keyboard.available())
        {
          char c = keyboard.read();
          if (c == PS2_DOWNARROW) bmenos = 1;
          else if (c == PS2_UPARROW) bmais = 1;
          else if (c == PS2_ESC) bvoltar = 1;
          else if (c == PS2_ENTER) benter = 1; 
        }

        if (bmenos == 1 && listar < participantes) listar+=2;
        else if (bmais == 1 && listar != 0) listar-=2;
        else if (benter == 1 || bvoltar == 1) break;

        lcd.setCursor(0,0);
        for (int i = listar; i < listar+2; i++)
        {
          if (i < participantes)
          {
            if (i < 9) lcd.print("0");
            lcd.print(i+1);
            lcd.print(" - ");
            for (int j = 0; j < 11; j++)
            {
              if (nomes[i][j] != NULL)
              {
                lcd.print(nomes[i][j]);
              }
            }
            lcd.setCursor(0,1);
          }
        }
    }
    delay(250);
}

void buscar_verificar() 
{
  delay(350);
  lcd.clear();    
  lcd.setCursor(0, 0);
  int escolha = 0;
  int quant = 0;
  
  while (1) // Recebendo o nome da pessoa para buscar
   {
      delay(350);
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("Digite o Nome:");

      // Recebendo os inputs
      int bmais = 0;
      int bmenos = 0;
      int bvoltar = 0;
      int benter = 0;
      
      char c = keyboard.read();
      if (c == PS2_DOWNARROW) bmenos = 1;
      else if (c == PS2_UPARROW) bmais = 1;
      else if (c == PS2_ESC) bvoltar = 1;
      else if (c == PS2_ENTER) benter = 1; 


      // Configurando os botões
      if (bvoltar == 1) return; // Se apertar ESC

      lcd.setCursor(0, 1);

      for (int i = 0; i < quant; i++)
      {
        lcd.print(buscar[i]);
      }
        
      if (isalpha(c) || c == ' ')
      {
        lcd.print(c);
        buscar[quant] = c;
        quant++;
      }
          
      if (benter == 1) // Se apertar enter é pq finalizou
      {   
          for (int j = 0; j < 2; j++) idades[participantes][j] = idade_char[j];    
          lcd.clear();
          delay(100);
          break;
      }
  }

    // percorrendo a matriz para ver se está cadastrado
    for (int i = 0; i < participantes; i++)
    {
        for (int j = 0; j < 16; j++)
        {
          if (buscar[j] != nomes[i][j]) break;
          if (j == 15)
          {
              lcd.clear();
              lcd.setCursor(0,0);
              lcd.print("Nome Encontrado");
              
              delay(1000);
              lcd.clear();
              lcd.setCursor(0,0);
              for (int k = 0; k < 16; k++)
              {
                if (nomes[i][k] != NULL)
                {
                  lcd.print(nomes[i][k]);
                }
              }

              lcd.setCursor(0,1);
              lcd.print("Idade: ");
              for (int k = 0; k < 2; k++) lcd.print(idades[i][k]);
              lcd.print(" anos");
              while (1)
              {
                delay(100);
                char c = keyboard.read();
                if (c == PS2_ENTER || c == PS2_ESC) return; 
              }
          }
        }
    }
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Nao encontrado");
    delay(1000);
}

void loop() 
{
    delay(120);
    lcd.clear();
    int adm = 0;
    adm = mostrarMenu();
    
    switch (adm)
    {
        case 1: recebeData(data_evento); break;
        case 2: cadastraParticipante(); break;
        case 3: listarParticipantes(); break;
        case 4: buscar_verificar(); break;
        //case 5: Modificar(orig, mod); break;
    }
}