from stack import Stack


def is_balanced(expression):
    stack = Stack()
    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']

    for char in expression:
        if char in opening_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if stack.is_empty():
                return "Несбалансированно"
            top = stack.pop()
            if not is_matching_brackets(top, char):
                return "Несбалансированно"

    if stack.is_empty():
        return "Сбалансированно"
    else:
        return "Несбалансированно"


def is_matching_brackets(opening, closing):
    if opening == '(' and closing == ')':
        return True
    elif opening == '[' and closing == ']':
        return True
    elif opening == '{' and closing == '}':
        return True
    else:
        return False


if __name__ == '__main__':
    print(is_balanced("(((([{}]))))"))  # Сбалансированно
    print(is_balanced("[([])((([[[]]])))]{()}"))  # Сбалансированно
    print(is_balanced("{{[()]}}"))  # Несбалансированно
    print(is_balanced("}{"))  # Несбалансированно
    print(is_balanced("{{[(])]}}"))  # Несбалансированно
    print(is_balanced("[[{())}]"))  # Несбалансированно
