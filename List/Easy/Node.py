from typing import Any, Optional, TypeVar

T = TypeVar('T')  # Generic type for data


class SingleLinkedList:
    """Robust singly linked list node with type hints and debug support."""

    def __init__(self, data: T):
        self.data: T = data
        self.next: Optional['SingleLinkedList'] = None

    def __repr__(self) -> str:
        return f"SingleLinkedList(data={self.data}, next={self.next.data if self.next else None})"


class DoubleLinkedList(SingleLinkedList):
    """Robust doubly linked list node (extends SinglyNode)."""

    def __init__(self, data: T, prev: Optional['DoubleLinkedList'] = None):
        super().__init__(data)
        self.prev: Optional['DoubleLinkedList'] = prev

    def __repr__(self) -> str:
        return (f"DoubleLinkedList(data={self.data}, "
                f"prev={self.prev.data if self.prev else None}, "
                f"next={self.next.data if self.next else None})")
