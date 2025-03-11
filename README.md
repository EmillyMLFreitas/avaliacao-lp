# Avaliação de Linguagem de Programação e Processamento da Informação


Conteúdo: Introdução à algorítmos e lógica de programação em Python

_Essa é uma versão adaptada de uma avaliação que tive na FATEC Carapicuiba, onde o conteúdo inicial era POO._

---
Crie um programa em Python e peça para que o usuário digite os seguintes atributos e salva-las em variáveis:

- Nome;
- Data de nascimento;
- Peso;
- % de Gordura corporal (Valor inteiro);

---
Crie duas funções: **imprimirPaciente** (para imprimir os dados do usuário) e **verificarSituacao**. A função verificarSituacao deve considerar a variável gordura corporal para informar / imprimir a condição do paciente utilizando as seguintes probabilidades:

- Muito Magro: Menos de 5% de gordura corporal;
- Magro, abaixo do peso: De 6 a 15% de gordura corporal;
- Peso ideal: De 16 a 25% de gordura corporal;
- Acima do peso: De 26 a 35% de gordura corporal;
- Obeso: Acima de 36% de gordura corporal;

A função **imprimirPaciente** deve mostrar em tela a seguinte estrutura:

```
-- Paciente N (posição no array + 1) --
Nome: 
Data de Nasc:
Peso:
Gordura Corporal (%):
```

--- 
Salve as informações do paciente em um array de pacientes, crie uma função **procuraPaciente** que receba por parâmetro o número do paciente e retorna o paciente que está na posição N-1.

Exemplo: O usuário deseja verificar o paciente de número 1. A função deve retornar o paciente que está na primeira posição do array.

---
Utilize um loop while para mostrar um menu de opções para o usuário seguindo o modelo a seguir:

1. Imprimir dados do Paciente
2. Verificar situação do Paciente
3. Sair do programa

---
Extra

1. Para imprimir os dados do paciente, deve se utilizar a função **imprimirPaciente** e função **procuraPaciente**

2. Para verificar a situação do paciente, deve se utilizar a função **verificarSituacao** e função **procuraPaciente**

3. Se caso for necessário, pode se utilizar _dicionários_ ou _matrizes_. Se for utilizar matrizes, opte pela seguinte estrutura:

    [ nomePaciente, dataNascimento, peso, gordura ]  
