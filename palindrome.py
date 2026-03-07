"""
Name: Neel Srivastava
Date: 6/3/26
Assignment: Palindrome, 7.2
Summary: The program checks inputted strings to see if they are palindromes, utilizes stack implementation.
Has a menu with a palindrome checker operation as well as a quit operation
"""


class Stack:
    """A simple stack implementation using a Python list."""

    def __init__(self):
        self._data = []

    def push(self, item):
        """
        Push an item onto the top of the stack.

        :param item: The item to push onto the stack.
        :return: None
        """
        self._data.append(item)

    def pop(self):
        """
        Remove and return the top item of the stack.

        :return: The item at the top of the stack.
        :raises IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self._data.pop()

    def peek(self):
        """
        Return the top item without removing it.

        :return: The item at the top of the stack.
        :raises IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("peek at an empty stack")
        return self._data[-1]

    def is_empty(self):
        """
        Check whether the stack contains no items.

        :return: True if the stack is empty, False otherwise.
        """
        return len(self._data) == 0

    def size(self):
        """
        Return the number of items currently in the stack.

        :return: Integer count of items in the stack.
        """
        return len(self._data)


def isPalindrome(text: str):
    """
    Determine whether a string is a palindrome using a stack.

    Normalises the input to lowercase alphanumeric characters, pushes
    each character onto a stack, then pops them off to form the reversed
    string, and compares it to the original normalised string.

    :param text: The string to test for palindrome property.
    :return: True if text is a palindrome, False otherwise.
    """
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())

    if len(cleaned) == 0:
        return True

    stack = Stack()
    for ch in cleaned:
        stack.push(ch)

    reversed_str = ""
    while not stack.is_empty():
        reversed_str += stack.pop()

    return cleaned == reversed_str


def main():
    """
    Repeatedly prompt the user for input and report whether each string
    is a palindrome. Exits when the user enters 'q' or 'Q'.

    :return: None
    """
    print("=" * 50)
    print("   Palindrome Checker   ")
    print("=" * 50)
    print("Enter a string to check, or 'q' / 'Q' to quit.\n")

    while True:
        user_input = input("Enter string: ")

        if user_input.strip().lower() == "q":
            print("Goodbye!")
            break

        if isPalindrome(user_input):
            print(f'"{user_input}" IS a palindrome.\n')
        else:
            print(f'"{user_input}" is NOT a palindrome.\n')


if __name__ == "__main__":
    main()