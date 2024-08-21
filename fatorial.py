# função de fatorial
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

# programa principal
if __name__ == '__main__':
    try:
       n = int(input('Informe um número inteiro positivo: '))

       if n >= 0:
           print(f'O fatorial de {n} é = {fatorial(n)} .  ')
       else:
           print(f'Não exixte fatorial de {n} .  ')
    except:
        print('Não possivel calcular o fatorial.')
