import random
repeticoes = int(input('Digite a quantidade de números aleatórios: '))

for i in range(1, repeticoes + 1):
    num = random.randint(1, 100)
    print(f'{i}o número aleatório {num}')
