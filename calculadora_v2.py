def adicao(a, b):
    return a + b
    
def subtracao(a, b):
    return a - b
    
def multiplicacao(a, b):
    return a * b
    
def divisao(a, b):
    if b == 0:
        return 'Não foi possivel realizar a divisão por 0'
        
    return a / b
    
def calculadora(operacao, num1, num2):
    if operacao == 'adicao' or operacao == '+':
        return adicao(num1, num2)
    elif operacao == 'subtracao' or operacao == '-':
        return subtracao(num1, num2)
    elif operacao == 'multiplicacao' or operacao == '*':
        return multiplicacao(num1, num2)
    elif operacao == 'divisao' or operacao == '/':
        return divisao(num1, num2)
    else:
        return "Operação inválida"
        
saida = ""
while saida != 'n' and saida != 'N':
    operacao = input('Qual operação você deseja realizar? (adicao, subtracao, multiplicacao, divisao)')
    num1 = float(input('Primeiro numero: '))
    num2 = float(input('Segundo numero: '))
    resultado = calculadora(operacao, num1, num2)
    print('Sua resposta é: ' + str(resultado))
    print('---------')
    saida = input('Você deseja continuar? (s/n): ')