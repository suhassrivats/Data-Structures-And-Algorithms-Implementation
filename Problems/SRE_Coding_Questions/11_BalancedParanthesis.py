"""
Balanced Parentheses Exercise
Return True if the equation is balanced. False otherwise.
In real life you can see this extend to many things such as text editor plugins
and interactive development environments for all sorts of bracket completion
checks. Take a string as an input and return True if it's parentheses are
balanced or False if it is not.

Ex: ((32+8)∗(5/2))/(2+6)
"""


def balanced_paranthesis(equation):
    if not equation:
        return True
    stack = []
    for c in equation:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if stack:
                # It means that there is no opening bracket bracket for a closing one.
                if stack.pop() == None:
                    return False
    return len(stack) == 0


def main():
    print("Pass" if (balanced_paranthesis('((3^2 + 8)*(5/2))/(2+6)')) else "Fail")
    print("Pass" if not (balanced_paranthesis('((3^2 + 8)*(5/2))/(2+6))')) else "Fail")


if __name__ == '__main__':
    main()
