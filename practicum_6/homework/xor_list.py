from __future__ import annotations
from dataclasses import dataclass
from typing import Any

import ctypes
import yaml


@dataclass
class Element:
    key: Any
    data: Any = None
    np: int = 0

    def next(self, prev):
        return self.np ^ prev

    def prev(self, next):
        return self.np ^ next

class XorDoublyLinkedList:
    def __init__(self) -> None:
        self.head: Element = None
        self.tail: Element = None
        self.nodes = []

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        node_keys = []
        next = id(self.head)
        prev = 0
        while next != 0:
            next_el = ctypes.cast(next, ctypes.py_object).value
            node_keys.append(str(next_el.key))
            prev, next = next, next_el.next(prev)

        return " <-> ".join(node_keys)

    def to_pylist(self) -> list[Any]:
        py_list = []
        next = id(self.head)
        prev = 0
        while next != 0:
            next_el = ctypes.cast(next, ctypes.py_object).value
            py_list.append(next_el.ky)
            prev, next = next, next_el.next(prev)
        return py_list

    def empty(self):
        return self.head is None

    def search(self, k: Element) -> Element:
        """Complexity: O(n)"""

        next = id(self.head)
        prev = 0
        while next != 0 and next_el.key != k.key:
            next_el = ctypes.cast(next, ctypes.py_object).value
            prev, next = next, next_el.next(prev)
        return next_el

    def insert(self, x: Element) -> None:
        """Insert to the front of the list (i.e., it is 'prepend')
        Complexity: O(1)
        """
        if self.head is None:
            self.head = x
            self.tail = x
        else:
            self.head.np = id(x) ^ self.head.np
            x.np = id(self.head)
            self.head = x
        self.nodes.append(x)

    def remove(self, x: Element) -> None:
        """Remove x from the list
        Complexity: O(n)
        """

        next = id(self.head)
        prev = 0
        next_el = ctypes.cast(next, ctypes.py_object).value
        while next != 0 and next_el.key != x.key:
            prev, next = next, next_el.next(prev)
            next_el = ctypes.cast(next, ctypes.py_object).value
        if next != 0:
            next_next = next_el.np ^ prev
            next_next_el = ctypes.cast(next_next, ctypes.py_object).value
            if prev != 0:
                prev_el = ctypes.cast(prev, ctypes.py_object).value
                prev_el.np = prev_el.np ^ next ^ next_next
            else:
                self.head = next_next_el
            if next_next != 0:
                next_next_el = ctypes.cast(next_next, ctypes.py_object).value
                next_next_el.np = next_next_el.np ^ next ^ prev
            else:
                self.tail = prev_el
            self.nodes.remove(next_el)

    def reverse(self) -> XorDoublyLinkedList:
        """Returns the same list but in the reserved order
        Complexity: O(1)
        """

        self.head, self.tail = self.tail, self.head
        return self


if __name__ == "__main__":
    with open("./xor_list_cases.yaml", "r") as f:
        cases = yaml.safe_load(f)

    for i, c in enumerate(cases):
        l = XorDoublyLinkedList()
        for el in reversed(c["input"]["list"]):
            l.insert(Element(key=el))
        for op_info in c["input"]["ops"]:
            if op_info["op"] == "insert":
                l.insert(Element(key=op_info["key"]))
            elif op_info["op"] == "remove":
                l.remove(Element(key=op_info["key"]))
            elif op_info["op"] == "reverse":
                l = l.reverse()
        py_list = l.to_pylist()
        print(py_list)
        print(f"Case #{i + 1}: {py_list == c['output']}")
