# sisca
Sistema de Caixa

## Sincronização e comunicação entre processos
Problema: Desenvolva um sistema de caixa que atenda a vários clientes simultaneamente e que registre os pedidos de cada cliente 
em um arquivo separado. Seu programa deverá gerar um número sequencial para cada pedido. Seu programa deverá funcionar a partir de qualquer diretório. O diretório de registro dos pedidos será o diretório ".sisca" da pasta HOME do usuário que executá-lo. Seu sistema deverá executar várias instâncias (processos) e NÃO poderá ter um servidor.

Ideia básica:
1. Pretender;
2. Entrar();
3. Sair();
  
## 1. Pretender
```
Criar arquivo com PID (py:os.getpid())
prim_da_vez = Falso
enquanto não prim_da_vez:
  ler_lista_pids()
  gerar_tempo_mod_pids()
  ordenar_lista_tempo_mod_pids()
  se lista_tempo_pids[0] = os.getpid():
    prim_da_vez = Verdadeiro
```
## 2. Entrar
Executar código da região crítica.

## 3. Sair
Apagar arquivo cujo nome é `os.getpid()`

## Funções úteis para resolução do problema
* [os.getpid](https://docs.python.org/3/library/os.html?highlight=os%20getpid#os.getpid)
* [os.stat](https://docs.python.org/3/library/os.html?highlight=os%20stat#os.stat)
* [os.stat_result](https://docs.python.org/3/library/os.html?highlight=os%20stat#os.stat_result) 

O atributo `st_mtime` devolvido por *os.stat* é útil para saber a data da última modificação de conteúdo de um arquivo.

## Referências
* [Where is Tomboy data stored?](https://wiki.gnome.org/Apps/Tomboy/Directories)
* [XDG Base Directory Specification](https://wiki.gnome.org/Apps/Tomboy/Directories)
