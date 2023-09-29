from random import randint
from time import sleep

def sortea(repeticao, lista):
    print(f"Sorteando {repeticao} valores da lista: ", end='')
    for cont in range(0, int(repeticao)):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end= " ", flush=True)
        sleep(0.5)
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')

repeticao = input("Quantos numeros quer sortear ?")
numeros = []
sortea(repeticao, numeros)
somaPar(numeros)