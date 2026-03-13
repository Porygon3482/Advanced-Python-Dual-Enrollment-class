"""
Name: Neel Srivastava
Project: Convert from infix expressions to postfix expressions
Date: 12/3/26
Summary: Converts infix expressions to postfix form using a stack.
Operators are held on the stack until a lower precedence operator
or end of expression forces them to the output.
"""

from tokens import Token
from scanner import Scanner
from arraystack import ArrayStack


class IFToPFConverter(object):

    def __init__(self, scanner):
        """
        Initializes the converter with a Scanner object wrapping the infix expression.

        :param scanner: A Scanner instance positioned at the start of the infix expression.
        :return: None
        """
        self.scanner = scanner

    def convert(self):
        """
        Reads tokens one at a time and builds the postfix output using a stack.
        Integers are appended directly to output, while operators are pushed onto
        the stack and popped when a lower or equal precedence operator is encountered.

        :param: None
        :return: A list of Token objects representing the postfix form of the infix expression.
        """
        postfix = []
        stack = ArrayStack()

        while self.scanner.hasNext():
            currentToken = self.scanner.next()

            if currentToken.getType() == Token.INT:
                postfix.append(currentToken)

            elif str(currentToken) == '(':
                stack.push(currentToken)

            elif str(currentToken) == ')':
                while str(stack.peek()) != '(':
                    postfix.append(stack.pop())
                stack.pop()

            else:
                while not stack.isEmpty() and \
                      str(stack.peek()) != '(' and \
                      stack.peek().getPrecedence() >= currentToken.getPrecedence():
                    postfix.append(stack.pop())
                stack.push(currentToken)

        while not stack.isEmpty():
            postfix.append(stack.pop())

        return postfix


def main():
    """
    Repeatedly prompts the user for an infix expression and prints its postfix equivalent.
    Entering a blank line exits the loop.

    :param: None
    :return: None
    """
    print("Infix-to-Postfix Converter")
    print("Enter a blank line to quit.\n")
    while True:
        sourceStr = input("Enter an infix expression: ").strip()
        if sourceStr == "":
            break
        scanner = Scanner(sourceStr)
        converter = IFToPFConverter(scanner)
        postfix = converter.convert()
        postfixStr = " ".join(str(token) for token in postfix)
        print("Postfix expression:", postfixStr)
        print()


if __name__ == "__main__":
    main()
