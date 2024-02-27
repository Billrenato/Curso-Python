def soma (x=0, y=0, z=0):
    """

    :param x: valor opcional
    :param y: valor opcional
    :param z:valor opcional
    """
    return x+y+z

print(soma(3,2,1))
help(soma)





def fatorial(num):
    """

    :param num:
    :return:
    """
    fat = 1
    if num == 0:
        return fat
    for i in range(1, num+1, 1):
        fat *= i
    return fat

x = int(input('digite um valor para calcular o fatorial: ' ))
print('{}! = {}'.format(x,fatorial(x)))
help(fatorial)








def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or(x > max)):
        x = int(input(pergunta))
    return x


def fatorial(num):
    """

    :param num:
    :return:
    """
    fat = 1
    if num == 0:
        return fat
    for i in range(1, num+1, 1):
        fat *= i
    return fat

x = valida_int('digite um valor para calcular o fatorial: ', 0, 99999)
print('{}! = {}'.format(x,fatorial(x)))
help(fatorial)














def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or(x > max)):
        x = int(input(pergunta))
    return x

def criararquivo(nomedoarquivo):
    try:
        a = open(nomedoarquivo, 'wt+')
        a.close()
    except:
        print('errona criacao de arquivo')
    else:
        print('arquivo {} criado com sucesso!\n'.format(nomedoarquivo))

def existearquivo(nomedoarquivo):
    try:
        a = open(nomedoarquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
def listararquivo(nomedoarquivo):
    try:
        a = open(nomedoarquivo, 'rt')
    except:
        print('erro ao ler o arquivo')
    else:
        print(a.read())

def cadastrarjogo(nomedoarquivo, nomejogo, nomedovideogame):
    try:
        a = open(nomedoarquivo, 'at')
    except:
        print('erro ao abrir')
    else:
        a.write('{};{}\n'.format(nomejogo,nomedovideogame))
    finally:
        a.close()

arquivo = 'games.txt'
if existearquivo(arquivo):
    print('arquivo localizado no pc')
else:
    print('arquivo nao existe')
    criararquivo(arquivo)


while True:
    print('menu')
    print('1 - cadastrar novo iten')
    print('2 - listar cadastro')
    print('3 - sair')

    op = valida_int('escolha a opção', 1, 3)
    if op == 1:
        print('opcao de cadastrar novo iten selecionado.....')
        nomejogo = input('nome do jogo:')
        nomedovideogame = input('nome do video game:')
        cadastrarjogo(arquivo, nomejogo, nomedovideogame)
    elif op == 2:
        print('opção de listar selecionada')
        listararquivo(arquivo)
    elif op == 3:
        print('encerrar o programa.....')
        break

