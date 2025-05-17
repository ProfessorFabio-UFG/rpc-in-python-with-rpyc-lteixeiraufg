# import rpyc
# from constRPYC import * #-
# from rpyc.utils.server import ThreadedServer

# class DBList(rpyc.Service):
#   value = []

#   def exposed_append(self, data):
#     self.value = self.value + [data]
#     return self.value

#   def exposed_value(self):
#     return self.value

# if __name__ == "__main__":
#   server = ThreadedServer(DBList(), port = PORT)
#   server.start()

import rpyc
from constRPYC import *
from rpyc.utils.server import ThreadedServer

class DBList(rpyc.Service):
    value = []

    def exposed_append(self, data):
        self.value = self.value + [data]
        return self.value

    def exposed_value(self):
        return self.value

    def exposed_clear(self):
        self.value = []
        return self.value

    def exposed_get(self, index):
        try:
            return self.value[index]
        except IndexError:
            return f"Erro: índice {index} fora do alcance"

    def exposed_remove(self, val):
        try:
            self.value.remove(val)
            return self.value
        except ValueError:
            return f"Erro: valor {val} não encontrado na lista"

    def exposed_length(self):
        return len(self.value)

if __name__ == "__main__":
    server = ThreadedServer(DBList(), port=PORT)
    server.start()
