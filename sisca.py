#!/usr/bin/env python3
# ^
# A primeira linha se chama "shebang"
# Para saber mais:
#   https://pt.wikipedia.org/wiki/Shebang
#   https://en.wikipedia.org/wiki/Shebang_(Unix)
#   https://docs.python.org/3/using/windows.html#shebang-lines

import os

def registrar_pedido(nome: str, pedido: str, no_pedido: int):
    arq_cliente = open(f'{nome}.ped', 'a')
    # Código de sincronização
    arq_cliente.close()

def atender_pedido():
    nome = input('Entre com seu nome: ')
    while nome:
        pedido = input('Qual o seu pedido?')
        # no_pedido = ?
        # registrar_pedido(nome, pedido, no_pedido)
        nome = input('Entre com seu nome: ')
    

def conf_inicial():
    home = os.path.expanduser('~')
    dir_sisca = os.path.join(home, '.sisca')
    if not os.path.exists(dir_sisca):
        os.mkdir(dir_sisca)
        
    os.chdir(dir_sisca)

def principal():
    conf_inicial()
    atender_pedido()
    pass

if __name__ == '__main__':
    principal()
