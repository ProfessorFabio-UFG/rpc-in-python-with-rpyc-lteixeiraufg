# import rpyc
# from constRPYC import * #-

# class Client:
#   conn = rpyc.connect(SERVER, PORT) # Connect to the server
#   print (conn.root.exposed_value())
#   conn.root.exposed_append(5)       # Call an exposed operation,
#   conn.root.exposed_append(6)       # and append two elements
#   print (conn.root.exposed_value())   # Print the result


import rpyc
from constRPYC import *

class Client:
    conn = rpyc.connect(SERVER, PORT)

    print("Lista inicial:", conn.root.exposed_value())

    conn.root.exposed_append(5)
    conn.root.exposed_append(10)
    conn.root.exposed_append(15)
    print("Após adicionar [5, 10, 15]:", conn.root.exposed_value())

    print("Tamanho da lista:", conn.root.exposed_length())

    print("Valor no índice 1:", conn.root.exposed_get(1))
    print("Valor no índice 5 (fora do alcance):", conn.root.exposed_get(5))

    print("Removendo 10:", conn.root.exposed_remove(10))
    print("Tentando remover 100 (não existe):", conn.root.exposed_remove(100))

    print("Lista antes de limpar:", conn.root.exposed_value())
    print("Limpando lista:", conn.root.exposed_clear())
    print("Lista final:", conn.root.exposed_value())
