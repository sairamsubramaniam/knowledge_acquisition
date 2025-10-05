# Linked List

from typing import Optional



class Node:

    def __init__(self, data: int, next_node: Optional[Node]) -> None:
        self.data = data
        self.next_node = next_node



class LinkedList:

    def __init__(self, node: Optional[Node] = None) -> None:
        self.head = node
        self.total_nodes = 0 if not node else 1


    def get_by_index(self, index: int) -> Optional[Node]:
        position_counter = 1
        current_node = self.head
        while position_counter <= index:
            current_node = current_node.next_node
            position_counter += 1
        return current_node



    def add_node(self, new_node: Node, position: int) -> None:
        if position == 0:
            node_to_be_replaced = self.head
            self.head = new_node
            if node_to_be_replaced:
                self.head.next_node = node_to_be_replaced
        elif position >= self.total_nodes:
            last_node = self.get_by_index(self.total_nodes-1)
            last_node.next_node = new_node
        else:
            before_position = position - 1
            prev_node = self.get_by_index(before_position)
            node_at_position = self.get_by_index(position)
            prev_node.next_node = new_node
            new_node.next_node = node_at_position


        self.total_nodes += 1


    def delete_node(self, index: int) -> Node:
        if self.head is None:
            raise Exception(f"There are no nodes in this linked list yet! So, nothing can be deleted.")
        elif position >= self.total_nodes:
            raise Exception(f"Total elements in this linked list is {self.total_nodes}. There is no element at {index} for deleting")
        else:
            node_index_minus_one = None if self.total_nodes == 1 else self.get_by_index(index-1)
            node_index_plus_one = None if (self.total_nodes-1) == index else self.get_by_index(index+1)
            node_index = self.get_by_index(index)

            if self.total_nodes == 1:
                self.head = None
                self.total_nodes = 0
                return self.head

            if not node_index_minus_one:
                self.head = node_index.next_node
            elif not node_index_plus_one:
                node_index_minus_one.next_node = None
            else:
                node_index_minus_one.next_node = node_index_plus_one

            self.total_nodes -= 1
            return node_index



    def __len__(self):
        return self.total_nodes



