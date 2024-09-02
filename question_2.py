import os

def fibonacci(n):
    fib_sequence = [0, 1]

    while fib_sequence[-1] < n:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)

    if n in fib_sequence:
        return f"{n} pertence à sequência de Fibonacci."
    else:
        return f"{n} não pertence à sequência de Fibonacci."

# Solicita o número ao usuário
while True:
    try:
        print('')
        number = int(input("Informe um número inteiro ou 00 para encerrar: "))
        if number == 0:
            os.system('cls')
            print('Programa encerrado!')
            break
        result = fibonacci(number)
        print(result)

    except ValueError:
        print("Por favor, insira um número inteiro válido.")
