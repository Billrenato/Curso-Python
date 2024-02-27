print('CALCULADORA')
print(' + ADIÇÃO')
print(' - subtração')
print(' * multiplicação')
print(' / divisão')
print(' qualquer outra tleca para sair')

op = input('qual operação deseja fazer?')
if op == '+' or op == '-' or  op == '*' or op == '/':
   x = int(input(' digite o primeiro valor:'))
   y = int(input(' digite o primeiro valor:'))

if( op == '+'):
   res = x + y
   input('resultado: {} + {} = {} '.format(x, y, res))
elif( op == '-'):
     res = x - y
     input('resultado: {} - {} = {} '.format(x, y, res))
elif( op == '*'):
     res = x * y
     input('resultado: {} * {} = {} '.format(x, y, res))
elif( op == '/'):
     res = x / y
     input('resultado: {} / {} = {} '.format(x, y, res))
else:
    print('invalido.')

print('encerrar')

