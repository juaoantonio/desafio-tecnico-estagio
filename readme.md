# Resolução dos Desafios

## Questão 1: 
Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

Resolução: [fibonacci.py](fibonacci.py)

## Questão 2: 
Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

Resolução: [letter_exists.py](letter_exists.py)

## Questão 3:
Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);

Resolvendo o por meio de um somatório, temos que o resultado dessa soma é igual a 77

## Questão 4:
- a) 1, 3, 5, 7, 9
- b) 2, 4, 8, 16, 32, 64, 128
- c) 0, 1, 4, 9, 16, 25, 36, 49
- d) 4, 16, 36, 64, 100
- e) 1, 1, 2, 3, 5, 8, 13
- f) 2, 10, 12, 16, 17, 18, 19, ? (Não sei a resposta)

## Questão 5:
Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada? 

Eu começaria ligando o primeiro interruptor por alguns minutos e, depois de desligá-lo, iria até a sala das lâmpadas pela primeira vez. Lá, eu verificaria qual lâmpada está apagada mas quente ao toque, identificando assim o interruptor correspondente ao primeiro. Em seguida, voltaria e ligaria o segundo interruptor, deixando o terceiro desligado. Na segunda ida à sala das lâmpadas, verificaria que a lâmpada acesa corresponde ao segundo interruptor, e a lâmpada apagada e fria ao terceiro. Dessa forma, consigo descobrir qual interruptor controla cada lâmpada usando duas idas.