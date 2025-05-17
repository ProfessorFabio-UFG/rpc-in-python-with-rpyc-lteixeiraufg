[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/i7KUR3a2)
### Overview

This example illustrates RPC in Python using the RPyC library (https://rpyc.readthedocs.io/).

It consists of a server that exposes two remotely accessible procedures used to manipulate a list:

- value(): returns the current value of the list (its elements)
- append(): adds a new element to the end of the list

### Before running the example, you need to install the RPyC library:

Do the following on the two machines (AWS EC2 instances) that you will use for this activity:

    sudo apt update
    sudo apt install python3-rpyc

### Then edit the constRPYC.py file to use the IP address of the machine where you will run the server:

Also make sure it is using one of the ports left open for incoming TCP connections on the firewall (security group), such as 5678

### Then run the server on one machine

    python3 server.py

(and leave it running)

### Then run the client on the other machine

    python3 client.py

### Now add other remote procedures to the server and change the client to test them

You may add the same remote procedures that you added in the sockets activity.


-----------------------------------------------------------------------------------------------------------------------------------------

saída atual:

Lista inicial: []
O cliente conecta ao servidor e verifica que a lista começa vazia.

Após adicionar [5, 10, 15]: [5, 10, 15]
O cliente adiciona três números à lista remota, que agora contém [5, 10, 15].

Tamanho da lista: 3
O cliente consulta o tamanho da lista, que tem 3 elementos.

Valor no índice 1: 10
O cliente acessa o valor na posição 1 da lista (que é 10).

Valor no índice 5 (fora do alcance): Erro: índice 5 fora do alcance
O cliente tenta acessar um índice inexistente, e o servidor retorna uma mensagem de erro amigável.

Removendo 10: [5, 15]
O cliente remove o valor 10 da lista com sucesso.

Tentando remover 100 (não existe): Erro: valor 100 não encontrado na lista
O cliente tenta remover um valor que não está na lista, e o servidor retorna uma mensagem de erro.

Lista antes de limpar: [5, 15]
O cliente mostra o estado atual da lista antes de limpá-la.

Limpando lista: []
A lista é esvaziada remotamente pelo cliente.

Lista final: []
O cliente confirma que a lista agora está vazia.
