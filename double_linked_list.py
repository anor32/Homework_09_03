class Node:
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.tail = new_node
        else:
            new_node.next_node = self.head  # работа с текущей головой
            self.head.prev_node = new_node  # работа с текущей головой
        self.head = new_node
        return f"Теперь в голове узел с данными {self.head.data}"

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            # return self.insert_at_head(data)
            self.head = new_node
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
        self.tail = new_node
        return f"Теперь в хвосте узел с данными {self.tail.data}"

    def remove_from_head(self):
        removed_node = self.head
        self.head = self.head.next_node
        self.head.prev_node = None
        return f"Были удалены данные {removed_node.data} из головы списка.\nТеперь голова списка {self.head.data}"

    def remove_from_tail(self):
        removed_node = self.tail
        self.tail = self.tail.prev_node
        self.tail.next_node = None
        return f"Были удалены данные {removed_node.data} из хвоста списка.\nТеперь хвост списка {self.tail.data}"

    def print_ll_from_head(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next_node
        return "Список выведен с начала"



class DoubldeLlUpgraded(LinkedList):
    def __init__(self):
       super().__init__()
    def print_ll_from_tail(self):
        current_tail = self.tail
        while current_tail:
            print(current_tail.data)
            current_tail = current_tail.prev_node
        return "список выведен с конца"



q =DoubldeLlUpgraded()
q.insert_at_head(1)
q.insert_at_head(2)
q.insert_at_head(3)
q.print_ll_from_tail()




















