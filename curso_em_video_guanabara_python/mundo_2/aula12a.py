name = str(input('Qual é o seu nome? '))
colors = {'clear': '\033[m',
          'bluesublime': '\033[4;34m'}

if name == 'Rafael':
    print('Bom dia, {}Chefe{}!!!'.format(colors['bluesublime'], colors['clear']))
elif name == 'Pedro' or name == 'Maria' or name == 'Paulo':
    print('Bom dia, seu nome é bem popular no Brasil!')
elif name in 'Ana Cláudia Jéssica Juliana':
    print('Bom dia, você tem um nome bonito!')
else:
    print('Bom dia, você tem um nome bem comum')
