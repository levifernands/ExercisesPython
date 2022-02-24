#Obtenha a idade de um individuo a partir da data do seu nascimento, mostrando quantos anos, meses
#e dias o indivíduo possui atualmente.

'''
TESTEE

anoNasc = int(input("Qual o ano de nascimento do individuo? [AAAA]: "))
anoAtual = int(input("Digite o ano atual[AAAA]: "))

idade = anoAtual - anoNasc

print(f'O indivíduo nasceu no ano {anoNasc}')

print(f'Logo, o indivíduo possui {idade} anos no ano de {anoAtual}')
'''

from datetime import date


diaNasc = int(input("Qual o dia que o invidíduo nasceu? [DD] "))
mesNasc = int(input("Qual o mês que o invidíduo nasceu? [MM] "))
anoNasc = int(input("Qual o ano que o invidíduo nasceu? [AAAA] "))

dataNasc = [diaNasc, mesNasc, anoNasc]



ano = 365

dataAtual = date.today()
diaAtual = int(dataAtual.strftime("%d"))
mesAtual = int(dataAtual.strftime("%m"))
anoAtual = int(dataAtual.strftime("%Y"))

d1 = dataAtual.strftime("%d/%m/%Y")

print(f'Hoje é {d1}')

idade = anoAtual - anoNasc

age = anoAtual - anoNasc - ((mesAtual, diaAtual) < (mesNasc, diaNasc))


print(f'Logo, o indivíduo possui {age} anos no ano de {anoAtual}.')
