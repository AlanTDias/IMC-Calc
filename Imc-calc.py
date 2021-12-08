a = float(input('Insira Altura: '))
b = float(input('Insira seu peso: '))
imc = b / (a * a)
tabela = imc
if tabela < 18.5:
    print('Seu IMC está abaixo do peso')
elif tabela > 18.5 and tabela < 24.9:
    print('seu peso está normal')
elif tabela > 25 and tabela < 29.9:
    print('você está com sobre-preso')
elif tabela > 30 and tabela < 34.9:
    print('você está com Obesidade Grau 1')
elif tabela > 35 and tabela < 39.9:
    print('você está com Obesidade Grau 2')
elif tabela > 40:
    print('você está com Obesidade Grau 3 ou Mórbida')

print('seu IMC é:  {}'.format(imc))


