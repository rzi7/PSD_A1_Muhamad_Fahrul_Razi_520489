class Stack:
    def __init__(self):
        self.item = []

    def push(self, item):
        return self.item.append(item)
    
    def pop(self):
        return self.item.pop()

    def peek(self):
        return self.item[-1]
    
    def isEmpty(self):
        return len(self.item) == 0
    
    def size(self):
        return len(self.item)
    
    def postfix(self, expression):
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        output = []
        operators = Stack()

        for char in expression:
            if char.isalnum():
                output.append(char)
            elif char == '(':
                operators.push(char)
            elif char == ')':
                while operators.peek() != '(' and not operators.isEmpty():
                    output.append(operators.pop())
                operators.pop()  # Pop the '('
            else:
                while (not operators.isEmpty() and precedence.get(char, 0) <= precedence.get(operators.peek(), 0)):
                    output.append(operators.pop())
                operators.push(char)

        while not operators.isEmpty():
            output.append(operators.pop())

        return ''.join(output)
    
stack = Stack()

infix = input()
stack.push("___")
postfix = stack.postfix(infix)
print(f"postfix = {postfix}")