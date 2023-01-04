import os
import re


def clear(): return os.system('cls')


clear()


class Node:
    def __init__(self, product, next_node=None):
        self.product = product
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def add_product(self, product):
        new_node = Node(product)
        new_node.next_node = self.head
        self.head = new_node

    def print_products(self):
        current_node = self.head
        while current_node:
            print(current_node.product)
            current_node = current_node.next_node


product_list = LinkedList()

while True:
    user_input = input("Enter a two-letter code followed by a dash and a number between 200 and 700 (XX-###) or type 'exit' to exit: ")
    if user_input.strip().lower() == "exit":
        break
    if not user_input:
        print("Input is empty. Please try again.")
        continue
    pattern = r"^[a-zA-Z]{2}-\d{3}$"
    if re.match(pattern, user_input):
        number = int(user_input[3:])
        if 200 <= number <= 700:
            product_list.add_product(user_input)
            continue
        elif number < 200 or number > 700:
            print("Number is out of range. Please try again.")
            continue
    else:
        print("Input does not match pattern. Please try again.")
        continue
product_list.print_products()
