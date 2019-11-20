BRACKETS = {
    '(': ')',
    '{': '}',
    '[': ']'
}


def check(expr):
    stack = []
    for char in expr:
        if char in BRACKETS:
            stack.append(BRACKETS[char])
        elif char in BRACKETS.values() and char != stack.pop():
            return False
    return not stack


print(check("{'abc', 'efg',[1,2]], 'ij'),32}"))
print(check("[['a',{'b'}},'c']"))
print(check("[[[{['a'],'b'},'c']],'d']"))
print(check("[[{[['a'],'b'},'c']],'d']"))
