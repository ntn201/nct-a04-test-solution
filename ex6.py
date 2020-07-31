# [ [ ( {     } ) [] ] ]
from stack import Stack

def match(a,b):
    if a == "(":
        if b != ")":
            return False
        return True
    if a == "[":
        if b != "]":
            return False
        return True
    if a == "{":
        if b != "}":
            return False
        return True

def is_balance(string):
    s = Stack()
    for i in string:
        if i in ["(","{","["]:
            s.push(i)
        if i in [")","}","]"]:
            temp = s.pop()
            if match(temp,i) == False:
                return False
    return s.is_empty()

print(is_balance("[[({})[]]]"))