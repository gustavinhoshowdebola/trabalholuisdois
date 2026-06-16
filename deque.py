from typing import Any, List

class Deque:
  
    def __init__(self) -> None:
        self.__data: List[Any] = []

    def __repr__(self) -> str:
        return str(self.__data)

    def is_empty(self) -> bool:
        if len(self.__data) == 0:
            return True
        else:
            return False

    def insert_first(self, valor: Any) -> None:
        self.__data.insert(0, valor)
        print("item inserido no inicio:", valor)

    def insert_last(self, valor: Any) -> None:
        self.__data.append(valor)
        print("item inserido no fim:", valor)

    def remove_first(self) -> Any:
        if self.is_empty():
            print("deque vazio, nao foi possivel remover do inicio")
        else:
            item = self.__data.pop(0)
            print("item removido do inicio:", item)
            return item

    def remove_last(self) -> Any:
        if self.is_empty():
            print("deque vazio, nao foi possivel remover do fim")
        else:
            item = self.__data.pop()
            print("item removido do fim: ", item)
            return item

    def first(self) -> Any:
        if self.is_empty():
            print("deque vazio")
        else:
            print("primeiro item: ", self.__data[0])
            return self.__data[0]

    def last(self) -> Any:
        if self.is_empty():
            print("deque vazio")
        else:
            print("ultimo item: ", self.__data[-1])
            return self.__data[-1]

    def size(self) -> int:
        print("tamanho do deque: ", len(self.__data))
        return len(self.__data)


# # teste do programa
deque = Deque()

print("deque incial: ", deque)

deque.insert_first(10)
deque.insert_last(20)
deque.insert_first(5)
deque.insert_last(30)

print("deque atual: ", deque)

deque.first()
deque.last()
deque.size()

deque.remove_first()
deque.remove_last()

print("deque atual: ", deque)

deque.insert_last(40)
deque.insert_first(1)

print("deque atual: ", deque)

deque.remove_first()
deque.remove_first()
deque.remove_first()
deque.remove_first()

deque.size()
print("deque final: ", deque)
