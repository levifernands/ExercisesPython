#   MATRIZES

'''matriz = [[5, 10 , 15, 20],[25, 30, 35, 40], [45, 50, 55, 60]]

print(matriz)
print("--"*50)

print(matriz[0],[2])'''

'''matriz = [[1,2,3],[4,5,6],[7,8,9]]


for i in range(0,3):
    for j in range(0,3):
        print("linha ", i, "Coluna ", j, "=", matriz[i][j])'''

#Em uma matriz 3x3, solicite ao usuário digitar os elementos da matriz, e ao final, ordene do menor para o maior (ordem crescente)
#OBS: Utilizar IF-ELSE, While, for e input

'''lista = []
for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista o elemento digitado...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Foi adicionado este elemento na posição {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')'''


#2. Numa matriz 3x3, solicite ao usuário digitar os elementos. Identifiqque os impares e some.
#OBS: Utilize While, IF-ELSE, Operação Aritmética, Input


'''num = int(input("Digite um numero: "))
total = 0

if (num % 2) == 0:
   print(num, "é um número par")
else:
   print(num, "é um número ímpar")

for num in range(1, maximo + 1):
    if (num % 2 == 0):
        print("{0}".format(num))
        total = total + num'''


lista = []
linha = []

numeroColuna = int(input('Quantas colunas? '))
numeroLinha = int(input('Quantas linhas? '))

for c in range(0, numeroLinha):
    lista.append(linha)
for c1 in range(0, numeroLinha):
    for c2 in range(0, numeroColuna):
        n = int(input(f'Número Linha[{c1+1}] Coluna[{c2+1}]: '))
        lista[c1].append(n)
print(lista)
