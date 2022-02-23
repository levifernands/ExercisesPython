#Faça um algoritmo que faça conversão do kelvin(K) para graus celsius(°C).
#Obs: faça uma análise em qual estado o elemento *Mercúrio" está.
'''
Dados:
    Hg < -273.14°C -> CONDENSADO DE BOSE-EINSTEIN
    Hg < -38.8°C -> SÓLIDO
    Hg > -38.8°C and Hg < 1538°C -> LÍQUIDO
    Hg > 1538°c -> GASOSO
    Hg > 10,000°C -> PLASMA
    '''

escolha = int(input("Digite O valor em Kelvin() do Hg para converter para graus Celsius(°C): "))
C = (escolha - 273.15)

print("o valor em Celsius é:", C,"°C")

if C < -273.14:
    print("O elemento atual (Hg) se encontra na fase CONDENSADO DE BOSE-EINSTEIN")
elif C < -38.8:
    print("O elemento atual (Hg) se encontra na fase SÓLIDA")
elif C > -38.8 and C < 1538 :
    print("O elemento atual (Hg) se encontra na fase LÍQUIDA")
elif C > 1538 :
    print("O elemento atual (Hg) se encontra na fase GASOSA")
elif C > 10000 :
    print("O elemento atual (Hg) se encontra como PLASMA")




#Faça um simulador de reajuste de um salário. Com salário anterior, o valor do reajuste e valor final atualizado.
#OBS: Peça para digitar o salário inicial e o percentual do reajuste.
