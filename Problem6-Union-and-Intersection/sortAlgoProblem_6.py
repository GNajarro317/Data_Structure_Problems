# Node class represents a single node in the linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


# LinkedList class represents the entire linked list
class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    # Append a new node to the end of the linked list
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    # Get the size of the linked list
    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

# Union function combines two linked lists and removes duplicates
def union(llist_1, llist_2):
    result = LinkedList()
    seen = set()

    node = llist_1.head
    while node:
        result.append(node.value)
        seen.add(node.value)
        node = node.next

    node = llist_2.head
    while node:
        if node.value not in seen:
            result.append(node.value)
            seen.add(node.value)
        node = node.next

    return result

# Intersection function finds the common elements between two linked lists
def intersection(llist_1, llist_2):
    result = LinkedList()
    seen = set()

    node = llist_1.head
    while node:
        seen.add(node.value)
        node = node.next

    node = llist_2.head
    while node:
        if node.value in seen:
            result.append(node.value)
            seen.remove(node.value)
        node = node.next

    return result

# Test Case 1: Linked Lists with very large values
llist_1 = LinkedList()
llist_2 = LinkedList()

for i in range(1, 1001):
    llist_1.append(i)
    llist_2.append(i + 500)

print("Union of linked lists with very large values:")
print(union(llist_1, llist_2))

print("Intersection of linked lists with very large values:")
print(intersection(llist_1, llist_2))

# Test Case 2: Linked Lists with common and unique elements
llist_1 = LinkedList()
llist_2 = LinkedList()

llist_1.append(1)
llist_1.append(2)
llist_1.append(3)
llist_1.append(4)

llist_2.append(2)
llist_2.append(4)
llist_2.append(5)
llist_2.append(6)

print("Union of linked lists with common and unique elements:")
print(union(llist_1, llist_2))

print("Intersection of linked lists with common and unique elements:")
print(intersection(llist_1, llist_2))

# Test Case 3: One set is empty
llist_1 = LinkedList()
llist_2 = LinkedList()

llist_1.append(1)
llist_1.append(2)
llist_1.append(3)

print(union(llist_1, llist_2))  # Output: 1 -> 2 -> 3

# Test Case 4: Both sets are empty
llist_1 = LinkedList()
llist_2 = LinkedList()

print(union(llist_1, llist_2))  # Output: 

# Test Case 5
llist_1 = LinkedList()
llist_2 = LinkedList()

llist_2.append(4)
llist_2.append(5)
llist_2.append(6)

print(union(llist_1, llist_2))  # Output: 4 -> 5 -> 6