preco = float(input('Digite o preço do produto:'))
p = float(input('Digite o percentual de desconto (0-100):'))

desconto = preco * (p / 100)
final = preco - desconto



print('o preçco do produto é {}. Desconto sera de {}%.'.format(preco, p))
print('valor do desconto: {}. Valor final: {}' .format(desconto, final))


km = int(input('quantos km forem precorrido'))
dias = int(input('quantos dias ele foi alugado'))

preco = 60 * dias + 0.15 * km

print('km = {}. dias: {}'. format(km, dias))
print('valor total: {}'. format(preco))

frase = input('digite uma frase:')
tam = len(frase)

frase2 = frase[:int(tam/2)]

print(frase2[-2:])

