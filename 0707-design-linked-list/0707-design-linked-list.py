class MyLinkedList:

    def __init__(self):
        self.l = []

    def get(self, index: int) -> int:
        if 0 <= index < len(self.l):
            return self.l[index]
        return -1

    def addAtHead(self, val: int) -> None:
        self.l = [val] + self.l

    def addAtTail(self, val: int) -> None:
        self.l.append(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if 0 <= index <= len(self.l):
            self.l = self.l[:index] + [val] + self.l[index:]

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < len(self.l):
            self.l = self.l[:index] + self.l[index + 1:]
