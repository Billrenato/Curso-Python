print('Olá, mundo!')

print( )

nota =  8.5
diciplina = "matematica"
print(nota)
print(diciplina)

print('Diciplina:',diciplina,'.nota:',nota)



a = 1 #a recebe 1 
b = 5 #b recebe 5

resposta = a == b
print(resposta)

nota = 8.5
s1 = 'vc tirou %f na diciplina' % nota 
print(s1)

nota = 8.5
s1 = 'vc tirou %.1f na diciplina' % nota 
print(s1)

nota = 8.5
diciplina = 'matematica'
s1 = 'vc tirou %.1f na diciplina %s' % (nota,diciplina)
print(s1)

nota = 8.5
diciplina = 'matematica'
s1 = 'vc tirou {} na diciplina {}' .format(nota,diciplina)
print(s1)

s1 = 'Logica de programação e Algoritimos'
print(s1[0:6])

s1 = 'Logica de programação e Algoritimos'
print(s1[24:34])

s1 = 'Logica de programação e Algoritimos'
print(s1[:22])

s1 = 'Logica de programação e Algoritimos'
tamanho = len(s1)
print(tamanho)


<a name="machine-learning-examples"></a>

## Exemplos de machine learning

#Para ver exemplos completos das análises interativas de machine learning possibilitadas pelo Colaboratory, confira estes tutoriais que usam modelos do <a href="https://tfhub.dev">TensorFlow Hub</a>.

#Vejas alguns exemplos:

#<a href="https://tensorflow.org/hub/tutorials/tf2_image_retraining">Treinar novamente um classificador de imagens</a>: crie um modelo do Keras com base em um classificador de imagens pré-treinado para distinguir flores.
#<a href="https://tensorflow.org/hub/tutorials/tf2_text_classification">Classificação de texto</a>: classifique avaliações de filmes do IMDB como <em>positivas</em> ou <em>negativas</em>.
#<a href="https://tensorflow.org/hub/tutorials/tf2_arbitrary_image_stylization">Transferência de estilo</a>: use o aprendizado profundo para transferir o estilo entre imagens.
#<a href="https://tensorflow.org/hub/tutorials/retrieval_with_tf_hub_universal_encoder_qa">Perguntas e respostas sobre o codificador de frases universais multilíngue</a>: use um modelo de machine learning para responder a perguntas do conjunto de dados SQuAD.
#<a href="https://tensorflow.org/hub/tutorials/tweening_conv3d">Interpolação de vídeo</a>: preveja o que aconteceu em um vídeo entre o primeiro e o último frames.


nome = input('qual e sau nome? ')
print('Olá {}, seja bem vindo!' .format(nome))

nota = int(input('qula a sua nota? '))
print('voce tirou nota {}'.format(nota))

x = int(input('Digite um numero inteiro: '))
y = int(input('Digite um numero inteiro: '))
res = 'o resultado da soma de {} com o {} é {}.'.format(x,y,x+y)
print(res) 

x = int(input('Digite um numero inteiro: '))
y = int(input('Digite um numero inteiro: '))
res = 'o resultado da soma de %i com o %i é %i.' % (x,y,x+y)
print(res)

idade = input('qual sua idade?')
print(idade)