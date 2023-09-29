from time import sleep

def contagem(i, f, p):
    print("-=" * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')

    if i <= f:
        cont = i
        while cont <= f:
            sleep(0.5)
            print(cont, end=" ", flush=True)
            cont += p
        print("FIM")
    else: 
        cont = i
        while cont >= f:
            sleep(0.5)
            print(cont, end=" ", flush=True)
            cont -= p
        print("FIM")


contagem(1, 10, 1)
contagem(10, 0, 1)
print("-=" * 20)
print("Agora é sua vez de personalizar a contagem!")
inicio = int(input("Início: "))
final = int(input("Fim: "))
inter = int(input("Passo: "))
contagem(inicio, final, inter)
