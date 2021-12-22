def inicio():
    """
    Função que dará o cabeçário do programa, foram definidas cores as linhas, cor das letras e cor de fundo porém
    só funcionarão em terminal linux ou executando direto no PyCharm.

    """
#Acima está a explicação da função, foi colocada somente para fins visuais

    print('\033[42;1;30m' + '|', '__'*20,'|'+'\033[0;0m')
    print('\033[42;1;30m' + '|', '__'*20,'|'+'\033[0;0m')
    print('\033[42;1;55m     LÓGICA DE PROGRAMAÇÃO E ALGORITMOS     \033[0;0m')
    print('\033[42;1;55m           PYTHON CRIPTOGRAFIA              \033[0;0m')
    print('\033[42;1;30m' + '|', '__'*20,'|'+'\033[0;0m')
    print('\033[42;1;30m' + '|', '__'*20,'|'+'\033[0;0m')

#Abaixo, definido o valida_int, que foi feito na Aula 5 junto ao professor Vinicius, o mesmo código foi utilizado dos meus programas anteriores.
#O que o função faz é simples, ele define um valor mínimo e máximo para que possa ser salvo na variável quando for necessário
def valida_int (pergunta, min, max):
    x = int(input(pergunta))

    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

inicio() #Lê a função início, função visual do programa.

#Inicio do Programa

while True: #Loop infinito que se encerrará conforme próxima explicação.
    try: #Tenta executar a variável "op", afim de criar um sistema para encerrar o programa com except ValueError
        op = valida_int('\n\nDigite o código de 5 dígitos (entre 10.000 e 30.000), digite qualquer caractere que não seja numérico para encerrar o programa: ',10000,30000) #Lê o número digitado pelo usuário
    except ValueError: #Caso o usuário digite algum caracter que não seja um número, ele encerrará o programa
        print('Encerrando o programa')
        break #Encerra o programa

#Os seguintes números vem da divisão (somente a parte inteira) dos números digitados pelo usuário e a partir disso foi pego o resto da divisão
    a = op // 1 % 10
    b = op // 10 % 10
    c = op // 100 % 10
    d = op // 1000 % 10
    e = op // 10000 % 10

#Aqui está o peso de cada número, o primeiro pesa 2, o segundo 3, terceiro 4, quarto 5 e o quinto 6, a partir disso foi feita a multiplicação com os números
    mult5 = (e * 6)
    mult4 = (d * 5)
    mult3 = (c * 4)
    mult2 = (b * 3)
    mult1 = (a * 2)

#O seguinte valor é a soma de todos os valores acima, que servirá para darmos o codigo abaixo
    soma = mult1 + mult2 + mult3 + mult4 + mult5

#Codigo de validação do número, é a soma e o MOD de 7 conforme estabelecido pelo enunciado do exercício
    codigo = soma % 7

#Abaixo os prints com o resultado e uma explicação que eu resolvi deixar na tela para o usuário, de maneira visual mais clara e bem contextualizado.
    print('\nCódigo de validação: ' + '\033[42;1;30m', op,'-',codigo, '\033[0;0m')

    print('Fórmula:')
    print('Os seguintes números vem da divisão (somente a parte inteira) dos números digitados por você acima  e a partir disso foi pego o resto da divisão,\no resultado é: ' + '\033[42;1;30m', a, b, c, d, e, '\033[0;0m')
    print('Aqui está o peso de cada número, o primeiro pesa 2, o segundo 3, terceiro 4, quarto 5 e o quinto 6, a partir disso foi feita a multiplicação\ncom os números acima que resultaram no seguinte:  ' + '\033[42;1;30m',mult1, mult2, mult3, mult4, mult5, '\033[0;0m')
    print('O seguinte valor é a soma de todos os valores acima, que servirá para darmos o dígito abaixo ' + '\033[42;1;30m', soma, '\033[0;0m')
    print('O dígito que valida o código digitado foi feito com o resto da divisão por 7 (fórmula) dos valores acima, que resultou no seguinte número: ' + '\033[42;1;30m', codigo, '\033[0;0m')
    continue #reinicia o código, para que o usuário possa digitar mais números, fiz por conta